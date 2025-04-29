from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "You are connected to the PostLand server!"