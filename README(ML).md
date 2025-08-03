This project leverages YOLOv8 to detect essential safety objects inside a synthetic space station environment (provided by Falcon Digital Twin). The aim is to enhance **equipment tracking**, **crew safety**, and **inventory management** in space missions.

---

## 📁 Project Structure

| File/Folder           | Description                                           |
|-----------------------|------------------------------------------------------|
| `best.pt`             | Trained YOLOv8 model (space station object detector) |
| `yolo_params.yaml`    | Dataset configuration file (train/val/test split)    |
| `hackathon_project.ipynb` | Full Colab notebook: training, evaluation, failure analysis |
| `Curves/`             | Model evaluation graphs (`confusion_matrix.png`, `PR_curve.png`, etc.) |
| `test_predictions3/`  | Test image predictions: `images/` and `labels/`      |
| `Failure analysis/`   | Images showing model errors and failure types        |

---

## 📊 Evaluation Metrics

| Metric         | Validation Set | Test Set |
|----------------|----------------|----------|
| Precision      | 95.1%          | 76.0%    |
| Recall         | 86.6%          | 73.6%    |
| mAP@0.5        | 90.7%          | 71.2%    |
| mAP@0.5:0.95   | 78.4%          | 59.3%    |

➡️ **Current mAP on test set: 0.71**

> Given more time, I would further improve accuracy by increasing training epochs, tuning hyperparameters (e.g., optimizer, learning rate), and leveraging GPU resources for longer training.

---

## ❌ Failure Analysis & Correction Strategy

We performed detailed analysis on incorrect detections and categorized failures into:

1. **Wrong Class Prediction**
   - Predicted label ≠ Ground truth label.
   - Fix: Improve class separation with more diverse synthetic data.

2. **Poor Box Location (Low IoU)**
   - Box is misaligned or loose.
   - Fix: Fine-tune with higher-resolution images and adjusted `mosaic`/`IoU` thresholds.

3. **Missing Detection**
   - No box predicted for ground truth object.
   - Fix: Retrain with `single_cls=False` and more balanced data.

✅ **Failure images saved in `Failure analysis/` folder**

---

## 📈 Improvement Techniques Tried

| Parameter   | Original | Improved |
|-------------|----------|----------|
| `epochs`    | 10       | 20       |
| `mosaic`    | 0.1      | 0.5      |
| `optimizer` | AdamW    | SGD (tried) |
| `lr0`       | 0.001    | 0.0005   |

➡️ Future: Resume training from `best.pt` (warm start) to save time.

---

## 🛠 How to Use the Model

```python
from ultralytics import YOLO
model = YOLO('best.pt')
results = model.predict(source='your_image.jpg', save=True)
