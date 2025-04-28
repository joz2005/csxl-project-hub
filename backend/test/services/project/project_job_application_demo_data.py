import pytest
from sqlalchemy.orm import Session
from ....models.project_job_application import ProjectJobApplication
from ....entities.project_job_app_entity import ProjectJobApplicationEntity
from ..reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kaw Bu"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"

application1 = ProjectJobApplication(
    id=1,
    project_id=1,
    poster_id=7,
    user_id=1,
    personal_statement="I am passionate about mental health advocacy and believe MindMate can make a real difference for students like me. My experience organizing campus wellness events gives me a unique perspective on student needs.",
    experience="2 years volunteering at university counseling center, led mindfulness workshops for peers.",
    gpa=3.8,
    skills="Public speaking, event planning, basic app prototyping",
    contact="rhonda.root@example.com",
)

application2 = ProjectJobApplication(
    id=2,
    project_id=2,
    poster_id=8,
    user_id=2,
    personal_statement="As a software engineering major with a strong interest in navigation technology, I am excited to contribute to UNC Campus Navigator. I am particularly interested in applying my AR skills to help new students.",
    experience="Completed a mobile development internship building GPS-enabled fitness apps.",
    gpa=3.6,
    skills="Android development, ARCore, Java, Kotlin",
    contact="amy.ambassador@example.com",
)

application3 = ProjectJobApplication(
    id=3,
    project_id=5,
    poster_id=11,
    user_id=3,
    personal_statement="My passion lies at the intersection of technology and career development. UNC Career Connect’s mission aligns perfectly with my goal to empower students to discover their future opportunities.",
    experience="Worked as a peer career coach assisting students with resume and internship searches.",
    gpa=3.9,
    skills="Full-stack web development (MERN), LinkedIn scraping, resume critique",
    contact="sally.student@example.com",
)

applications = [application1, application2, application3]

def insert_fake_data(session: Session):
    global applications
    entities = []
    for application in applications:
        entity = ProjectJobApplicationEntity.from_model(application)
        session.add(entity)
        entities.append(entity)

    reset_table_id_seq(
        session,
        ProjectJobApplicationEntity,
        ProjectJobApplicationEntity.id,
        len(applications) + 1,
    )

    session.commit()

@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
