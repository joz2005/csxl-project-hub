# Projects Feature Technical Specification

> Written by []() for the CSXL Web Application.<br> _Last Updated: 05/02/2025_ <br>
> Inspired by [Ajay Gandecha](https://github.com/ajaygandecha)

This document outlines the technical specifications for the Projects feature of the CSXL web application. This feature introduces 2 new database tables, new API endpoints, and multiple Angular components to support posting projects, finding projects, project applications, and AI-driven recommendations.

The Projects feature enables users to post and manage project listings, as well as apply to open positions with customized application content. It also allows project owners to review submissions. Each project contains detailed information including descriptions, requirements, and contact details. Applicants can provide relevant experience, GPA, and personal statements through structured forms.

All visitors to the CSXL platform can browse a comprehensive list of available technical projects. Logged-in users can submit applications, and optionally upload their resume to receive AI-generated project recommendations based on similarity to posted descriptions. Project listings and applicant data are modifiable by their respective authors.

## Table of Contents

- [Frontend Features](#FrontendFeatures)
  - [User Features](#UserFeatures)
    - [Homepage](#Homepage)
    - [Project Details Page](#ProjectDetailsPage)
    - [Applications Page](#ApplicationsPage)
    - [Posting Project](#PostingProject)
    - [Applying to Project](#ApplyingProject)
- [Backend Design and Implementation](#BackendDesignandImplementation)
  - [Entity Design](#EntityDesign)
  - [Pydantic Model Implementation](#PydanticModelImplementation)
  - [API Implementation](#APIImplementation)
    - [AI Implementation](#AIImplementation)
  - [Testing](#Testing)
  - [User Narratives](#UserNarratives)

## Frontend Features<a name="FrontendFeatures"></a>

The frontend portion of the Projects feature includes components that allow users to create new project listings, apply to projects, and receive personalized AI-powered project recommendations. All features are implemented using Angular components and interact with FastAPI backend services.

### User Features<a name="UserFeatures"></a>

#### Homepage<a name="Homepage"></a>

![Projects Homepage UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/project-homepage.png)

The homepage for the Projects feature serves as the entry point for users interested in exploring available projects or submitting new ones. It provides a clear overview of all publicly listed projects and offers intuitive navigation for both browsing and interaction.

Key elements of the homepage include:

- **Project Feed**: Displays a scrollable list of available projects, each rendered using the `project-card` widget. Each card includes the key information like title and description.
- **Search**: Users can search for projects by keyword.
- **Call-to-Action Buttons**: Prominent buttons allow users to create a new project or upload a resume to get AI-generated project recommendations.

The design focuses on simplicity and discoverability, ensuring users can quickly engage with content or take action.

The homepage integrates tightly with backend APIs to fetch project data.

These features are accessible to all authenticated users of the CSXL platform and are designed to support seamless project exploration and application submission.

#### Project Details Page<a name="ProjectDetailsPage"></a>

![Project Details Page UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/project-details-page.png)

The project details page displays in-depth information about a selected project. It is accessed by clicking on a project card from the homepage or search results. The page is rendered using the `project-details-info-card` widget, which fetches and displays all metadata associated with a project.

Key elements shown on the details page:

- **Full Description**: Includes both short and long descriptions to provide a comprehensive overview of the project.
- **Requirements**: Clearly outlines what the project creator expects from applicants.
- **Contact Information**: Includes the poster's email, phone number, and LinkedIn.
- **Apply Button**: Triggers the application modal to allow users to apply directly from the details view.
- **Delete Button** (conditional): If the logged-in user is the creator, they have the option to delete their project.

The page is powered by a slug-based route and uses the backend API (`GET /api/projects/{slug}`) to retrieve the associated data in real time.

#### Applications Page<a name="ApplicationsPage"></a>

![Applications Page UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/applications-page.png)

The applications page allows both project owners and applicants to view and manage job applications tied to projects.

**For Project Owners:**
This page displays all submissions received for projects they have posted. It is designed to help owners review applicant qualifications quickly and efficiently.

Key features for owners:

- **Applicant List**: Shows all applications submitted to their projects.
- **Inline Application Cards**: Each card contains the applicant's personal statement, GPA, experience, skills, and contact information.
- **Delete Button**: Allows the project owner to delete an application.
- **AI Recommendation Sorting**: Owners can use the AI resume scoring interface to sort applicants based on semantic similarity to the project description (see [AI Implementation](#AIImplementation)).

**For Applicants:**
Applicants can also access this page to view their own submitted applications.

Key features for applicants:

- **View Submitted Applications**: Users can see all the projects they've applied to, along with the details of their submission.
- **Withdraw Option**: Each application includes a "Withdraw" button, which allows applicants to delete their own submissions.

The page uses conditional logic to determine whether the logged-in user is the owner or the applicant of each application, and displays the appropriate controls. All data is fetched dynamically via the `/api/projects/job-applications` route, with permission filtering enforced on the backend.

#### Posting Project<a name="PostingProject"></a>

![Posting Project UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/add-project.png)

Users can post a new project using the `add-job` widget. This is a form where users provide essential project details such as title, description, requirements, and contact information. Once submitted, the data is sent to the backend API and persisted in the `project` table via the `ProjectEntity` SQLAlchemy model.

The key fields users must fill out include:

- **Title**: A clear, concise project title
- **Short & Long Description**: Context and expectations for the project
- **Requirements**: Desired qualifications or skill sets
- **Contact Info**: Email, phone number, and LinkedIn

After submission, the project appears in the general listing and is accessible for browsing by other users. Authenticated users can also view their own submitted projects and have the option to delete.

#### Applying to Project<a name="ApplyingProject"></a>

![Applying to Project UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/apply-project.png)

Each project listing includes an **Apply** button that opens a modal implemented with the `apply-job-dialog` widget. This form allows users to submit a personalized application by filling out:

- **Personal Statement**: A written explanation of why the applicant is a good fit
- **Experience**: Relevant work, academic, or extracurricular experience
- **GPA**: Self-reported GPA value
- **Skills**: A comma-separated list of skills
- **Contact Info**: Email or phone

Once submitted, this information is packaged into a `ProjectJobApplication` object and sent to the backend, where it is validated and stored in the `project_job_application` table. The listing owner can later view and review all applications to their project.

This flow enables customized, project-specific applications rather than generic form submissions, giving project owners meaningful insights into applicant fit.

Users can also upload a resume for AI-assisted project matching, which is documented in the [AI Implementation](#AIImplementation) section.

## Backend Design and Implementation<a name='BackendDesignandImplementation'></a>

The Projects feature adds _2_ new database tables and _9_ API endpoints.

---

### Entity Design<a name='EntityDesign'></a>

The Projects Feature introduces the following database entities:

| Table Name                | Entity Class                  | Description                                        |
| ------------------------- | ----------------------------- | -------------------------------------------------- |
| `project`                 | `ProjectEntity`               | Stores metadata about each user-created project    |
| `project_job_application` | `ProjectJobApplicationEntity` | Stores applications from users to project listings |

These tables are defined using SQLAlchemy models in `project_entity.py` and `project_job_app_entity.py`. Each project contains detailed information such as the author, description, requirements, contact info, etc. Each job application references the user and project it belongs to, along with resume-style fields like GPA, experience, and personal statement.

An overview of the fields and relationships is shown below:

![Entity Design](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/project-entity-diagram.png)

### Pydantic Model Implementation<a name='PydanticModelImplementation'></a>

The Projects feature defines Pydantic models that mirror the structure of the SQLAlchemy entities. These models are used to validate data at API boundaries. (i.e converting from models to entities and entities to models)

The two primary models are `Project` and `ProjectJobApplication`, both located in the `models` directory.

<table>
<tr><th width="520">`Project`, `ProjectDetails` and `ProjectJobApplication` Models</th></tr>
<tr>
<td>

```py
# project.py
class Project(BaseModel):
    id: int | None
    author_id: int | None
    author: str
    image: str
    title: str
    short_description: str
    long_description: str
    requirements: str
    additional_info: str
    email: str
    phone_number: str
    linked_in: str
    public: bool
    slug: str

# project_details.py
class ProjectDetails(Project):
    resume: str = "hello world"


# project_job_application.py
class ProjectJobApplication(BaseModel):
    id: int | None
    user_id: int
    poster_id: int
    project_id: int
    personal_statement: str
    experience: str
    gpa: float
    skills: str
    contact: str
```

</td>
</tr>
</table>



**Purpose:**  
These models define the data structure for creating, displaying, and applying to user-generated projects.

- `Project` holds metadata about a project such as title, description, contact info, and visibility.
- `ProjectDetails` extends `Project` for full-page project views and may include additional fields.
- `ProjectJobApplication` captures structured application input like GPA, skills, experience, and personal statements submitted by users applying to a project.

**Used in:**

- Creating and retrieving project listings (`POST /api/projects`, `GET /api/projects`)
- Fetching individual project detail pages (`GET /api/projects/{slug}`)
- Submitting applications to projects (`POST /api/projects/job-applications`)
- Listing and managing applications (`GET`/`DELETE /api/projects/job-applications`)

There is also an additional model to support AI integration called `openai_project`.

<table> <tr><th width="520">AI-Specific Models</th></tr>
<tr> 
<td>

 ```py
# openai_project.py
class OpenAIProjectResponse(BaseModel):
    listings: list[Project]
```
 </td>
 </tr>
 </table>



**Purpose:**  
This model structure the AI-generated recommendations. `OpenAIProjectResponse` wraps a list of matching projects based on resume content. `OpenAIProjectRecResponse` provides a text-based recommendation and explanation, useful for debugging or experimental UIs.

**Used in:**

- Returning project matches via AI (`POST /api/projects/recommendation`)

### API Implementation<a name='APIImplementation'></a>

This feature adds 9 new API routes to deliver CRUD operations on a variety of objects, such as project listings, applications, etc.

Below is a summary of these routes:

![Summary of API Routes](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/api-endpoints.png)

### Testing<a name='Testing'></a>

This feature also contains a test for each operation in the service layer of this project. With each creation of a new service method, a test accompanies its functionality. All tests pass, and general use-cases of these methods have insurance behind these tests.

## Future Considerations<a name='FutureConsiderations'></a>

- Currently, the Projects feature is fleshed out in functionality, but missing a crucial aspect of security and moderation behind these project listings and applicants. We would love to improve on this much-needed implementation in the future.
- We also want developers to be able to edit their current postings to allow for better user experience for those using this feature.
- We can consider creating a default page for specifically unauthenticated users.

## User Narratives<a name='UserNarratives'></a>

Starting from the Projects homepage, here are some narratives to follow:

### Student Candidate

You're a student who's curious about what projects you can do at UNC. Guided to the projects homepage, you see a sea of listings.

![Projects Homepage UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/project-homepage.png)

Mesmerized by the listings, you decide to click on `Recommend Projects` to get a better idea of your capabilities in relation to these projects.

![Recommend Projects UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/recommend-projects.png)

After uploading your resume, you're presented with a snackbar for the returned recommended projects.

![Recommend Projects Snackbar](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/recommend-project-snackbar.png)

Knowing what to join now, you click on the details of your desired project.

![Project Detail UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/project-details-page.png)

You then click apply, bringing up a form with relevant fields.

![Application UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/apply-project.png)

After sending the application, you're greeted with a snackbar confirming your request.

![Snackbar Sent](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/applied-snackbar.png)

After an hour, you realize that you accidently put a 5 as your gpa instead of a 4, so you go to applications withdraw your application.

![Applicants Application Page](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/applicants-application-page.png)

Now you are met with this sad blank applications page. Go apply!

![Applicants Application Page](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/blank-application.png)


### Aspiring Developer

You're a developer who wants to make it big in the industry, and CSXL's Projects feature caught your attention. On the homepage, you click on `Add a Project`.

![Add a Project Form](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/add-project.png)

After submitting your project submission, you're pulled back to the Projects page with your project displayed in the crowd of listings.

![Job Listing in Projects](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/your-posted-project.png)

After waiting for 30 minutes, you click on `Applications` and coincidentally have one new applicant to review.

![Application UI with Applicant](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/your-applicants.png)

Seeing this promising candidate show up at the doorstep of your listing, you gladly accept them, prompting an confirmation screen which also inclues the candidates contact information.

![Application Confirmation UI](https://github.com/comp423-25s/csxl-team-d8/blob/editing/kamalv-specs.md/docs/images/applicant-contact-info.png)


