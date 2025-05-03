from pydantic import BaseModel

__authors__ = ["Zhi Hang Yang", "Joseph Zheng", "Kaw Bu", "Kamal Deep Vasireddy"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"


class OpenAIProjectRecResponse(BaseModel):
    """Response model for OpenAI test endpoint."""

    recommended_project: str
    reasoning: str
