from fastapi import FastAPI

from src.api.users import router as users_router
from sqlmodel import SQLModel
from src.database.models import engine

app = FastAPI()
app.include_router(users_router)

@app.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)

@app.get('/')
async def main():
    return {"message": "Hello World"}
