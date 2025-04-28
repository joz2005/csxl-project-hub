from fastapi import Depends, UploadFile
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.services.exceptions import ResourceNotFoundException

import PyPDF2
import uuid

from ..database import db_session
from ..models import User
from ..models.project import Project
from ..models.project_details import ProjectDetails
from ..entities.project_entity import ProjectEntity
from ..models.resume import Resume
from ..models.openai_project import OpenAIProjectResponse
from ..services.openai import OpenAIService
from .permission import PermissionService
from ..models.project_job_application import ProjectJobApplication
from ..entities.project_job_app_entity import ProjectJobApplicationEntity


__authors__ = ["Kaw BU", "Joseph", "Kamal Deep", "Zhi Yang"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class ProjectService:
    """
    Service that performs all of the actions on the `Project` table
    """

    def __init__(
        self,
        session: Annotated[Session, Depends(db_session)],
        openai_svc: Annotated[OpenAIService, Depends()],
        permission: Annotated[PermissionService, Depends()],
    ):
        """Initializes the `OrganizationService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission
        self._openai_svc = openai_svc

    def all(self) -> list[Project]:
        """
        Retrieves all projects from the table

        Returns:
            list[Project]: List of all `Project`
        """
        # Select all entries in `Organization` table
        # query = select(OrganizationEntity)
        # entities = self._session.scalars(query).all()

        # Convert entries to a model and return

        query = select(ProjectEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def get_by_slug(self, slug: str) -> ProjectDetails:
        """
        Get the project from a slug
        If none retrieved, a debug description is displayed.

        Parameters:
            slug: a string representing a unique project slug

        Returns:
            Organization: Object with corresponding slug

        Raises:
            ResourceNotFoundException if no project is found with the corresponding slug
        """

        project = (
            self._session.query(ProjectEntity)
            .filter(ProjectEntity.slug == slug)
            .one_or_none()
        )
        # Check if result is null
        if project is None:
            raise ResourceNotFoundException(
                f"No project found with matching slug: {slug}"
            )

        return project.to_details_model()

    def post_application(self, subject: User, application: Project) -> Project:
        try:
            # Checks if the organization already exists in the table
            if application.id:
                # Set id to None so database can handle setting the id
                application.id = None

            # Create new object
            project_entity = ProjectEntity.from_model(application)

            # Add new object to table and commit changes
            self._session.add(project_entity)
            self._session.commit()

            # Return added object
            return project_entity.to_model()
        except Exception as e:
            import traceback

            print(f"Error in service post_application: {str(e)}")
            print(traceback.format_exc())
            raise

    def remove_application(self, subject: User, id: int) -> None:
        # First query the project entity
        project_entity = (
            self._session.query(ProjectEntity)
            .filter(ProjectEntity.id == id)
            .one_or_none()
        )

        # Check if the project exists in the table
        if not project_entity:
            raise ResourceNotFoundException(f"No project found with id: {id}")

        # Check if the author is the same as the user
        if project_entity.author_id != subject.id:
            raise ResourceNotFoundException(
                f"User does not have permission to delete this project"
            )

        # Delete the project from the table
        self._session.delete(project_entity)
        self._session.commit()


    def post_resume(self, resume: UploadFile) -> Resume:
        random_uuid = uuid.uuid4()
        content = ""
        try:
            pdf_reader = PyPDF2.PdfReader(resume.file)
            for page in pdf_reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    content += extracted_text
        except Exception as e:
            print(f"Error extracting PDF content: {e}")
        return Resume(id=random_uuid.int, content=content)

    def get_resume(self, id: int) -> Resume:
        pass

    # def get_reccommendation(self, id: int) -> OpenAIProjectResponse:

    #     service = ProjectService()

    #     system_prompt = (
    #         "You are a student at UNC-Chapel Hill applying for a project, "
    #         "here are the following projects with descriptions in JSON format."
    #         + str(service.all())
    #     )

    #     user_prompt = (
    #         "This is my resume contents, please match me with the listing(s) that closely pertains to my experiences and interests"
    #         + service.post_resume(resume)
    #     )

    #     response_model = OpenAIProjectResponse

    #     return self._openai_svc.prompt(system_prompt, user_prompt, response_model)

    def get_all_project_job_applications(self) -> list[ProjectJobApplication]:
        """
        Retrieves all projects from the table

        Returns:
            list[Project]: List of all `Project`
        """
        # Select all entries in `ProjectJobApplication` table
        # query = select(OrganizationEntity)
        # entities = self._session.scalars(query).all()

        # Convert entries to a model and return

        query = select(ProjectJobApplicationEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def post_job_application(
        self, subject: User, application: ProjectJobApplication
    ) -> ProjectJobApplication:
        try:
            # Create new object
            project_job_entity = ProjectJobApplicationEntity.from_model(application)

            # Add new object to table and commit changes
            self._session.add(project_job_entity)
            self._session.commit()

            # Return added object
            return project_job_entity.to_model()
        except Exception as e:
            import traceback

            print(f"Error in service post_application: {str(e)}")
            print(traceback.format_exc())
            raise

    def remove_job_application(self, subject: User, id: int) -> None:
        # First, query the job application entity
        job_application_entity = (
            self._session.query(ProjectJobApplicationEntity)
            .filter(ProjectJobApplicationEntity.id == id)
            .one_or_none()
        )

        # Check if the application exists
        if not job_application_entity:
            raise ResourceNotFoundException(f"No job application found with id: {id}")

        # Check if the user is the owner of the application
        if job_application_entity.user_id != subject.id:
            raise ResourceNotFoundException(
                f"User does not have permission to delete this job application"
            )

        # Delete the application
        self._session.delete(job_application_entity)
        self._session.commit()

