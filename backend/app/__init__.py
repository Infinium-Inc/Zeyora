from . import models
from .database import engine
from .routers import users

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow only zeyora.in and localhost (commonly used with React/Vite dev server)
origins = [
    "https://zeyora.in",
    "http://localhost:3000",  # Common port for React dev server
    "http://127.0.0.1:3000",  # Alternative localhost IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)

@app.get("/")
async def root():
    return "You are connected to the Zeyora backend API!"

# Create DB tables
models.Base.metadata.create_all(bind=engine)
