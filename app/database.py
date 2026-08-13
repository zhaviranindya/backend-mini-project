import logging
import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

logger = logging.getLogger(__name__)


async def connect_database():
    try:
        await db.command("ping")
        logger.info("MongoDB Connected success")
    except Exception:
        logger.exception("MongoDB Connection failed")
        raise
