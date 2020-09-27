from fastapi import APIRouter, HTTPException
from models.prediction import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
def health():
    try:
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
