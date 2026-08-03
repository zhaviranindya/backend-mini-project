from datetime import date
from typing import Optional

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


class TicketsUpdateRequest(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="Judul ticket (opsional)")
    description: Optional[str] = Field(None, min_length=1, description="Deskripsi ticket (opsional)")
    priority: Optional[str] = Field(None, min_length=1, description="Prioritas ticket (opsional)")
    status: Optional[str] = Field(None, min_length=1, description="Status ticket (opsional)")
    category: Optional[str] = Field(None, min_length=1, description="Kategori ticket (opsional)")