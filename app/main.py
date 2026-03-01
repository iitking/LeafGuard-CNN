"""
LeafGuard AI - Plant Disease Detection System
FastAPI Application Entrypoint
"""

import os
from pathlib import Path
from typing import Dict, Any, List

from fastapi import FastAPI, File, UploadFile, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import settings, APP_DIR, BASE_DIR
from app.disease_data import DISEASE_KNOWLEDGE_BASE, get_disease_details
from app.model_service import model_service

# Initialize FastAPI App
app = FastAPI(
    title=settings.APP_NAME,
    description="Automated Plant Disease Diagnosis & Remedy Recommendations using Deep Convolutional Neural Networks (CNN).",
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for external frontend or mobile integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Files and Templates
static_dir = APP_DIR / "static"
templates_dir = APP_DIR / "templates"

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))


@app.on_event("startup")
async def startup_event():
    """Load model during application startup."""
    model_service.load_model()


@app.get("/", response_class=HTMLResponse, summary="Serve Web Interface")
async def serve_home(request: Request):
    """Renders the main web interface for LeafGuard AI."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "total_classes": len(model_service.class_indices) or len(DISEASE_KNOWLEDGE_BASE)
        }
    )


@app.post("/predict", summary="Predict plant disease from leaf image")
@app.post("/api/predict", summary="Alias API for leaf disease prediction")
async def predict_image(file: UploadFile = File(...)):
    """
    Accepts an uploaded leaf image (JPEG, PNG, WebP) and returns:
    - Detected plant species & health status
    - Specific disease identification
    - Prediction confidence score (%)
    - Top-3 alternative candidate predictions
    - Detailed symptoms, causes, organic treatments, and chemical remedies
    """
    # 1. Validate file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file format '{file_ext}'. Allowed formats: {', '.join(settings.ALLOWED_EXTENSIONS)}"
        )

    # 2. Read image content
    try:
        contents = await file.read()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to read uploaded file: {str(e)}"
        )

    # 3. Check file size limit
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(contents) > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds maximum upload size limit of {settings.MAX_UPLOAD_SIZE_MB}MB."
        )

    if len(contents) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty."
        )

    # 4. Perform Inference
    try:
        result = model_service.predict(contents, top_k=3)
        result["filename"] = file.filename
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference error during disease analysis: {str(e)}"
        )


@app.get("/health", summary="API Health Check")
async def health_check():
    """Returns application status, model loading state, and configuration info."""
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "model_loaded": model_service.is_loaded,
        "is_mock_fallback": model_service.is_mock,
        "total_classes": len(model_service.class_indices),
        "model_file_exists": settings.MODEL_PATH.exists(),
        "model_path": str(settings.MODEL_PATH.name)
    }


@app.get("/classes", summary="List all supported plant disease classes")
async def list_classes():
    """Returns the list of 38 classes supported by the trained CNN."""
    classes_list = []
    for idx, raw_name in sorted(model_service.class_indices.items()):
        details = get_disease_details(raw_name)
        classes_list.append({
            "index": idx,
            "raw_name": raw_name,
            "plant": details["plant"],
            "disease": details["disease"],
            "is_healthy": details["is_healthy"],
            "severity": details["severity"]
        })
    return {
        "total": len(classes_list),
        "classes": classes_list
    }


@app.get("/remedies/{raw_class_name}", summary="Get remedies for a specific disease class")
async def get_remedy(raw_class_name: str):
    """Returns complete treatment, prevention, and symptom details for a specified class."""
    details = get_disease_details(raw_class_name)
    return {
        "class_name": raw_class_name,
        "details": details
    }
