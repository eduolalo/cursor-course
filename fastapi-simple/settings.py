"""
Application settings.
"""
from typing import List


class Settings:
    """Application settings."""
    
    # Basic app info
    PROJECT_NAME: str = "FastAPI Simple Project"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A simple FastAPI project"
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["*"]


settings = Settings()
