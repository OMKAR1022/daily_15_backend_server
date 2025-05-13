from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

# Create FastAPI app
app = FastAPI(
    title="Daily 15 API",
    description="Backend API for Daily 15 Flutter Application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Flutter app's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Daily 15 API"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}