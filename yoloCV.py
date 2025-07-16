import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from ultralytics import YOLO
import av
import cv2

# Set Streamlit page config
st.set_page_config(page_title="YOLOv8 Live Detection", layout="centered")
st.title("🔍 YOLOv8 Live Object Detection")
st.markdown("Detect objects in real-time using your webcam and **YOLOv8**.")
st.markdown("---")

# Sidebar for model selection and confidence
with st.sidebar:
    st.header("Settings")
    model_type = st.selectbox("Select YOLOv8 Model", ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt"], index=0)
    conf = st.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)
    st.markdown("---")
    st.info("Press 'Stop' to end webcam stream.")

# Load YOLO model
@st.cache_resource(show_spinner=True)
def load_model(model_type):
    return YOLO(model_type)

model = load_model(model_type)

# Video transformer for YOLO inference
class YOLOVideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        results = model.predict(source=img, show=False, conf=conf, verbose=False)
        annotated_img = results[0].plot()
        return annotated_img

# Start webcam stream
webrtc_streamer(
    key="yolov8-live",
    video_transformer_factory=YOLOVideoTransformer,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit, OpenCV, and Ultralytics YOLOv8")
