from datetime import datetime

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

        fields = {"ticket_code": 1, "title": 1, "priority": 1, "status": 1, "category": 1, "reporter_name": 1, "created_at": 1}

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

        fields = {"ticket_code": 1, "title": 1, "description": 1, "priority": 1, "status": 1, "category": 1, "reporter_name": 1, "created_at": 1, "updated_at": 1}

        ticket = await self.collection.find_one({"_id": ObjectId(id)}, fields)

        if ticket is None:
            return None

        ticket["id"] = str(ticket["_id"])
        del ticket["_id"]
        return ticket

    async def create_ticket(self, ticket_data: dict):
        total_ticket = await self.collection.count_documents({})
        new_ticket_code = f"TCK-{total_ticket + 1:03d}"
        new_ticket = {"ticket_code": new_ticket_code, "title": ticket_data["title"], "description": ticket_data["description"], "priority": ticket_data["priority"], "status": TicketStatus.Open, "category": ticket_data["category"], "reporter_name": ticket_data["reported_by"], "created_at": datetime.now()}
        tickets = await self.collection.insert_one(new_ticket)

        new_ticket["id"] = str(tickets.inserted_id)
        del new_ticket["_id"]

        return new_ticket

    async def update_ticket(self, id: str, ticket_data: dict):
        if not ObjectId.is_valid(id):
            return None

        update_fields = {}

        if ticket_data["title"] is not None:
            update_fields["title"] = ticket_data["title"]

        if ticket_data["description"] is not None:
            update_fields["description"] = ticket_data["description"]

        if ticket_data["priority"] is not None:
            update_fields["priority"] = ticket_data["priority"]

        if ticket_data["category"] is not None:
            update_fields["category"] = ticket_data["category"]

        update_fields["updated_at"] = datetime.now()

        tickets = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_fields})

        if tickets.matched_count == 0:
            return None

        return await self.get_ticket_by_id(id)

    async def delete_ticket(self, id: str):
        if not ObjectId.is_valid(id):
            return None

        tickets = await self.collection.delete_one({"_id": ObjectId(id)})

        return tickets.deleted_count > 0
