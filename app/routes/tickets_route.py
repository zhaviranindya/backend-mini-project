from fastapi import APIRouter, HTTPException
from app.modules.tickets.tickets_service import TicketsService
from app.modules.tickets.tickets_schema import TicketsResponse

router = APIRouter()


@router.get("/tickets", response_model=list[TicketsResponse])
async def get_tickets():
    result = await TicketsService().get_tickets()
    return result["tickets"]


@router.get("/tickets/{ticket_id}", response_model=TicketsResponse)
async def get_detail_tickets(ticket_id: str):
    ticket = await TicketsService().get_ticket_by_id(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return ticket
