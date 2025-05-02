from .routers import users

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "You are connected to the Zeyora backend API!"