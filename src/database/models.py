import datetime

from sqlmodel import Field, Relationship, SQLModel, create_engine

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(max_length=64, unique=True)
    password: str = Field(max_length=64)
    is_active: bool = Field(default=True)
    
    login_sessions: list["LoginSessions"] = Relationship(back_populates="user")
    

class LoginSessions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    success: bool = Field(default=True)
    date: str | None = Field(max_length=64, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="login_sessions")

url: str = "sqlite:///database.db"
engine = create_engine(url=url, echo=True)
