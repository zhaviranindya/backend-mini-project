from pydantic import BaseModel


class TicketsResponse(BaseModel):
    ticket_id: str
    title: str
    description: str
    priority: str
    status: str
