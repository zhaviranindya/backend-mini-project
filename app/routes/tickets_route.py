from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.modules.tickets.tickets_depedency import get_tickets_service
from app.modules.tickets.tickets_schema import (
    TicketsCreateRequest,
    TicketsListResponse,
    TicketsResponse,
    TicketStatus,
    TicketsUpdateRequest,
)
from app.modules.tickets.tickets_service import TicketsService

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("", response_model=list[TicketsListResponse])
async def get_tickets(
    search_title: Optional[str] = None,
    status: Optional[TicketStatus] = None,
    page: int = 1,
    limit: int = 5,
    tickets_service: TicketsService = Depends(get_tickets_service),
):
    return await tickets_service.get_tickets(search_title, status, page, limit)


@router.get("/{id}", response_model=TicketsResponse)
async def get_ticket_by_id(id: str, service: TicketsService = Depends(get_tickets_service)):
    ticket = await service.get_ticket_by_id(id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return ticket


@router.post("", response_model=TicketsListResponse, status_code=201)
async def create_ticket(ticket: TicketsCreateRequest, tickets_service: TicketsService = Depends(get_tickets_service)):
    new_ticket = await tickets_service.create_ticket(ticket.model_dump())
    return new_ticket


@router.patch("/{ticket_id}", response_model=TicketsListResponse)
async def update_ticket(
    ticket_id: str,
    ticket: TicketsUpdateRequest,
    tickets_service: TicketsService = Depends(get_tickets_service),
):
    updated_ticket = await tickets_service.update_ticket(ticket_id, ticket.model_dump())

    if update_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return updated_ticket


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: str, tickets_service: TicketsService = Depends(get_tickets_service)):
    deleted_ticket = await tickets_service.delete_ticket(ticket_id)

    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return {"message": f"Ticket dengan ID {ticket_id} berhasil dihapus"}
