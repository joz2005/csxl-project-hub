from pydantic import BaseModel


class Resume(BaseModel):

    id: int | None
    content: str
