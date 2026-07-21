from fastapi import FastAPI
from app.routes.health_route import router as health_router
app=FastAPI(title="Backend FastAPI Template")
app.include_router(health_router)
