from src.database.models import User, engine

from sqlmodel import Session

def insert_user(user: dict) -> User:
    user = User(**user)

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user
