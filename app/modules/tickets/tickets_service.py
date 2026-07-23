from app.modules.tickets.tickets_repository import TicketsRepository
class TicketsService:
    async def get_all_tickets(self):
        return TicketsRepository().get_all_tickets()
