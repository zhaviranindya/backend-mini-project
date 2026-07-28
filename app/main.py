from fastapi import FastAPI
from app.routes.health_route import router as health_router
from app.routes.tickets_route import router as tickets_router

app = FastAPI(title="Backend FastAPI Template")
app.include_router(health_router)
app.include_router(tickets_router)
