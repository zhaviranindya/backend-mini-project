from fastapi import FastAPI

from app.database import db
from app.routes.tickets_route import router as tickets_router

app = FastAPI(title="Backend FastAPI Mini Project")

@app.on_event("startup")
async def connect_db():
    await db.command("ping")
    print("MongoDB Connected")


app.include_router(tickets_router)
