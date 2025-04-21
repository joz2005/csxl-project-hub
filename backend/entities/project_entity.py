from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .entity_base import EntityBase
from typing import Self
from ..models.project import Project
from ..models.project_details import ProjectDetails


class ProjectEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `Organization` table"""

    # Name for the organizations table in the PostgreSQL database
    __tablename__ = "project"

    # Organization properties (columns in the database table)

    # Unique ID for the organization
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    short_description: Mapped[str] = mapped_column(String)
    long_description: Mapped[str] = mapped_column(String)
    requirements: Mapped[str] = mapped_column(String)
    additional_info: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    linked_in: Mapped[str] = mapped_column(String)
    public: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
      

    @classmethod
    def from_model(cls, model: Project) -> Self:
        """
        Class method that converts a `Project` model into a `ProjectEntity`

        Parameters:
            - model (Project): Model to convert into an entity
        Returns:
            ProjectEntity: Entity created from model
        """
        return cls(
            id=model.id,
            author=model.author,
            image=model.image,
            title=model.title,
            short_description=model.short_description,
            long_description=model.long_description,
            requirements=model.requirements,
            additional_info=model.additional_info,
            email=model.email,
            phone_number=model.phone_number,
            linked_in=model.linked_in,
            public=model.public,
            slug=model.slug,
        )

    def to_model(self) -> Project:
        """
        Converts a `ProjectEntity` object into a `Project` model object

        Returns:
            Project: `Project` object from the entity
        """
        return Project(
            id=self.id,
            author=self.author,
            image=self.image,
            title=self.title,
            short_description=self.short_description,
            long_description=self.long_description,
            requirements=self.requirements,
            additional_info=self.additional_info,
            email=self.email,
            phone_number=self.phone_number,
            linked_in=self.linked_in,
            public=self.public,
            slug=self.slug,
        )

    def to_details_model(self) -> ProjectDetails:
        """
        Converts a `ProjectEntity` object into a `ProjectDetails` model object

        Returns:
            ProjectDetails: `ProjectDetails` object from the entity
        """
        return ProjectDetails(
            id=self.id,
            author=self.author,
            image=self.image,
            title=self.title,
            short_description=self.short_description,
            long_description=self.long_description,
            requirements=self.requirements,
            additional_info=self.additional_info,
            email=self.email,
            phone_number=self.phone_number,
            linked_in=self.linked_in,
            public=self.public,
            slug=self.slug,
        )
