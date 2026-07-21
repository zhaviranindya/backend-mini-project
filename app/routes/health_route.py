from fastapi import APIRouter
from app.modules.health.health_service import HealthService
router=APIRouter()
@router.get("/health")
async def health():
    return await HealthService().health()
