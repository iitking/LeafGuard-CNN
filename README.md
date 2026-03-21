# 🌿 LeafGuard AI — Deep CNN Plant Disease Diagnosis & Treatment Platform

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

**An intelligent end-to-end Computer Vision platform that detects 38 crop diseases from leaf images in milliseconds and provides instant organic & chemical treatment recommendations.**

[Features](#-key-features) •
[Quickstart](#-quickstart-guide) •
[GitHub & Git LFS](#-important-github--model-file-setup) •
[API Reference](#-api-documentation) •
[Supported Crops](#-supported-crops--conditions-38-classes) •
[Deployment](#-docker--cloud-deployment)

</div>

---

## 🌟 Key Features

- 🔬 **High-Accuracy Deep CNN**: Custom Sequential Convolutional Neural Network trained on 50,000+ leaf images across 38 distinct crop disease conditions.
- ⚡ **Lightning Fast FastAPI Backend**: Sub-100ms inference time with async file stream processing and validation.
- 🎨 **Modern Botanical Web Interface**:
  - Drag-and-drop file upload with live client-side image preview.
  - **Live Camera Capture**: Directly photograph plant leaves via mobile/laptop browser.
  - **Try Sample Leaf**: One-click instant demonstration with bundled leaf sample.
  - **Probability Breakdown**: Top-3 candidate predictions with animated confidence bars.
- 🩺 **Actionable Agrochemical & Organic Remedies**:
  - Pathogen identification (Fungal, Bacterial, Viral, Pest).
  - Observed visual symptoms.
  - **Eco-friendly Organic Remedies** (Neem, potassium bicarbonate, bio-controls).
  - **Chemical Treatments** (Standard commercial fungicides & bactericides).
  - **Agronomic Prevention Plan** (Crop rotation, pruning, drip irrigation).
- 🖨️ **Printable Plant Health Report**: Export clean diagnosis sheets for farmers and agronomists.
- 🐳 **Containerized & Production Ready**: Pre-configured Dockerfile, Docker Compose, and environment variables.

---

## 📁 Project Architecture

```
LeafGuard-CNN/
├── .gitattributes             # Git LFS tracking for *.pkl (>100MB model files)
├── .gitignore                 # Standard Python, macOS, IDE, and cache ignore rules
├── .env.example               # Environment variables template
├── Dockerfile                 # Production Docker container configuration
├── docker-compose.yml         # Multi-platform docker container service
├── LeafGuard-CNN_model.pkl    # Trained CNN weights (Pickle / Keras Sequential)
├── LeafGuard_CNN.ipynb        # Original model training & evaluation notebook
├── class_indices.json         # 38-class index-to-label mapping dictionary
├── anthracnose-1-920x518.webp # Sample leaf image for testing
├── requirements.txt           # Production Python dependencies
├── run.py                     # Convenience server launcher script
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI endpoints, routes, static mount & CORS
│   ├── config.py              # Application settings, paths, image resolutions
│   ├── model_service.py       # Inference engine, image preprocessing, fallback mode
│   ├── disease_data.py        # Comprehensive 38-class remedies & symptoms database
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Modern responsive glassmorphism UI styles
│   │   ├── js/
│   │   │   └── app.js         # Drag-drop, camera snap, and live UI controller
│   │   └── samples/
│   │       └── sample_leaf.webp
│   └── templates/
│       └── index.html         # Web dashboard interface template
└── tests/
    ├── __init__.py
    └── test_api.py            # Automated API integration tests
```

---

## ⚠️ Important: GitHub & Model File Setup

GitHub imposes a strict **100 MB file limit** per single file. Because `LeafGuard-CNN_model.pkl` is **~573 MB**, standard `git push` will be blocked unless you use **Git LFS (Large File Storage)** or external model hosting.

### Option A: Using Git LFS (Recommended for GitHub)

```bash
# 1. Install Git LFS (macOS: brew install git-lfs | Ubuntu: sudo apt install git-lfs)
git lfs install

# 2. Track large model files (.gitattributes is already created for you)
git lfs track "*.pkl"

# 3. Add files and commit
git add .gitattributes
git add .
git commit -m "feat: initial commit of LeafGuard AI platform"

# 4. Push to your GitHub repository
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/LeafGuard-CNN.git
git push -u origin main
```

### Option B: Hosting Model on Hugging Face / Google Drive (Free Alternative)

If you don't want to use Git LFS bandwidth on GitHub:
1. Open `.gitignore` and uncomment `LeafGuard-CNN_model.pkl`.
2. Upload `LeafGuard-CNN_model.pkl` to **Hugging Face Hub** or **Google Drive**.
3. Add a direct download link or automated downloader script in `app/model_service.py`.

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/LeafGuard-CNN.git
cd LeafGuard-CNN
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note for Apple Silicon (M1/M2/M3 Mac users)**:
> If installing standard `tensorflow` gives wheel conflicts, install Apple-optimized TensorFlow:
> ```bash
> pip install tensorflow-macos
> ```

### 4. Run the Application
```bash
# Option 1: Using the launcher script
python run.py

# Option 2: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Now open **http://localhost:8000** in your browser to access the web application!

---

## 📖 API Documentation

Once the server is running, explore the interactive documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Key Endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Web dashboard user interface |
| `POST` | `/predict` | Diagnose uploaded leaf image (Form `file`) |
| `GET` | `/health` | Server status and model load confirmation |
| `GET` | `/classes` | List all 38 supported plant diseases |
| `GET` | `/remedies/{class_name}` | Fetch detailed causes, symptoms & remedies |

### Example cURL Request:
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@anthracnose-1-920x518.webp"
```

### Sample Response:
```json
{
  "success": true,
  "status": "Disease Detected",
  "is_healthy": false,
  "plant": "Tomato",
  "disease": "Early Blight",
  "raw_class": "Tomato___Early_blight",
  "confidence": 98.42,
  "severity": "Moderate to High",
  "pathogen": "Alternaria solani (Fungus)",
  "summary": "Foliar disease starting on bottom leaves and progressing upwards with target-ring spots.",
  "symptoms": [
    "Dark brown spots with concentric target-board rings on older foliage.",
    "Leaves yellow around spots, turn brown, and drop."
  ],
  "organic_remedies": [
    "Prune off the lowest 12-18 inches of branches to prevent splash infection.",
    "Spray organic copper fungicide or Bacillus subtilis."
  ],
  "chemical_remedies": [
    "Apply Chlorothalonil (Daconil), Mancozeb, or Azoxystrobin."
  ],
  "prevention": [
    "Rotate tomato location every 2-3 years away from solanaceous plants.",
    "Stake or cage tomatoes for upright growth and maximum air circulation."
  ],
  "top_predictions": [
    {
      "class_index": 29,
      "raw_class": "Tomato___Early_blight",
      "plant": "Tomato",
      "disease": "Early Blight",
      "confidence": 98.42,
      "is_healthy": false
    }
  ]
}
```

---

## 🌾 Supported Crops & Conditions (38 Classes)

| Crop | Conditions Detected |
|---|---|
| **Apple** | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| **Blueberry** | Healthy |
| **Cherry** | Powdery Mildew, Healthy |
| **Corn (Maize)** | Cercospora Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| **Grape** | Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis), Healthy |
| **Orange / Citrus** | Citrus Greening (Huanglongbing - HLB) |
| **Peach** | Bacterial Spot, Healthy |
| **Pepper (Bell)** | Bacterial Spot, Healthy |
| **Potato** | Early Blight, Late Blight, Healthy |
| **Raspberry** | Healthy |
| **Soybean** | Healthy |
| **Squash** | Powdery Mildew |
| **Strawberry** | Leaf Scorch, Healthy |
| **Tomato** | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Two-Spotted Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |

---

## 🐳 Docker & Cloud Deployment

### Run with Docker Compose
```bash
docker-compose up --build
```

### Build & Run Docker Image Directly
```bash
docker build -t leafguard-ai:latest .
docker run -p 8000:8000 leafguard-ai:latest
```

### Deploying to Cloud (Render / Railway / Fly.io / AWS EC2)
1. Push your repository to GitHub.
2. In **Render** or **Railway**, create a new **Web Service** connected to your repo.
3. Select **Docker** environment or Python environment (`uvicorn app.main:app --host 0.0.0.0 --port $PORT`).
4. Set health check path to `/health`.

---

## 🧪 Running Automated Tests

Run the test suite using pytest:
```bash
pytest -v
```

---

## 🤝 Contributing

Contributions are welcomed! If you'd like to improve the architecture, add more crop species, or optimize the frontend:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <sub>Developed with ❤️ for Farmers, Gardeners, and Agronomists worldwide.</sub>
</div>
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
<!-- log -->
