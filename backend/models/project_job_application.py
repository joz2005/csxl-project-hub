from pydantic import BaseModel


class ProjectJobApplication(BaseModel):
    """
    Pydantic model to represent a `ProjectJobApplication`.

    This model is based on the `ProjectJobApplicationEntity` model, which defines the shape
    of the `ProjectJobApplication` database in the PostgreSQL database.
    """

    id: int | None
    user_id: int
    poster_id: int
    project_id: int
    personal_statement: str
    experience: str
    gpa: float
    skills: str
    contact: str
