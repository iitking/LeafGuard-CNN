"""
LeafGuard AI - Model Service
Handles model loading, image preprocessing, and inference.
"""

import io
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

import numpy as np
from PIL import Image

from app.config import settings
from app.disease_data import get_disease_details

logger = logging.getLogger("leafguard.model_service")
logging.basicConfig(level=logging.INFO)

class ModelService:
    def __init__(self):
        self.model = None
        self.class_indices: Dict[int, str] = {}
        self.is_loaded: bool = False
        self.is_mock: bool = False
        self._load_class_indices()

    def _load_class_indices(self) -> None:
        """Loads the class mapping from class_indices.json."""
        try:
            if settings.CLASS_INDICES_PATH.exists():
                with open(settings.CLASS_INDICES_PATH, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)
                    # Convert keys to int (json keys are strings)
                    self.class_indices = {int(k): v for k, v in raw_data.items()}
                logger.info(f"Loaded {len(self.class_indices)} class mappings from {settings.CLASS_INDICES_PATH}")
            else:
                logger.warning(f"Class indices file not found at {settings.CLASS_INDICES_PATH}")
        except Exception as e:
            logger.error(f"Failed to load class indices: {e}")

    def load_model(self) -> bool:
        """
        Loads the trained model from LeafGuard-CNN_model.pkl.
        If TensorFlow is unavailable or unpickling fails in the environment,
        activates safe fallback mode so the application remains operable.
        """
        if self.is_loaded:
            return True

        if not settings.MODEL_PATH.exists():
            logger.warning(f"Model file not found at {settings.MODEL_PATH}. Enabling fallback mode.")
            self.is_mock = True
            self.is_loaded = True
            return False

        try:
            logger.info(f"Attempting to load model from {settings.MODEL_PATH}...")
            # Try importing tensorflow first
            import tensorflow as tf
            import pickle

            with open(settings.MODEL_PATH, "rb") as f:
                self.model = pickle.load(f)
            
            self.is_loaded = True
            self.is_mock = False
            logger.info("Successfully loaded LeafGuard-CNN model!")
            return True

        except ImportError as ie:
            logger.warning(
                f"TensorFlow is not installed in the current environment: {ie}. "
                "Running in demonstration/fallback mode. Install dependencies with: pip install -r requirements.txt"
            )
            self.is_mock = True
            self.is_loaded = True
            return False

        except Exception as e:
            logger.error(
                f"Error while loading pickle model: {e}. "
                "Running in demonstration/fallback mode."
            )
            self.is_mock = True
            self.is_loaded = True
            return False

    def preprocess_image(self, image_bytes: bytes) -> np.ndarray:
        """
        Preprocesses raw image bytes to match model training:
        1. Open image with Pillow and convert to RGB (removes alpha or grayscale channels)
        2. Resize to (224, 224)
        3. Convert to float32 numpy array and scale to [0, 1]
        4. Add batch dimension -> (1, 224, 224, 3)
        """
        img = Image.open(io.BytesIO(image_bytes))
        
        # Ensure 3-channel RGB
        if img.mode != "RGB":
            img = img.convert("RGB")
            
        img = img.resize((settings.IMG_WIDTH, settings.IMG_HEIGHT))
        img_array = np.array(img, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, image_bytes: bytes, top_k: int = 3) -> Dict[str, Any]:
        """
        Performs plant disease prediction on given image bytes.
        Returns top prediction, top_k alternatives, and full disease details.
        """
        if not self.is_loaded:
            self.load_model()

        # Handle Mock / Fallback mode if TensorFlow or Model is not loaded
        if self.is_mock or self.model is None:
            return self._mock_prediction(image_bytes)

        # Real Inference
        preprocessed = self.preprocess_image(image_bytes)
        raw_preds = self.model.predict(preprocessed)
        
        # Squeeze batch dimension
        probs = raw_preds[0]
        
        # Top-1 class
        best_idx = int(np.argmax(probs))
        confidence = float(probs[best_idx])
        raw_class_name = self.class_indices.get(best_idx, "Unknown")
        
        # Top-K predictions
        top_indices = np.argsort(probs)[::-1][:top_k]
        top_predictions = []
        for idx in top_indices:
            idx_int = int(idx)
            c_name = self.class_indices.get(idx_int, f"Class {idx_int}")
            details = get_disease_details(c_name)
            top_predictions.append({
                "class_index": idx_int,
                "raw_class": c_name,
                "plant": details["plant"],
                "disease": details["disease"],
                "confidence": round(float(probs[idx_int]) * 100, 2),
                "is_healthy": details["is_healthy"]
            })

        # Fetch comprehensive metadata for best prediction
        disease_info = get_disease_details(raw_class_name)

        return {
            "success": True,
            "status": "Healthy" if disease_info["is_healthy"] else "Disease Detected",
            "is_healthy": disease_info["is_healthy"],
            "plant": disease_info["plant"],
            "disease": disease_info["disease"],
            "raw_class": raw_class_name,
            "confidence": round(confidence * 100, 2),
            "severity": disease_info["severity"],
            "pathogen": disease_info["pathogen"],
            "summary": disease_info["summary"],
            "symptoms": disease_info["symptoms"],
            "organic_remedies": disease_info["organic_remedies"],
            "chemical_remedies": disease_info["chemical_remedies"],
            "prevention": disease_info["prevention"],
            "top_predictions": top_predictions,
            "is_mock_fallback": False
        }

    def _mock_prediction(self, image_bytes: bytes) -> Dict[str, Any]:
        """
        Graceful fallback when TensorFlow is not installed in the host environment.
        Detects image size and returns a structured response to allow testing UI and API.
        """
        try:
            img = Image.open(io.BytesIO(image_bytes))
            width, height = img.size
        except Exception:
            width, height = (224, 224)

        # Default representative response
        sample_class = "Tomato___Early_blight"
        info = get_disease_details(sample_class)

        return {
            "success": True,
            "status": "Disease Detected",
            "is_healthy": False,
            "plant": info["plant"],
            "disease": info["disease"],
            "raw_class": sample_class,
            "confidence": 96.85,
            "severity": info["severity"],
            "pathogen": info["pathogen"],
            "summary": info["summary"],
            "symptoms": info["symptoms"],
            "organic_remedies": info["organic_remedies"],
            "chemical_remedies": info["chemical_remedies"],
            "prevention": info["prevention"],
            "top_predictions": [
                {
                    "class_index": 29,
                    "raw_class": "Tomato___Early_blight",
                    "plant": "Tomato",
                    "disease": "Early Blight",
                    "confidence": 96.85,
                    "is_healthy": False
                },
                {
                    "class_index": 30,
                    "raw_class": "Tomato___Late_blight",
                    "plant": "Tomato",
                    "disease": "Late Blight",
                    "confidence": 2.45,
                    "is_healthy": False
                },
                {
                    "class_index": 32,
                    "raw_class": "Tomato___Septoria_leaf_spot",
                    "plant": "Tomato",
                    "disease": "Septoria Leaf Spot",
                    "confidence": 0.52,
                    "is_healthy": False
                }
            ],
            "is_mock_fallback": True,
            "note": "Demo fallback active. Install TensorFlow in your environment to run live CNN weights from LeafGuard-CNN_model.pkl."
        }

# Global singleton
model_service = ModelService()
