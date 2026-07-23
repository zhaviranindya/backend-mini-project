class TicketsRepository:
    def get_all_tickets(self):
        return {
            "tickets": [
                {
                    "ticket_id": "TCK-001",
                    "title": "Tidak bisa login",
                    "description": "User tidak dapat login ke aplikasi.",
                    "priority": "High",
                    "status": "Open",
                },
                {
                    "ticket_id": "TCK-002",
                    "title": "Printer rusak",
                    "description": "Printer tidak mengeluarkan hasil cetak.",
                    "priority": "Medium",
                    "status": "In Progress",
                },
                {
                    "ticket_id": "TCK-003",
                    "title": "Permintaan reset password",
                    "description": "User lupa password dan meminta untuk di reset",
                    "priority": "Medium",
                    "status": "Open",
                },
                {
                    "ticket_id": "TCK-004",
                    "title": "Tidak bisa cetak dokumen",
                    "description": "Printer tidak merespon perintah print dari komputer, padahal ketika di cek kabel sudah tersambung",
                    "priority": "Medium",
                    "status": "Open",
                },
                {
                    "ticket_id": "TCK-005",
                    "title": "AC ruangan lantai 1 tidak dingin",
                    "description": "Ruangan lantai 1 jadi terasa panas karena AC kurang dingin",
                    "priority": "Medium",
                    "status": "Closed",
                },
            ]
        }
