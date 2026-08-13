from fastapi import Depends

from app.modules.tickets.tickets_repository import TicketsRepository
from app.modules.tickets.tickets_service import TicketsService


def get_tickets_repository() -> TicketsRepository:
    return TicketsRepository()


def get_tickets_service(tickets_repository: TicketsRepository = Depends(get_tickets_repository)) -> TicketsService:
    return TicketsService(tickets_repository)
