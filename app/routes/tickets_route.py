from typing import Optional

from fastapi import APIRouter, HTTPException, Depends

from app.modules.tickets.tickets_schema import TicketsCreateRequest, TicketsResponse
from app.modules.tickets.tickets_schema import TicketsUpdateRequest, TicketsListResponse
from app.modules.tickets.tickets_service import TicketsService

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_service(service: TicketsService = Depends()):
    return service

@router.get("", response_model=list[TicketsListResponse])
async def get_tickets(search_title: Optional[str] = None, status: Optional[str] = None, 
                      page: int = None, limit: int = 5,
                      service: TicketsService = Depends(get_service)):
    return await service.get_tickets(search_title, status, page, limit)


@router.get("/{id}", response_model=TicketsResponse)
async def get_ticket_by_id(id: str, 
                           service: TicketsService = Depends(get_service)):
    ticket = await service.get_ticket_by_id(id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return ticket


@router.post("", response_model=TicketsResponse, status_code=201)
async def create_ticket(ticket: TicketsCreateRequest, 
                        service: TicketsService = Depends(get_service)):
    new_ticket = await service.create_ticket(ticket.model_dump())
    return new_ticket

@router.patch("/{ticket_id}", response_model=TicketsResponse)
async def update_ticket(ticket_id: str, ticket: TicketsUpdateRequest, 
                        service: TicketsService = Depends(get_service)):
    updated_ticket = await service.update_ticket(ticket_id, ticket.model_dump())

    if update_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return updated_ticket

@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: str, service: TicketsService = Depends(get_service)):
    deleted_ticket = await service.delete_ticket(ticket_id)

    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket tidak ditemukan!")
    return {"message": f"Ticket dengan ID {ticket_id} berhasil dihapus"}
