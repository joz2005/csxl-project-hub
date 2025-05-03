from pydantic import BaseModel
from .project import Project

__authors__ = ["Zhi Hang Yang", "Joseph Zheng", "Kaw Bu", "Kamal Deep Vasireddy"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"


class OpenAIProjectResponse(BaseModel):

    listings: list[Project]
