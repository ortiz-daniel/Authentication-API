from fastapi import FastAPI
from sqlmodel import SQLModel

from src.api.users import router as users_router
from src.api.auth import router as auth_router
from src.database.models import engine

app = FastAPI()
app.include_router(users_router)
app.include_router(auth_router)

@app.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
