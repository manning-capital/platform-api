"""
Main FastAPI application entry point.

TODO:
- Import core configuration
  - from .core.config import settings

- Import API routers
  - from .api.v1 import api_router

- Update FastAPI app initialization
  - Use settings.PROJECT_NAME, settings.VERSION
  - Add API prefix from settings.API_V1_PREFIX

- Include API routers
  - app.include_router(api_router, prefix=settings.API_V1_PREFIX)

- Update CORS configuration
  - Use settings.CORS_ORIGINS instead of hardcoded ["*"]

- Add startup/shutdown events (optional)
  - Database connection initialization
  - Health check endpoints
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# TODO: Import configuration
# from .core.config import settings

# TODO: Import API routers
# from .api.v1 import api_router

app = FastAPI(
    title="Trading Platform API",
    description="FastAPI backend for the trading platform",
    version="0.1.0",
    # TODO: Use settings
    # title=settings.PROJECT_NAME,
    # version=settings.VERSION,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Use settings.CORS_ORIGINS
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: Include API routers
# app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
def read_root():
    return {"message": "Trading Platform API", "version": "0.1.0"}


# TODO: Add health check endpoint
# @app.get("/health")
# def health_check():
#     """Health check endpoint."""
#     return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)