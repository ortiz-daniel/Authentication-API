from fastapi import FastAPI

from src.api.users import router as users_router
from src.api.auth import router as auth_router
from sqlmodel import SQLModel
from src.database.models import engine

app = FastAPI()
app.include_router(users_router)
app.include_router(auth_router)

@app.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)

@app.get('/')
async def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
