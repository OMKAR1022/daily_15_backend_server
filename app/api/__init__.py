from fastapi import APIRouter
from app.api.v1.endpoints import users

# Create the main API router
router = APIRouter()

# Include the v1 API router
v1_router = APIRouter()
v1_router.include_router(users.router, prefix="/users", tags=["users"])

# Include v1 router in main router
router.include_router(v1_router, prefix="/v1")
