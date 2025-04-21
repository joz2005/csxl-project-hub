from pydantic import BaseModel


class OpenAIProjectRecResponse(BaseModel):
    """Response model for OpenAI test endpoint."""

    recommended_project: str
    reasoning: str
