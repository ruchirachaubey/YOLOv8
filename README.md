# 🚀 SpaceSafetyScanner: YOLOv8-Based Space Object Detection

This project leverages YOLOv8 to detect essential safety objects inside a synthetic space station environment (provided by Falcon Digital Twin). The aim is to enhance **equipment tracking**, **crew safety**, and **inventory management** in space missions.

---

## 🌐 Demo Application (Frontend)

An interactive web interface is built using Streamlit to make the model usable in real time.

### Features
- Upload space station images  
- Detect safety equipment (Fire Extinguishers, Oxygen Tanks, Toolboxes)  
- Adjustable confidence threshold  
- Visual bounding boxes with detection scores  
- Side-by-side comparison (Original vs Detected image)  

## 📁 Project Structure

| File/Folder              | Description                     |
|--------------------------|---------------------------------|
| `best.pt`                | Trained YOLOv8 model            |
| `yolo_params.yaml`       | Dataset configuration file      |
| `hackathon_project.ipynb`| Training + evaluation notebook  |
| `Curves/`                | Evaluation graphs               |
| `test_predictions3/`     | Test predictions                |
| `Failure analysis/`      | Failure cases                   |
| `app.py`                 | Streamlit frontend              |

---

## ⚙️ How to Run

### Install Dependencies
```bash
pip install ultralytics streamlit opencv-python pillow

## 📊 Evaluation Metrics

| Metric       | Validation | Test |
|--------------|------------|------|
| Precision    | 95.1%      | 76.0% |
| Recall       | 86.6%      | 73.6% |
| mAP@0.5      | 90.7%      | 71.2% |
| mAP@0.5:0.95 | 78.4%      | 59.3% |

**Final Test mAP: 0.71**

---

## ❌ Failure Analysis

### Wrong Class Prediction
- Predicted label does not match ground truth  
- **Solution:** Increase dataset diversity  

### Poor Bounding Box (Low IoU)
- Bounding boxes are inaccurate  
- **Solution:** Use higher resolution + tune IoU  

### Missing Detection
- Object not detected  
- **Solution:** Improve class balance and retrain  

---

## 📈 Improvements Applied

| Parameter      | Before | After |
|----------------|--------|-------|
| Epochs         | 5      | 10    |
| Mosaic         | 0.1    | 0.5   |
| Optimizer      | AdamW  | SGD (tested) |
| Learning Rate  | 0.001  | 0.0005 |

---

## 🚀 Future Work

- Train on larger datasets (synthetic + real)  
- Advanced hyperparameter tuning  
- Deploy as API / full web app  
- Add real-time video detection  
