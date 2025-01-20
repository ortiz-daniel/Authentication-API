from src.database.models import User, engine

from sqlmodel import Session

def insert_user(user: dict) -> User:
    user = User(**user)

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user

def get_user_by_email(email: str) -> User:
    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
    return user
