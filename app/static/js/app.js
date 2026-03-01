/**
 * LeafGuard AI - Frontend Controller
 * Handles image selection, drag-and-drop, camera capture,
 * API requests to FastAPI backend, and dynamic result rendering.
 */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const emptyState = document.getElementById('emptyState');
    const previewState = document.getElementById('previewState');
    const imagePreview = document.getElementById('imagePreview');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const fileSizeDisplay = document.getElementById('fileSizeDisplay');
    
    // Buttons
    const browseBtn = document.getElementById('browseBtn');
    const sampleBtn = document.getElementById('sampleBtn');
    const cameraBtn = document.getElementById('cameraBtn');
    const clearBtn = document.getElementById('clearBtn');
    const reselectBtn = document.getElementById('reselectBtn');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const scanAnotherBtn = document.getElementById('scanAnotherBtn');
    const printReportBtn = document.getElementById('printReportBtn');

    // Camera Stream Elements
    const cameraContainer = document.getElementById('cameraContainer');
    const cameraVideo = document.getElementById('cameraVideo');
    const cameraCanvas = document.getElementById('cameraCanvas');
    const captureBtn = document.getElementById('captureBtn');
    const closeCameraBtn = document.getElementById('closeCameraBtn');
    let videoStream = null;

    // Overlays & Results
    const loadingOverlay = document.getElementById('loadingOverlay');
    const resultsCard = document.getElementById('resultsCard');
    const toast = document.getElementById('toast');

    // Currently selected file
    let selectedFile = null;

    // -------------------------------------------------------------
    // Toast Notification Utility
    // -------------------------------------------------------------
    function showToast(message, type = 'info') {
        toast.textContent = message;
        toast.className = 'toast';
        if (type === 'error') {
            toast.style.backgroundColor = '#b91c1c';
        } else if (type === 'success') {
            toast.style.backgroundColor = '#059669';
        } else {
            toast.style.backgroundColor = '#0f172a';
        }
        toast.classList.remove('hidden');

        setTimeout(() => {
            toast.classList.add('hidden');
        }, 4000);
    }

    // -------------------------------------------------------------
    // File Selection & Drag & Drop Handling
    // -------------------------------------------------------------
    browseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        fileInput.click();
    });

    reselectBtn.addEventListener('click', () => {
        fileInput.click();
    });

    emptyState.addEventListener('click', (e) => {
        if (!e.target.closest('button')) {
            fileInput.click();
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
            handleSelectedFile(e.target.files[0]);
        }
    });

    // Drag & Drop events
    ['dragenter', 'dragover'].forEach(eventName => {
        emptyState.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            emptyState.classList.add('drag-over');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        emptyState.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            emptyState.classList.remove('drag-over');
        });
    });

    emptyState.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        if (dt.files && dt.files[0]) {
            handleSelectedFile(dt.files[0]);
        }
    });

    function formatBytes(bytes, decimals = 1) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    function handleSelectedFile(file) {
        // Validate type
        const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/jpg'];
        if (!validTypes.includes(file.type)) {
            showToast('Please upload a valid image file (JPEG, PNG, WebP)', 'error');
            return;
        }

        // Validate size (15MB)
        if (file.size > 15 * 1024 * 1024) {
            showToast('Image size exceeds 15MB limit', 'error');
            return;
        }

        selectedFile = file;

        // Render preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            fileNameDisplay.textContent = file.name;
            fileSizeDisplay.textContent = formatBytes(file.size);

            emptyState.classList.add('hidden');
            cameraContainer.classList.add('hidden');
            previewState.classList.remove('hidden');
            resultsCard.classList.add('hidden');
        };
        reader.readAsDataURL(file);
    }

    clearBtn.addEventListener('click', resetUploader);
    scanAnotherBtn.addEventListener('click', () => {
        resetUploader();
        window.scrollTo({ top: dropzone.offsetTop - 80, behavior: 'smooth' });
    });

    function resetUploader() {
        selectedFile = null;
        fileInput.value = '';
        imagePreview.src = '';
        previewState.classList.add('hidden');
        resultsCard.classList.add('hidden');
        cameraContainer.classList.add('hidden');
        emptyState.classList.remove('hidden');
        stopCamera();
    }

    // -------------------------------------------------------------
    // "Try Sample Leaf" Feature
    // -------------------------------------------------------------
    sampleBtn.addEventListener('click', async () => {
        try {
            showToast('Loading sample leaf image...', 'info');
            const response = await fetch('/static/samples/sample_leaf.webp');
            if (!response.ok) {
                throw new Error('Sample image not found on server');
            }
            const blob = await response.blob();
            const file = new File([blob], 'grape_anthracnose_sample.webp', { type: 'image/webp' });
            handleSelectedFile(file);
        } catch (err) {
            showToast('Could not load sample leaf: ' + err.message, 'error');
        }
    });

    // -------------------------------------------------------------
    // Live Camera Capture
    // -------------------------------------------------------------
    cameraBtn.addEventListener('click', async () => {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            showToast('Camera access is not supported by your browser', 'error');
            return;
        }

        try {
            videoStream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment' }
            });
            cameraVideo.srcObject = videoStream;
            emptyState.classList.add('hidden');
            previewState.classList.add('hidden');
            resultsCard.classList.add('hidden');
            cameraContainer.classList.remove('hidden');
        } catch (err) {
            showToast('Camera access denied or unavailable: ' + err.message, 'error');
        }
    });

    closeCameraBtn.addEventListener('click', () => {
        stopCamera();
        cameraContainer.classList.add('hidden');
        emptyState.classList.remove('hidden');
    });

    function stopCamera() {
        if (videoStream) {
            videoStream.getTracks().forEach(track => track.stop());
            videoStream = null;
        }
    }

    captureBtn.addEventListener('click', () => {
        if (!cameraVideo.videoWidth) return;

        cameraCanvas.width = cameraVideo.videoWidth;
        cameraCanvas.height = cameraVideo.videoHeight;
        const ctx = cameraCanvas.getContext('2d');
        ctx.drawImage(cameraVideo, 0, 0, cameraCanvas.width, cameraCanvas.height);

        cameraCanvas.toBlob((blob) => {
            stopCamera();
            cameraContainer.classList.add('hidden');
            const file = new File([blob], 'camera_captured_leaf.jpg', { type: 'image/jpeg' });
            handleSelectedFile(file);
        }, 'image/jpeg', 0.95);
    });

    // -------------------------------------------------------------
    // Analysis & API Call
    // -------------------------------------------------------------
    analyzeBtn.addEventListener('click', async () => {
        if (!selectedFile) {
            showToast('Please select an image first', 'error');
            return;
        }

        loadingOverlay.classList.remove('hidden');

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errData = await response.json().catch(() => ({}));
                throw new Error(errData.detail || 'Prediction failed with status ' + response.status);
            }

            const data = await response.json();
            renderResults(data);
            showToast('Diagnosis complete!', 'success');
        } catch (error) {
            showToast('Analysis error: ' + error.message, 'error');
        } finally {
            loadingOverlay.classList.add('hidden');
        }
    });

    // -------------------------------------------------------------
    // Render Results on UI
    // -------------------------------------------------------------
    function renderResults(data) {
        // Status Badge
        const healthBadge = document.getElementById('healthBadge');
        const statusText = document.getElementById('statusText');
        if (data.is_healthy) {
            healthBadge.className = 'status-badge healthy';
            statusText.textContent = 'Healthy Plant';
        } else {
            healthBadge.className = 'status-badge disease';
            statusText.textContent = 'Disease Detected';
        }

        // Summary Tiles
        document.getElementById('plantName').textContent = data.plant;
        const diseaseElem = document.getElementById('diseaseName');
        diseaseElem.textContent = data.disease;
        if (data.is_healthy) {
            diseaseElem.classList.remove('text-accent');
            diseaseElem.style.color = 'var(--healthy)';
        } else {
            diseaseElem.classList.add('text-accent');
            diseaseElem.style.color = '';
        }

        // Confidence
        const confidenceText = `${data.confidence}%`;
        document.getElementById('confidenceScore').textContent = confidenceText;
        const confFill = document.getElementById('confidenceFill');
        confFill.style.width = '0%';
        setTimeout(() => {
            confFill.style.width = confidenceText;
            confFill.style.backgroundColor = data.is_healthy ? 'var(--healthy)' : 'var(--primary)';
        }, 100);

        // Severity
        document.getElementById('severityLevel').textContent = data.severity;

        // Pathogen & Overview
        document.getElementById('pathogenType').innerHTML = `<strong>Pathogen:</strong> ${escapeHtml(data.pathogen)}`;
        document.getElementById('diseaseSummary').textContent = data.summary;

        // Populate lists
        populateList('symptomsList', data.symptoms);
        populateList('organicList', data.organic_remedies);
        populateList('chemicalList', data.chemical_remedies);
        populateList('preventionList', data.prevention);

        // Top-K Breakdown
        renderAlternatives(data.top_predictions);

        // Show result card and scroll smoothly
        resultsCard.classList.remove('hidden');
        resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function populateList(elementId, items) {
        const list = document.getElementById(elementId);
        list.innerHTML = '';
        if (!items || items.length === 0) {
            const li = document.createElement('li');
            li.textContent = 'No specific instructions needed for this condition.';
            list.appendChild(li);
            return;
        }

        items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            list.appendChild(li);
        });
    }

    function renderAlternatives(topList) {
        const container = document.getElementById('alternativesContainer');
        container.innerHTML = '';

        if (!topList || topList.length === 0) {
            container.innerHTML = '<p class="text-muted">No candidate predictions available.</p>';
            return;
        }

        topList.forEach(item => {
            const row = document.createElement('div');
            row.className = 'alt-row';

            const name = document.createElement('div');
            name.className = 'alt-name';
            name.textContent = `${item.plant} - ${item.disease}`;

            const barWrapper = document.createElement('div');
            barWrapper.className = 'alt-bar-wrapper';

            const bar = document.createElement('div');
            bar.className = 'alt-bar';
            bar.style.width = `${Math.min(100, Math.max(2, item.confidence))}%`;
            if (item.is_healthy) {
                bar.style.backgroundColor = 'var(--healthy)';
            }

            barWrapper.appendChild(bar);

            const pct = document.createElement('div');
            pct.className = 'alt-pct';
            pct.textContent = `${item.confidence}%`;

            row.appendChild(name);
            row.appendChild(barWrapper);
            row.appendChild(pct);

            container.appendChild(row);
        });
    }

    function escapeHtml(string) {
        return String(string)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    // -------------------------------------------------------------
    // Tabs Controller
    // -------------------------------------------------------------
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');

            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanels.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const panel = document.getElementById(`tab-${targetTab}`);
            if (panel) {
                panel.classList.add('active');
            }
        });
    });

    // -------------------------------------------------------------
    // Print Report
    // -------------------------------------------------------------
    printReportBtn.addEventListener('click', () => {
        window.print();
    });
});
