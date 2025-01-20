from fastapi import FastAPI

from src.api.users import router as users_router
from sqlmodel import SQLModel

app = FastAPI()
app.include_router(users_router)

@app.get('/')
async def main():
    return {"message": "Hello World"}
