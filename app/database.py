import logging
import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

HELPDESK_DB_URI = os.getenv("HELPDESK_DB_URI")
HELPDESK_DB_NAME = os.getenv("HELPDESK_DB_NAME")

client = AsyncIOMotorClient(HELPDESK_DB_URI)
db = client[HELPDESK_DB_NAME]

logger = logging.getLogger(__name__)


async def connect_database():
    try:
        await db.command("ping")
        logger.info("MongoDB Connected success")
    except Exception:
        logger.exception("MongoDB Connection failed")
        raise
