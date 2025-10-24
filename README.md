# 🚀 SpaceSafetyScanner2 – Real-Time Tool Detection App

This project delivers a **real-time tool detection mobile application** designed specifically for critical environments like space stations. By leveraging a high-performance **YOLOv8 model** running directly on an Android device, the app ensures **crew safety** and **inventory management** by tracking essential safety equipment.

---

## ✨ Key Features & Functionality

| Feature | Description | Status |
| :--- | :--- | :--- |
| **Real-Time Detection** | Uses the phone’s camera to detect tools like **Fire Extinguishers**, **ToolBoxes**, and **Oxygen Tanks**. | ✅ Implemented |
| **Automated Alerts** | Sends immediate **alerts** if any critical tool is missing or if the detection confidence drops below 50%. | ✅ Implemented |
| **Local Tracking** | Tracks and stores the **last seen time and location** of each tool using a local database. | ✅ Implemented |
| **Cloud Ready** | Supports optional **cloud sync** with Firebase for data access from ground stations. | 🛠 Planned |
| **Future Upgrades** | Plans include **voice alerts** and **AR-based tool guidance** using ARCore. | 💡 Future |

---

## 🧠 Technical Details & Model Evaluation

This project utilizes computer vision to enhance equipment tracking within a synthetic space station environment (provided by Falcon Digital Twin).

### Model & Deployment

* **Model Architecture:** **YOLOv8** (You Only Look Once, v8)
* **Training Data:** Real + synthetic images.
* **Deployment Target:** Android devices.
* **Mobile Conversion:** The model is converted to **TorchScript** for efficient on-device execution.

### 📊 Performance Metrics (Test Set)

| Metric | Validation Set | **Test Set** |
| :--- | :--- | :--- |
| **Precision** | 95.1% | **76.0%** |
| **Recall** | 86.6% | **73.6%** |
| **mAP@0.5** | 90.7% | **71.2%** |
| mAP@0.5:0.95 | 78.4% | 59.3% |

➡️ **Current mAP on test set: 0.71**

### ❌ Failure Analysis & Correction

Detailed failure analysis identified misdetections, categorized as:

| Failure Type | Description | Correction Strategy |
| :--- | :--- | :--- |
| **Wrong Class Prediction** | Predicted label $\neq$ Ground truth label. | Improve class separation with more diverse synthetic data. |
| **Poor Box Location** | Bounding box is misaligned or loose (Low IoU). | Fine-tune with higher-resolution images and adjusted thresholds. |
| **Missing Detection** | No box predicted for ground truth object. | Retrain with more balanced data (`single_cls=False`). |

---

## 📁 Project Structure (Code & Data)

| File/Folder | Description |
| :--- | :--- |
| `SpaceSafetyScanner2/` | Root directory for the Android application (containing all app code). |
| `best.pt` | Trained YOLOv8 model (space station object detector). |
| `yolo_params.yaml` | Dataset configuration file (train/val/test split). |
| `hackathon_project.ipynb` | Full Colab notebook: training, evaluation, failure analysis. |
| `Curves/` | Model evaluation graphs (`confusion_matrix.png`, `PR_curve.png`, etc.). |
| `Failure analysis/` | Images showing model errors and failure types. |

### 📱 App Structure Overview

SpaceSafetyScanner2/ └── app/ ├── build.gradle.kts # Build settings for the app └── src/ └── main/ ├── java/.../ │ ├── MainActivity.kt # Controls camera, ML model, UI │ └── OverlayView.kt # Draws boxes over detected tools ├── assets/ │ ├── best.torchscript.pt # The ML model file (converted) │ └── labelmap.txt # Tool labels (class IDs to names) └── AndroidManifest.xml # App permissions (camera, etc.)


---

## 🛠 Getting Started (Model Usage)

### Step 1: Convert YOLOv8 Model for Android

The model must be converted to TorchScript format to run efficiently on Android.

```python
from ultralytics import YOLO

# Load the trained PyTorch model
model = YOLO('best.pt')

# Export to TorchScript format
model.export(format='torchscript')
Step 2: Run a Prediction
Use the following Python snippet to test the model locally on an image:

Python

from ultralytics import YOLO

# Load the trained model
model = YOLO('best.pt')

# Run prediction on a source image
results = model.predict(source='your_image.jpg', save=True)
