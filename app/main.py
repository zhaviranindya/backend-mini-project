import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import connect_database
from app.routes.tickets_route import router as tickets_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_database()
    yield


app = FastAPI(title="Backend FastAPI Mini Project", lifespan=lifespan)


app.include_router(tickets_router)
