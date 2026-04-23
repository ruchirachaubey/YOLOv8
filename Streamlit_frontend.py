import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# --- Page Configuration ---
st.set_page_config(
    page_title="SpaceSafetyScanner - YOLOv8",
    page_icon="🚀",
    layout="wide"
)

# --- Sidebar for Settings ---
st.sidebar.header("⚙️ Model Configuration")
confidence = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5)

# --- Title and Description ---
st.title("🚀 SpaceSafetyScanner: Tool Detection")
st.markdown("""
    This application uses a custom **YOLOv8** model to detect critical tools like 
    Fire Extinguishers, Oxygen Tanks, and Toolboxes in real-time.
    * **Model Format:** PyTorch (.pt)
    * **Target Environment:** Synthetic Space Station
""")

# --- Load Model ---
@st.cache_resource
def load_yolo_model():
    # Make sure 'best.pt' is in the same directory as this file
    model = YOLO('best.pt')
    return model

try:
    model = load_yolo_model()
    st.sidebar.success("✅ Model loaded successfully!")
except Exception as e:
    st.sidebar.error(f"❌ Error loading model: {e}")
    st.stop()

# --- File Uploader ---
uploaded_file = st.file_uploader("Upload an image for detection...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Convert uploaded file to PIL Image
    image = Image.open(uploaded_file)
    
    # UI Layout: 2 Columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Object Detection Result")
        
        # Perform Prediction
        with st.spinner('Running YOLOv8 inference...'):
            results = model.predict(image, conf=confidence)
            
            # Plot the results on the image
            res_plotted = results[0].plot()
            
            # Convert BGR (OpenCV format) to RGB (Streamlit/PIL format)
            res_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
            
            st.image(res_rgb, use_container_width=True)

    # --- Metrics and Logs ---
    st.divider()
    st.subheader("📊 Detection Metrics")
    
    boxes = results[0].boxes
    if len(boxes) > 0:
        for box in boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]
            conf_score = float(box.conf)
            
            st.write(f"Detected **{class_name}** with **{conf_score:.2f}** confidence.")
    else:
        st.warning("No objects detected above the selected confidence threshold.")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.write("Developed by [Your Name]")
st.sidebar.write("[GitHub Repository](https://github.com/ruchirachaubey/YOLOv8)")
