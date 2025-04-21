from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.services.exceptions import ResourceNotFoundException

from ..database import db_session
from ..models import User
from ..models.project import Project
from ..models.project_details import ProjectDetails
from .permission import PermissionService


__authors__ = ["Kaw BU", "Joseph", "Kamal Deep", "Zhi Yang"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

global mock_project, mock_project_2
mock_project = Project(
    id=1,
    author="Jane Doe",
    image="https://example.com/images/project-thumbnail.jpg",
    title="Smart Campus Energy Tracker",
    short_description="Track and optimize energy usage across campus buildings.",
    long_description=(
        "This project involves building a real-time dashboard that collects and visualizes "
        "energy consumption data across different facilities on campus. The goal is to reduce energy "
        "waste, promote sustainability, and provide actionable insights to facility managers."
    ),
    requirements=(
        "- Experience with Python and FastAPI\n"
        "- Familiarity with IoT and sensor data\n"
        "- Bonus: Knowledge of energy systems or building automation"
    ),
    additional_info="We’ll be presenting this project at the university's sustainability fair.",
    email="jane.doe@example.com",
    phone_number="(555) 123-4567",
    linked_in="https://linkedin.com/in/janedoe",
    public=True,
    slug="smart-campus-energy-tracker",
)
mock_project_2 = Project(
    id=2,
    author="Carlos Nguyen",
    image="https://example.com/images/agri-ai.jpg",
    title="AI-Powered Crop Disease Detection",
    short_description="Use AI to identify plant diseases from images.",
    long_description=(
        "This project aims to develop a machine learning model that can detect common crop diseases "
        "from leaf images. It will help farmers diagnose issues early and reduce crop loss. The app will "
        "also suggest remedies and connect users to agricultural experts."
    ),
    requirements=(
        "- Knowledge of machine learning and image classification\n"
        "- Python (TensorFlow or PyTorch preferred)\n"
        "- Optional: Familiarity with agriculture or plant science"
    ),
    additional_info=(
        "The project is part of a university research initiative and has potential for publication. "
        "You'll work with a diverse, cross-disciplinary team."
    ),
    email="carlos.nguyen@example.com",
    phone_number="(555) 987-6543",
    linked_in="https://linkedin.com/in/carlosnguyen",
    public=False,
    slug="ai-crop-disease-detector",
)


class ProjectService:
    """
    Service that performs all of the actions on the `Project` table
    """

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission: PermissionService = Depends(),
    ):
        """Initializes the `OrganizationService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission

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

        return [mock_project, mock_project_2]

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

        project: Project

        if slug == "smart-campus-energy-tracker":
            project = mock_project
        elif slug == "ai-crop-disease-detector":
            project = mock_project_2

        # Check if result is null
        if project is None:
            raise ResourceNotFoundException(
                f"No project found with matching slug: {slug}"
            )

        return ProjectDetails(**project.__dict__)
