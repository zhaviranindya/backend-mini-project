from fastapi import FastAPI

from app.routes.tickets_route import router as tickets_router

app = FastAPI(title="Backend FastAPI Mini Project")
app.include_router(tickets_router)
