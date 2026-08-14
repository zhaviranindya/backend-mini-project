from app.modules.tickets.tickets_repository import TicketsRepository
from app.modules.tickets.tickets_schema import TicketStatus


class TicketsService:
    def __init__(self, tickets_repository: TicketsRepository):
        self.tickets_repository = tickets_repository

    async def get_tickets(self, search_title: str = None, status: TicketStatus = None, page: int = 1, limit: int = 5):

        return await self.tickets_repository.get_tickets(search_title, status, page, limit)

    async def get_ticket_by_id(self, id: str):
        return await self.tickets_repository.get_ticket_by_id(id)

    async def create_ticket(self, ticket_data: dict):
        return await self.tickets_repository.create_ticket(ticket_data)

    async def update_ticket(self, ticket_id: str, ticket_data: dict):
        return self.repository.update_ticket(ticket_id, ticket_data)

    async def delete_ticket(self, ticket_id: str):
        return self.repository.delete_ticket(ticket_id)
