class TicketsRepository:
    def get_tickets(self):
        return {
            "tickets": [
                {
                    "ticket_id": "TCK-001",
                    "title": "Tidak bisa login",
                    "description": "User tidak dapat login ke aplikasi.",
                    "priority": "High",
                    "status": "Open",
                    "category": "Software",
                    "reported_by": "Billal Syaidan",
                    "created_at": "2026-07-20"
                },
                {
                    "ticket_id": "TCK-002",
                    "title": "Printer rusak",
                    "description": "Printer tidak mengeluarkan hasil cetak.",
                    "priority": "Medium",
                    "status": "In Progress",
                    "category": "Hardware",
                    "reported_by": "Anindya Kayla",
                    "created_at": "2026-07-21"
                },
                {
                    "ticket_id": "TCK-003",
                    "title": "Permintaan reset password",
                    "description": "User lupa password dan meminta untuk di reset",
                    "priority": "Medium",
                    "status": "Open",
                    "category": "Account & Access",
                    "reported_by": "Janari Yoga Swara",
                    "created_at": "2026-07-22"
                },
                {
                    "ticket_id": "TCK-004",
                    "title": "Tidak bisa cetak dokumen",
                    "description": "Printer tidak merespon perintah print dari komputer, padahal ketika di cek kabel sudah tersambung",
                    "priority": "Medium",
                    "status": "Open",
                    "category": "Hardware",
                    "reported_by": "Amira Putri",
                    "created_at": "2026-07-23"
                },
                {
                    "ticket_id": "TCK-005",
                    "title": "AC ruangan lantai 1 tidak dingin",
                    "description": "Ruangan lantai 1 jadi terasa panas karena AC kurang dingin",
                    "priority": "Medium",
                    "status": "Closed",
                    "category": "Facility",
                    "reported_by": "Nabil Arkananta",
                    "created_at": "2026-07-24"
                },
            ]
        }

    def get_ticket_by_id(self, ticket_id: str):
        data=self.get_tickets()
        for tickets in data["tickets"]:
            if tickets["ticket_id"] == ticket_id:
                return tickets
        return None    
