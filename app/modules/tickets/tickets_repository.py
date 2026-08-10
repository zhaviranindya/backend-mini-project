from datetime import date
from typing import Optional
from fastapi import Depends

from app.database import tickets_collection

def get_tickets_collection():
    return tickets_collection

class TicketsRepository:

    def __init__(self, collection = Depends(get_tickets_collection)):
        self.collection = collection

    async def get_tickets(self, search_title: str = None, status: str = None,
                          page: int = None, limit: int = 5):
        query = {}
        if search_title:
            query["title"] = search_title
        if status:
            query["status"] = status

        fields = {
            "ticket_id": 1,
            "title": 1,
            "priority": 1,
            "status": 1,
            "category": 1,
            "reported_by": 1,
            "created_at": 1
        }

        tickets_query = (
            self.collection.find(query, fields)
            .sort("created_at", -1)
        )

        if page is not None:
            skip = (page - 1) * limit
            pagination_result = tickets_query.skip(skip).limit(limit)
            tickets = await pagination_result.to_list()
        else: 
            tickets = await tickets_query.to_list()

        for ticket in tickets:
            ticket["id"] = str(ticket["_id"])
            del ticket["_id"]

        return tickets

    def get_ticket_by_id(self, ticket_id: str):
        for ticket in self.tickets_data["tickets"]:
            if ticket["ticket_id"] == ticket_id:
                return ticket
        return None

    def create_ticket(self, ticket_data: dict):
        new_ticket_id = len(self.tickets_data["tickets"]) + 1
        new_ticket = {
            "ticket_id": f"TCK-{new_ticket_id:03d}",
            "title": ticket_data["title"],
            "description": ticket_data["description"],
            "priority": ticket_data["priority"],
            "status": "Open",
            "category": ticket_data["category"],
            "reported_by": ticket_data["reported_by"],
            "created_at": date.today(),
        }
        self.tickets_data["tickets"].append(new_ticket)
        return new_ticket

    def update_ticket(self, ticket_id: str, ticket_data: dict):
        for ticket in self.tickets_data["tickets"]:
            if ticket["ticket_id"] == ticket_id:
                if ticket_data["title"] is not None:
                    ticket["title"] = ticket_data["title"]

                if ticket_data["description"] is not None:
                    ticket["description"] = ticket_data["description"]

                if ticket_data["priority"] is not None:
                    ticket["priority"] = ticket_data["priority"]

                if ticket_data["status"] is not None:
                    ticket["status"] = ticket_data["status"]

                if ticket_data["category"] is not None:
                    ticket["category"] = ticket_data["category"]

                return ticket
        return None

    def delete_ticket(self, ticket_id: str):
        for ticket in self.tickets_data["tickets"]:
            if ticket["ticket_id"] == ticket_id:
                self.tickets_data["tickets"].remove(ticket)
                return True
        return False
