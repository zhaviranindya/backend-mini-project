from app.modules.tickets.tickets_repository import TicketsRepository
from typing import Optional


class TicketsService:
    async def get_tickets(self):
        return TicketsRepository().get_tickets()

    async def get_ticket_by_id(self, ticket_id: str):
        return TicketsRepository().get_ticket_by_id(ticket_id)

    async def search_tickets(self, status: Optional[str] = None):
        return TicketsRepository().search_tickets(status)
