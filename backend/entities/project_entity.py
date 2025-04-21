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
