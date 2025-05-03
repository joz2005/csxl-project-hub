"""Contains mock data for the live demo of the projects feature."""

import pytest
from sqlalchemy.orm import Session
from ....models.project import Project
from ....entities.project_entity import ProjectEntity
from ..reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kaw Bu"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"

# --- Mock Project Data using Project model (NOT ProjectEntity) ---

project1 = Project(
    id=1,
    author_id=7,
    author="Alex Kim",
    image="https://www.creativefabrica.com/wp-content/uploads/2022/12/02/Mental-Health-Logo-with-Brain-and-Green-Graphics-49948798-1.jpg",
    title="MindMate: Student Mental Health Companion",
    short_description="A mobile app to support student mental health through journaling and mindfulness.",
    long_description=(
        "MindMate is a student-focused mental wellness app that encourages journaling, provides guided "
        "meditations, and integrates mental health resources from UNC. The goal is to support emotional well-being, "
        "reduce stigma, and provide an accessible support tool for students."
    ),
    requirements="- Experience with Swift or React Native\n- Interest in mental health advocacy\n- Bonus: UI/UX design experience",
    additional_info="Featured during UNC Mental Health Awareness Week.",
    email="alex.kim@example.com",
    phone_number="(555) 111-2222",
    linked_in="https://linkedin.com/in/alexkim",
    public=True,
    slug="mindmate-mental-health-companion",
)

project2 = Project(
    id=2,
    author_id=8,
    author="Riya Patel",
    image="https://r2.erweima.ai/i/1k9svko7T165wgUCZlM37Q.png",
    title="UNC Campus Navigator",
    short_description="Interactive map app to help students navigate UNC’s campus.",
    long_description=(
        "This app helps students find academic buildings, dining halls, and bus stops on campus. "
        "It integrates live bus tracking and includes AR wayfinding for on-foot navigation. The tool will be "
        "especially useful for new students during orientation."
    ),
    requirements="- Experience with mobile app development (Android or iOS)\n- Familiarity with GPS and mapping APIs\n- Bonus: ARKit or ARCore experience",
    additional_info="Collaborating with Carolina Housing for pilot testing.",
    email="riya.patel@example.com",
    phone_number="(555) 222-3333",
    linked_in="https://linkedin.com/in/riyapatel",
    public=True,
    slug="unc-campus-navigator",
)

project3 = Project(
    id=3,
    author_id=9,
    author="Jordan Smith",
    image="https://cdn2.iconfinder.com/data/icons/e-learning-17/96/timetable_classes_school_schedule-512.png",
    title="Class Sync Scheduler",
    short_description="A tool to help students find common free time for meetings and study sessions.",
    long_description=(
        "Class Sync is a web platform that aggregates students' class schedules and helps find overlapping "
        "free time slots. It's designed for study groups, club meetings, or collaborative work to coordinate easier."
    ),
    requirements="- Experience with Django or Node.js\n- Understanding of calendar APIs (Google Calendar, Outlook)\n- Bonus: Database design knowledge",
    additional_info="Selected for pilot in COMP 110 peer groups.",
    email="jordan.smith@example.com",
    phone_number="(555) 333-4444",
    linked_in="https://linkedin.com/in/jordansmith",
    public=True,
    slug="class-sync-scheduler",
)

project4 = Project(
    id=4,
    author_id=10,
    author="Emily Zhao",
    image="https://play-lh.googleusercontent.com/DRPxhc2e-kO79Yu0YvexKNwRyvpLY-AVw7_xz6UwVma4_lqWomJjxUbXeHplidWbYA",
    title="ZeroWaste: Campus Food Sharing Platform",
    short_description="Connects students to share extra food from events and dining plans.",
    long_description=(
        "ZeroWaste is a sustainability project aimed at reducing food waste on campus. The app lets students "
        "post surplus food from events or personal dining plans so others can claim it. It supports UNC’s Green "
        "Initiative and fosters community sharing."
    ),
    requirements="- Experience with Firebase or Supabase\n- Interest in sustainability and community impact\n- Bonus: UI design or community outreach experience",
    additional_info="In partnership with Carolina Dining Services.",
    email="emily.zhao@example.com",
    phone_number="(555) 444-5555",
    linked_in="https://linkedin.com/in/emilyzhao",
    public=True,
    slug="zerowaste-campus-food-sharing",
)

project5 = Project(
    id=5,
    author_id=11,
    author="Carlos Rivera",
    image="https://s3.amazonaws.com/file-management-customer-logo-prod-us-c0b832a/tenant_assests/4b0badb4-f992-455c-9187-dc7481401641/x1pmd_cst_logo_Career-Connect_Logos_C5V1_Full-color-(1).png",
    title="UNC Career Connect",
    short_description="A career resource hub for UNC students to explore internships and alumni mentors.",
    long_description=(
        "UNC Career Connect is a centralized platform that features internship postings, resume feedback tools, "
        "and a network of UNC alumni willing to offer mentorship. Students can search by major, industry, or company "
        "to discover relevant opportunities."
    ),
    requirements="- Experience with full-stack development (MERN stack preferred)\n- Familiarity with LinkedIn API or scraping tools\n- Bonus: Knowledge of career services or job boards",
    additional_info="Developed in collaboration with University Career Services.",
    email="carlos.rivera@example.com",
    phone_number="(555) 555-6666",
    linked_in="https://linkedin.com/in/carlosrivera",
    public=True,
    slug="unc-career-connect",
)

projects = [
    project1,
    project2,
    project3,
    project4,
    project5,
]

conflicting_id_project = Project(
    id=2,
    author_id=12,
    author="Sophia Lee",
    image="https://www.creativefabrica.com/wp-content/uploads/2022/12/02/Mental-Health-Logo-with-Brain-and-Green-Graphics-49948798-1.jpg",
    title="MindMate: Student Mental Health Companion",
    short_description="A mobile app to support student mental health through journaling and mindfulness.",
    long_description=(
        "MindMate is a student-focused mental wellness app that encourages journaling, provides guided "
        "meditations, and integrates mental health resources from UNC. The goal is to support emotional well-being, "
        "reduce stigma, and provide an accessible support tool for students."
    ),
    requirements="- Experience with Swift or React Native\n- Interest in mental health advocacy\n- Bonus: UI/UX design experience",
    additional_info="Featured during UNC Mental Health Awareness Week.",
    phone_number="1234567890",
    linked_in="https://linkedin.com/in/liamjohnson",
    public=True,
    slug="campus-fitness-tracker",
    email="joe@gmail.com",
)

to_add = Project(
    id=6,
    author_id=1,
    author="Rhonda Root",
    image="https://www.creativefabrica.com/wp-content/uploads/2022/12/02/Mental-Health-Logo-with-Brain-and-Green-Graphics-49948798-1.jpg",
    title="Campus Fitness Tracker",
    short_description="A fitness app to help students track workouts and nutrition.",
    long_description=(
        "Campus Fitness Tracker is a mobile app designed to help students monitor their fitness goals, "
        "track workouts, and log nutrition. It includes features like workout plans, meal tracking, and "
        "integration with fitness devices."
    ),
    requirements="- Experience with mobile app development (iOS or Android)\n- Familiarity with fitness APIs\n- Bonus: Nutrition knowledge",
    additional_info="In collaboration with Campus Recreation.",
    phone_number="1234567890",
    linked_in="https://linkedin.com/in/liamjohnson",
    public=True,
    slug="campus-fitness-tracker",
    email="joe@gmail.com",
)


def insert_fake_data(session: Session):
    """Inserts fake project data into the test session."""
    global projects

    entities = []
    for project in projects:
        entity = ProjectEntity.from_model(project)
        session.add(entity)
        entities.append(entity)

    reset_table_id_seq(session, ProjectEntity, ProjectEntity.id, len(projects) + 1)

    session.commit()


from sqlalchemy.orm import Session
from backend.entities.project_entity import ProjectEntity


def insert_project_data(session: Session):
    """Insert test projects into the database"""
    entities = [ProjectEntity.from_model(p) for p in projects]
    session.add_all(entities)
    reset_table_id_seq(session, ProjectEntity, ProjectEntity.id, len(projects) + 1)
    session.commit()


# Update the fixture to include projects
@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_project_data(session)  # Insert projects first
    insert_fake_data(session)  # Then insert job applications
    yield
    session.rollback()
