from fastapi import APIRouter

from api.routes import health
from api.routes import menu

router = APIRouter()
router.include_router(health.router, tags=["Health"], prefix="/v1")
router.include_router(menu.router, tags=["Menu"], prefix="/v1")