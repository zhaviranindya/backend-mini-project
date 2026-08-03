from typing import Optional

from app.modules.tickets.tickets_repository import TicketsRepository


class TicketsService:
    def __init__(self):
        self.repository = TicketsRepository()

    async def get_tickets(self):
        return self.repository.get_tickets()

    async def get_ticket_by_id(self, ticket_id: str):
        return self.repository.get_ticket_by_id(ticket_id)

    async def search_tickets(self, status: Optional[str] = None):
        return self.repository.search_tickets(status)

    async def create_ticket(self, ticket_data: dict):
        return self.repository.create_ticket(ticket_data)

    async def update_ticket(self, ticket_id: str, ticket_data: dict):
        return self.repository.update_ticket(ticket_id, ticket_data)

    async def delete_ticket(self, ticket_id: str):
        return self.repository.delete_ticket(ticket_id)
