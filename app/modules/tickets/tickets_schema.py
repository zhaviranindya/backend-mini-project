from datetime import date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field

class TicketStatus(str, Enum):
    Open = "Open"
    In_Progress = "In_Progress"
    Resolved = "Resolved"
    Closed = "Closed"

class TicketPriority(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class TicketsResponse(BaseModel):
    id : str 
    ticket_id: str
    title: str
    priority: TicketPriority
    status: TicketStatus
    category: str
    reported_by: str
    created_at: date


class TicketsCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, description="Judul ticket wajib diisi")
    description: str = Field(..., min_length=1, description="Deskripsi ticket wajib " \
    "diisi")
    priority: str = Field(..., min_length=1, description="Prioritas ticket wajib diisi")
    category: str = Field(..., min_length=1, description="Kategori ticket wajib diisi")
    reported_by: str = Field(..., min_length=1, description="Nama Pelapor ticket wajib " \
    "diisi")


class TicketsUpdateRequest(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="Judul ticket "
    "(opsional)")
    description: Optional[str] = Field(None, min_length=1, description="Deskripsi ticket"
    " (opsional)")
    priority: Optional[str] = Field(None, min_length=1, description="Prioritas ticket"
    " (opsional)")
    status: Optional[str] = Field(None, min_length=1, description="Status ticket"
    " (opsional)")
    category: Optional[str] = Field(None, min_length=1, description="Kategori ticket"
    " (opsional)")