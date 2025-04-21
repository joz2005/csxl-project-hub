from pydantic import BaseModel
from .project import Project


class OpenAIProjectResponse(BaseModel):

    listings: list[Project]
