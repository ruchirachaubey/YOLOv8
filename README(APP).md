# 🔧 SpaceSafetyScanner2 – Real-Time Tool Detection App

This project is a **real-time tool detection mobile app** designed for space station environments. It helps detect critical tools like **Fire Extinguishers**, **ToolBoxes**, and **Oxygen Tanks** using a trained **YOLOv8 model** running directly on your Android device. If any tool goes missing or is detected with low confidence, the app immediately alerts the user.

---

## 💡 What This App Does

- Uses your phone’s **camera** to detect tools in real-time.
- Sends **alerts** if any tool is missing or the detection confidence drops below 50%.
- Tracks and stores the **last seen time and location** of each tool using a local database.
- Supports optional **cloud sync** with Firebase so data can be accessed from ground stations.
- Plans for future upgrades like **voice alerts** and **AR-based tool guidance** using ARCore.

---

## 🧠 How the Detection Works

- Model: **YOLOv8**, trained with real + synthetic images.
- Augmentations used: Mosaic, Blur, Flip, Rotate.
- Evaluated using: mAP, Precision, Recall, Confusion Matrix, PR Curves.
- Custom failure analysis script to identify misdetections using IoU comparison.

The model is converted to **TorchScript** so it can run efficiently on Android.

---

## 📱 App Structure (Simple Overview)

SpaceSafetyScanner2/
└── app/
├── build.gradle.kts # Build settings for the app
└── src/
└── main/
├── java/com/example/spacesafetyscanner/
│ ├── MainActivity.kt # Controls camera, ML model, UI
│ └── OverlayView.kt # Draws boxes over detected tools
│
├── res/
│ ├── layout/
│ │ └── activity_main.xml # UI design for camera + overlay
│ ├── values/ # Colors, strings, themes
│ └── drawable/ # (Optional) Icons, images
│
├── assets/
│ ├── best.torchscript.pt # The ML model file
│ └── labelmap.txt # Tool labels (class IDs to names)
│
└── AndroidManifest.xml # App permissions (camera, etc.)

yaml
Copy
Edit

---

## 🚀 Getting Started

### Step 1: Convert YOLOv8 Model

In Python (Colab or locally):

```python
from ultralytics import YOLO
model = YOLO('best.pt')
model.export(format='torchscript')
