from fastapi import APIRouter
from app.modules.tickets.tickets_service import TicketsService

router = APIRouter()


@router.get("/tickets")
async def tickets():
    return await TicketsService().get_all_tickets()
