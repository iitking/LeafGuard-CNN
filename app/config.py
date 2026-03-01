import os
from pathlib import Path
from pydantic_settings import BaseSettings

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"

class Settings(BaseSettings):
    APP_NAME: str = "LeafGuard AI - Plant Disease Detection"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    
    # Host & Port
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Model configuration
    MODEL_PATH: Path = BASE_DIR / "LeafGuard-CNN_model.pkl"
    CLASS_INDICES_PATH: Path = BASE_DIR / "class_indices.json"
    
    # Image preprocessing
    IMG_HEIGHT: int = 224
    IMG_WIDTH: int = 224
    MAX_UPLOAD_SIZE_MB: int = 15
    
    # Allowed image MIME types
    ALLOWED_EXTENSIONS: set = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
