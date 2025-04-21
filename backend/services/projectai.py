from ..database import db_session
from ..models import User
from ..models.project import Project
from ..models.project_details import ProjectDetails
from ..models.resume import Resume
from ..models.openai_project import OpenAIProjectResponse
from ..services.openai import OpenAIService
from .permission import PermissionService
from .project import ProjectService

from fastapi import Depends, UploadFile
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.services.exceptions import ResourceNotFoundException


class ProjectAIService:

    def __init__(
        self,
        session: Annotated[Session, Depends(db_session)],
        openai_svc: Annotated[OpenAIService, Depends()],
        permission: Annotated[PermissionService, Depends()],
        project_service: Annotated[ProjectService, Depends()],
    ):
        """Initializes the `OrganizationService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission
        self._openai_svc = openai_svc
        self.project_service = project_service

    def get_recommendation(self, resume: Resume) -> OpenAIProjectResponse:

        system_prompt = (
            "You are a student at UNC-Chapel Hill applying for a project. "
            "Here are the following projects with descriptions in JSON format: "
            f"{self.project_service.all()}"
        )
        user_prompt = (
            f"Here is the content of my resume: {resume.content}. "
            "Please recommend the best, at most 3 matching projects from the above projects."
        )
        response_model = OpenAIProjectResponse
        # Here, we assume openai_svc.prompt returns a dict that is valid for OpenAIProjectResponse.
        return self._openai_svc.prompt(system_prompt, user_prompt, response_model)
