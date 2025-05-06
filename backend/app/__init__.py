from . import models
from .database import engine
from .routers import users

from fastapi import FastAPI

app = FastAPI()
app.include_router(users.router)

@app.get("/")
async def root():
    return "You are connected to the Zeyora backend API!"

models.Base.metadata.create_all(bind=engine)