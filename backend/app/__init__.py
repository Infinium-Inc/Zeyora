from . import models
from .database import engine

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "You are connected to the Zeyora backend API!"

models.Base.metadata.create_all(bind=engine)