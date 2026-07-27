from app.modules.tickets.tickets_repository import TicketsRepository


class TicketsService:
    async def get_tickets(self):
        return TicketsRepository().get_tickets()

    async def get_ticket_by_id(self, ticket_id: str):
        return TicketsRepository().get_ticket_by_id(ticket_id)
