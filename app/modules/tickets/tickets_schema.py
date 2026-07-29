from datetime import date

from pydantic import BaseModel, Field


class TicketsResponse(BaseModel):
    ticket_id: str
    title: str
    description: str
    priority: str
    status: str
    category: str
    reported_by: str
    created_at: date


class TicketsCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, description="Judul ticket wajib diisi")
    description: str = Field(..., min_length=1, description="Deskripsi ticket wajib diisi")
    priority: str = Field(..., min_length=1, description="Prioritas ticket wajib diisi")
    category: str = Field(..., min_length=1, description="Kategori ticket wajib diisi")
    reported_by: str = Field(..., min_length=1, description="Nama Pelapor ticket wajib diisi")
