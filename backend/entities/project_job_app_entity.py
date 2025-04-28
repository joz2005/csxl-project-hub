from typing import Self
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .entity_base import EntityBase
from ..models.project_job_application import ProjectJobApplication


class ProjectJobApplicationEntity(EntityBase):
    """Database schema for the `project_job_application` table."""

    __tablename__ = "project_job_application"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    poster_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    personal_statement: Mapped[str] = mapped_column(String, nullable=False)
    experience: Mapped[str] = mapped_column(String, nullable=False)
    gpa: Mapped[float] = mapped_column(Float, nullable=False)
    skills: Mapped[str] = mapped_column(String, nullable=False)
    contact: Mapped[str] = mapped_column(String, nullable=False)

    @classmethod
    def from_model(cls, model: ProjectJobApplication) -> Self:
        return cls(
            id=model.id,
            poster_id=model.poster_id,
            project_id=model.project_id,
            user_id=model.user_id,  # <-- Fixed here
            personal_statement=model.personal_statement,
            experience=model.experience,
            gpa=model.gpa,
            skills=model.skills,
            contact=model.contact,
        )

    def to_model(self) -> ProjectJobApplication:
        return ProjectJobApplication(
            id=self.id,
            poster_id=self.poster_id,
            project_id=self.project_id,
            user_id=self.user_id,
            personal_statement=self.personal_statement,
            experience=self.experience,
            gpa=self.gpa,
            skills=self.skills,
            contact=self.contact,
        )
