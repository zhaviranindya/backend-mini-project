from datetime import date

from bson import ObjectId

from app.database import db
from app.modules.tickets.tickets_schema import TicketStatus


class TicketsRepository:
    def __init__(self):
        self.collection = db.get_collection("tickets")

    async def get_tickets(self, search_title: str = None, status: TicketStatus = None, page: int = 1, limit: int = 5):
        query = {}
        if search_title:
            query["title"] = {"$regex": search_title, "$options": "i"}
        if status:
            query["status"] = status

        fields = {"ticket_code": 1, "title": 1, "priority": 1, "status": 1, "category": 1, "reported_name": 1, "created_at": 1}

        skip = (page - 1) * limit

        result = self.collection.find(query, fields).sort("created_at", -1).skip(skip).limit(limit)

        tickets = await result.to_list()

        for ticket in tickets:
            ticket["id"] = str(ticket["_id"])
            del ticket["_id"]

        return tickets

    async def get_ticket_by_id(self, id: str):
        if not ObjectId.is_valid(id):
            return None

        fields = {"ticket_code": 1, "title": 1, "description": 1, "priority": 1, "status": 1, "category": 1, "reported_name": 1, "created_at": 1}

        ticket = await self.collection.find_one({"_id": ObjectId(id)}, fields)

        if ticket is None:
            return None

        ticket["id"] = str(ticket["_id"])
        del ticket["_id"]
        return ticket

    def create_ticket(self, ticket_data: dict):
        new_ticket_id = len(self.tickets_data["tickets"]) + 1
        new_ticket = {
            "ticket_id": f"TCK-{new_ticket_id:03d}",
            "title": ticket_data["title"],
            "description": ticket_data["description"],
            "priority": ticket_data["priority"],
            "status": "Open",
            "category": ticket_data["category"],
            "reported_name": ticket_data["reported_name"],
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
