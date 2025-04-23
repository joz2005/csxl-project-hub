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

    def post_application(self, application: Project) -> Project:
        """
        Post a new application to the database

        Parameters:
            application: a valid Project model

        Returns:
            Project: Created project
        """
        # Create a new project in the database
        new_project = ProjectEntity.from_model(application)
        self._session.add(new_project)
        self._session.commit()
        return new_project.to_model()

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
