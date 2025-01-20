from sqlmodel import Field, SQLModel, create_engine

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(max_length=64, unique=True)
    password: str = Field(max_length=64)
    is_active: bool = Field(default=True)


url: str = "sqlite:///database.db"
engine = create_engine(url=url, echo=True)
