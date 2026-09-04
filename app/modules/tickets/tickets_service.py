from app.modules.tickets.tickets_repository import TicketsRepository
from app.modules.tickets.tickets_schema import TicketsCreateRequest, TicketStatus, TicketsUpdateRequest


class TicketsService:
    def __init__(self, tickets_repository: TicketsRepository):
        self.tickets_repository = tickets_repository

    async def get_tickets(self, search_title: str = None, status: TicketStatus = None, page: int = 1, limit: int = 5):

        if page < 1 and limit < 1:
            raise ValueError("page dan limit harus lebih besar atau sama dengan 1")

        return await self.tickets_repository.get_tickets(search_title, status, page, limit)

    async def get_ticket_by_id(self, ticket_id: str):
        return await self.tickets_repository.get_ticket_by_id(ticket_id)

    async def create_ticket(self, ticket_data: TicketsCreateRequest):
        total_ticket = await self.tickets_repository.count_tickets()
        new_ticket_code = f"TCK-{total_ticket + 1:03d}"

        return await self.tickets_repository.create_ticket(ticket_data, new_ticket_code)

    async def update_ticket(self, ticket_id: str, ticket_data: TicketsUpdateRequest):
        return await self.tickets_repository.update_ticket(ticket_id, ticket_data)

    async def delete_ticket(self, ticket_id: str):
        return await self.tickets_repository.delete_ticket(ticket_id)
