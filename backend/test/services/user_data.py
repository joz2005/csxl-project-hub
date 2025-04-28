"""Mock data for users.

Three users are setup for testing and development purposes:

1. Rhonda Root (root user with all permissions)
2. Amy Ambassador (staff of XL with elevated permissions)
3. Sally Student (standard user without any special permissions)
4. Ina Instructor
5. Uhlissa UTA
6. Stewie Student
7. Alex Kim (project author)
8. Riya Patel (project author)
9. Jordan Smith (project author)
10. Emily Zhao (project author)
11. Carlos Rivera (project author)
"""

import pytest
from sqlalchemy.orm import Session
from ...models.user import User
from ...entities.user_entity import UserEntity
from ...entities.user_role_table import user_role_table
from .reset_table_id_seq import reset_table_id_seq
from . import role_data

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

# Original Users
root = User(
    id=1,
    pid=999999999,
    onyen="root",
    email="root@unc.edu",
    first_name="Rhonda",
    last_name="Root",
    pronouns="She / Her / Hers",
    accepted_community_agreement=True,
)

ambassador = User(
    id=2,
    pid=888888888,
    onyen="xlstan",
    email="amam@unc.edu",
    first_name="Amy",
    last_name="Ambassador",
    pronouns="They / Them / Theirs",
    accepted_community_agreement=True,
)

user = User(
    id=3,
    pid=111111111,
    onyen="user",
    email="user@unc.edu",
    first_name="Sally",
    last_name="Student",
    pronouns="She / They",
    accepted_community_agreement=True,
)

instructor = User(
    id=4,
    pid=222222222,
    onyen="ina",
    email="ina@unc.edu",
    first_name="Ina",
    last_name="Instructor",
    pronouns="They / Them / Theirs",
)

uta = User(
    id=5,
    pid=333333333,
    onyen="uhlissa",
    email="uhlissa@unc.edu",
    first_name="Uhlissa",
    last_name="UTA",
    pronouns="They / Them / Theirs",
)

student = User(
    id=6,
    pid=555555555,
    onyen="stewie",
    email="stewie@unc.edu",
    first_name="Stewie",
    last_name="Student",
    pronouns="They / Them / Theirs",
)

# NEW users for Project authors
alex_kim = User(
    id=7,
    pid=666666666,
    onyen="alexkim",
    email="alex.kim@example.com",
    first_name="Alex",
    last_name="Kim",
    pronouns="He / Him / His",
)

riya_patel = User(
    id=8,
    pid=777777777,
    onyen="riyapatel",
    email="riya.patel@example.com",
    first_name="Riya",
    last_name="Patel",
    pronouns="She / Her / Hers",
)

jordan_smith = User(
    id=9,
    pid=888777666,
    onyen="jordansmith",
    email="jordan.smith@example.com",
    first_name="Jordan",
    last_name="Smith",
    pronouns="He / Him / His",
)

emily_zhao = User(
    id=10,
    pid=555444333,
    onyen="emilyzhao",
    email="emily.zhao@example.com",
    first_name="Emily",
    last_name="Zhao",
    pronouns="She / Her / Hers",
)

carlos_rivera = User(
    id=11,
    pid=444333222,
    onyen="carlosrivera",
    email="carlos.rivera@example.com",
    first_name="Carlos",
    last_name="Rivera",
    pronouns="He / Him / His",
)

# Update users list
users = [
    root,
    ambassador,
    user,
    instructor,
    uta,
    student,
    alex_kim,
    riya_patel,
    jordan_smith,
    emily_zhao,
    carlos_rivera,
]

# Role assignments (only original ones for now)
roles_users = {
    role_data.root_role.id: [root],
    role_data.ambassador_role.id: [ambassador],
}


def insert_fake_data(session: Session):
    global users
    entities = []
    for user in users:
        entity = UserEntity.from_model(user)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(session, UserEntity, UserEntity.id, len(users) + 1)
    session.commit()  # Commit to ensure User IDs are saved properly

    # Associate Users with the Role(s) they are in
    for role_id, members in roles_users.items():
        for user in members:
            session.execute(
                user_role_table.insert().values(
                    {"role_id": role_id, "user_id": user.id}
                )
            )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
