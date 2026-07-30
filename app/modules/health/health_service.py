from app.modules.health.health_repository import HealthRepository


class HealthService:
    async def health(self):
        return HealthRepository().get_health()
