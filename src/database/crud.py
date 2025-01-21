from typing import List

from sqlmodel import Session

from src.database.models import User, engine, LoginSessions

def insert_user(user: dict) -> User:
    """
    Args:
        user (dict): Recibe un diccionario con los datos del usuario a crear.

    Returns:
        User: Devuelve el usuario creado en la base de datos.
    """
    user = User(**user)

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user

def get_user_by_email(email: str) -> User:
    """
    Args:
        email (str): Recibe el email del usuario a buscar.

    Returns:
        User: Devuelve el usuario encontrado en la base de datos, si no lo encuentra devuelve None.
    """
    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
    return user

def get_logins_by_user(email: str) -> List[LoginSessions]:
    """
    Args:
        email (str): Email del usuario a buscar.

    Returns:
        List[LoginSessions]: Devuelve una lista con las sesiones de login del usuario.
    """

    user = get_user_by_email(email)

    with Session(engine) as session:
        logins: List[LoginSessions] = session.query(LoginSessions).filter(LoginSessions.user_id == user.id).all()
    
    data = list(map(lambda x: x.dict(), logins))
    
    return data


def insert_login_session(email: str, success: bool) -> LoginSessions:
    """
    Args:
        user_email (str): Email del usuario.
        success (bool): Indica si el login fue exitoso o no.

    Returns:
        LoginSessions: Devuelve la sesión de login creada en la base de datos.
    """

    user = get_user_by_email(email)

    login = LoginSessions(user=user, success=success)

    with Session(engine) as session:
        session.add(login)
        session.commit()
        session.refresh(login)

    return login
