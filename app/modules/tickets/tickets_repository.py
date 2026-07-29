from datetime import date
from typing import Optional


class TicketsRepository:
    tickets_data = {
        "tickets": [
            {
                "ticket_id": "TCK-001",
                "title": "Tidak bisa login",
                "description": "User tidak dapat login ke aplikasi.",
                "priority": "High",
                "status": "Open",
                "category": "Software",
                "reported_by": "Billal Syaidan",
                "created_at": "2026-07-20",
            },
            {
                "ticket_id": "TCK-002",
                "title": "Printer rusak",
                "description": "Printer tidak mengeluarkan hasil cetak.",
                "priority": "Medium",
                "status": "In Progress",
                "category": "Hardware",
                "reported_by": "Anindya Kayla",
                "created_at": "2026-07-21",
            },
            {
                "ticket_id": "TCK-003",
                "title": "Permintaan reset password",
                "description": "User lupa password dan meminta untuk di reset",
                "priority": "Medium",
                "status": "Open",
                "category": "Account & Access",
                "reported_by": "Janari Yoga Swara",
                "created_at": "2026-07-22",
            },
            {
                "ticket_id": "TCK-004",
                "title": "Tidak bisa cetak dokumen",
                "description": "Printer tidak merespon perintah print dari komputer, padahal ketika di cek kabel sudah tersambung",
                "priority": "Medium",
                "status": "Open",
                "category": "Hardware",
                "reported_by": "Amira Putri",
                "created_at": "2026-07-23",
            },
            {
                "ticket_id": "TCK-005",
                "title": "AC ruangan lantai 1 tidak dingin",
                "description": "Ruangan lantai 1 jadi terasa panas karena AC kurang dingin",
                "priority": "Medium",
                "status": "Closed",
                "category": "Facility",
                "reported_by": "Nabil Arkananta",
                "created_at": "2026-07-24",
            },
            {
                "ticket_id": "TCK-006",
                "title": "Lampu ruang rapat mati",
                "description": "Dua buah bohlam lampu di ruang rapat mati dan perlu segera diganti sebelum meeting sore",
                "priority": "Low",
                "status": "Open",
                "category": "Facility",
                "reported_by": "Dimas Nugraha",
                "created_at": "2026-07-29",
            },
        ]
    }

    def get_tickets(self):
        return self.tickets_data

    def get_ticket_by_id(self, ticket_id: str):
        for ticket in self.tickets_data["tickets"]:
            if ticket["ticket_id"] == ticket_id:
                return ticket
        return None

    def search_tickets(self, status: Optional[str] = None):
        result = self.tickets_data["tickets"]

        if status:
            result = [ticket for ticket in result if ticket["status"] == status]

        return result

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
