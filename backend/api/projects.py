"""Project API

Project routes are used to create, retrieve, and update Projects."""

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException

from ..services import ProjectService
from ..services.projectai import ProjectAIService
from ..models.project import Project
from ..models.project_details import ProjectDetails
from ..models.openai_project import OpenAIProjectResponse
from ..api.authentication import registered_user
from ..models.user import User
from ..models.resume import Resume


__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

api = APIRouter(prefix="/api/projects")
openapi_tags = {
    "name": "Projects",
    "description": "Create, update, delete, and retrieve CS projects.",
}


@api.get("", response_model=list[Project], tags=["Projects"])
def get_projects(
    project_service: ProjectService = Depends(),
) -> list[Project]:
    """
    Get all projects

    Parameters:
        project_service: a valid ProjectService

    Returns:
        list[Project]: All `Project`s in the `Project` database table
    """

    # Return all projects
    return project_service.all()


'''@api.post("", response_model=Project, tags=["Projects"])
def new_project(
    project: Project,
    subject: User = Depends(registered_user),
    project_service: ProjectService = Depends(),
    role_service: RoleService = Depends(),
) -> Project:
    """
    Create project

    Parameters:
        project: a valid Project model
        subject: a valid User model representing the currently logged in User
        project_service: a valid ProjectService

    Returns:
        Project: Created project

    Raises:
        HTTPException 422 if create() raises an Exception
    """

    new_project = project_service.create(subject, project)
    # Create a new role for the project newly created
    role_service.create(subject, new_project.slug)
    return new_project
'''


@api.get(
    "/{slug}",
    responses={404: {"model": None}},
    response_model=ProjectDetails,
    tags=["Projects"],
)
def get_project_by_slug(
    slug: str, project_service: ProjectService = Depends()
) -> ProjectDetails:
    """
    Get project with matching slug

    Parameters:
        slug: a string representing a unique identifier for an Project
        project_service: a valid ProjectService

    Returns:
        Project: Project with matching slug

    Raises:
        HTTPException 404 if get_by_slug() raises an Exception
    """

    return project_service.get_by_slug(slug)


@api.post(
    "/resume",
    responses={404: {"model": None}},
    response_model=Resume,
    tags=["Projects"],
)
def post_resume(
    resume: UploadFile = File(...), project_service: ProjectService = Depends()
) -> Resume:
    return project_service.post_resume(resume)


@api.post(
    "/recommendation",
    responses={404: {"model": None}},
    response_model=OpenAIProjectResponse,
    tags=["Projects"],
)
def recommend_project(
    resume: UploadFile = File(...),
    # If needed, require authenticated user:
    # subject: User = Depends(registered_user),
    project_service: ProjectService = Depends(),
    project_ai_service: ProjectAIService = Depends(),
) -> OpenAIProjectResponse:
    # Extract text from resume without persisting it publicly.
    resume_obj: Resume = project_service.post_resume(resume)

    if not resume_obj.content.strip():
        raise HTTPException(
            status_code=400, detail="Failed to extract content from the resume."
        )

    # Immediately obtain the recommendation from the AI service.
    recommendation: OpenAIProjectResponse = project_ai_service.get_recommendation(
        resume_obj
    )

    # Return the recommendation to the user.
    return recommendation
  
  
'''@api.put(
    "",
    responses={404: {"model": None}},
    response_model=Project,
    tags=["Projects"],
)
def update_project(
    project: Project,
    subject: User = Depends(registered_user),
    project_service: ProjectService = Depends(),
) -> Project:
    """
    Update project

    Parameters:
        project: a valid Project model
        subject: a valid User model representing the currently logged in User
        project_service: a valid ProjectService

    Returns:
        Project: Updated project

    Raises:
        HTTPException 404 if update() raises an Exception
    """

    return project_service.update(subject, project)


@api.delete("/{slug}", response_model=None, tags=["Projects"])
def delete_project(
    slug: str,
    subject: User = Depends(registered_user),
    project_service: ProjectService = Depends(),
):
    """
    Delete project based on slug

    Parameters:
        slug: a string representing a unique identifier for an Project
        subject: a valid User model representing the currently logged in User
        project_service: a valid ProjectService

    Raises:
        HTTPException 404 if delete() raises an Exception
    """

    project_service.delete(subject, slug)
'''
