"""
Core configuration settings for the FastAPI application.

TODO:
- Add environment variable loading (python-dotenv or pydantic-settings)
- Define database connection settings
- Add API versioning configuration
- Configure logging settings
- Add security settings (API keys, JWT secrets, etc.)
"""

from typing import Optional


class Settings:
    """Application settings."""

    # TODO: Load from environment variables
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Trading Platform API"
    VERSION: str = "0.1.0"

    # Database settings
    # TODO: Configure database connection string from environment
    DATABASE_URL: Optional[str] = None

    # CORS settings
    # TODO: Move to environment variables
    CORS_ORIGINS: list[str] = ["*"]  # In production, specify actual origins


# TODO: Create singleton instance
settings = Settings()
