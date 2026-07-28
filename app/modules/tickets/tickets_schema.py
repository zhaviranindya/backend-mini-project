from pydantic import BaseModel
from datetime import date


class TicketsResponse(BaseModel):
    ticket_id: str
    title: str
    description: str
    priority: str
    status: str
    category: str
    reported_by: str
    created_at: date
