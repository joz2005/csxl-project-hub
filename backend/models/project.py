from pydantic import BaseModel

__authors__ = ["Zhi Hang Yang", "Joseph Zheng", "Kaw Bu", "Kamal Deep Vasireddy"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"


class Project(BaseModel):
    """
    Pydantic model to represent a `Project`.

    This model is based on the `ProjectEntity` model, which defines the shape
    of the `Project` database in the PostgreSQL database.
    """

    id: int | None
    author_id: int | None
    author: str
    image: str
    title: str
    short_description: str
    long_description: str
    requirements: str
    additional_info: str
    email: str
    phone_number: str
    linked_in: str
    public: bool
    slug: str
