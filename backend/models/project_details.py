from pydantic import BaseModel
from .project import Project
from .event import EventOverview

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class ProjectDetails(Project):
    """
    Pydantic model to represent an `Project`, including back-populated
    relationship fields.

    This model is based on the `ProjectEntity` model, which defines the shape
    of the `Project` database in the PostgreSQL database.
    """

    resume: str = "hello world"  # Placeholder for resume or other details
