"""
Tests for LeafGuard AI FastAPI endpoints.
Run with: pytest
"""

import io
from pathlib import Path
from PIL import Image
import pytest

# Note: We use FastAPI TestClient if installed, or direct request checks
try:
    from fastapi.testclient import TestClient
    from app.main import app
    client = TestClient(app)
    HAS_TESTCLIENT = True
except ImportError:
    HAS_TESTCLIENT = False


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_home_page():
    """Verify home page loads successfully with HTML content."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "LeafGuard" in response.text


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_health_endpoint():
    """Verify /health returns 200 OK and appropriate metadata."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "model_loaded" in data
    assert "total_classes" in data
    assert data["total_classes"] == 38


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_classes_endpoint():
    """Verify /classes returns all 38 classes."""
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 38
    assert len(data["classes"]) == 38
    first_class = data["classes"][0]
    assert "plant" in first_class
    assert "disease" in first_class


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_remedies_endpoint():
    """Verify /remedies returns complete treatment info for Tomato Early Blight."""
    response = client.get("/remedies/Tomato___Early_blight")
    assert response.status_code == 200
    data = response.json()
    details = data["details"]
    assert details["plant"] == "Tomato"
    assert "Early Blight" in details["disease"]
    assert len(details["organic_remedies"]) > 0
    assert len(details["chemical_remedies"]) > 0


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_predict_invalid_extension():
    """Verify invalid file types are rejected with 400 Bad Request."""
    file_content = b"This is a text file, not an image."
    files = {"file": ("test.txt", file_content, "text/plain")}
    response = client.post("/predict", files=files)
    assert response.status_code == 400
    assert "Unsupported file format" in response.json()["detail"]


@pytest.mark.skipif(not HAS_TESTCLIENT, reason="FastAPI TestClient / httpx not installed")
def test_predict_valid_image():
    """Verify that a valid generated dummy image passes prediction."""
    # Create a small dummy RGB image
    img = Image.new("RGB", (224, 224), color=(34, 139, 34))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    files = {"file": ("leaf.jpg", buf, "image/jpeg")}
    response = client.post("/predict", files=files)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "plant" in data
    assert "disease" in data
    assert "confidence" in data
    assert "organic_remedies" in data
    assert "chemical_remedies" in data
