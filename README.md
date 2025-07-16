# YOLO_Model

Here's a stylish, professional `README.md` for your **YOLOv8 Live Object Detection App** using `➤` markers and rich formatting — clean, modern, and ready to paste to GitHub:

---


<h1 align="center" style="font-size: 3em; color: #e74c3c;">🎯 YOLOv8 Live Object Detection App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-red?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20UI-darkred?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/WebRTC-Live%20Camera-blue?style=for-the-badge&logo=webrtc">
  <img src="https://img.shields.io/badge/OpenCV-Real-Time-green?style=for-the-badge&logo=opencv">
</p>

---

## ➤ Project Overview

This app enables **real-time object detection** using **YOLOv8 models** from Ultralytics via your **webcam**, all within a clean **Streamlit** interface.

> 💡 Built for speed, simplicity, and visual clarity. Use it to demo YOLOv8 models on the fly — no setup required beyond your webcam.

---

## ➤ Features

✔️ Streamlit + WebRTC for live webcam feed  
✔️ Multiple YOLOv8 models (nano to x-large)  
✔️ Interactive sidebar with confidence slider  
✔️ Real-time bounding box visualization  
✔️ No file uploads or image selection — just run and detect!

---

## ➤ YOLOv8 Models Supported

| Model      | Description                   |
|------------|-------------------------------|
| `yolov8n.pt` | Nano (fastest, smallest)       |
| `yolov8s.pt` | Small                         |
| `yolov8m.pt` | Medium                        |
| `yolov8l.pt` | Large                         |
| `yolov8x.pt` | X-Large (most accurate)       |

Choose your desired model via the sidebar.

---

## ➤ App Preview



\[ Streamlit UI ]
┌──────────────────────────────────────┐
│     🔍 YOLOv8 Live Object Detection  │
└──────────────────────────────────────┘
\[ WebRTC Video Stream with BBoxes     ]
\[ Sidebar: Model Selector + Confidence ]


---



> Make sure your **webcam is enabled** and functional.


## ➤ How it Works

➤ The app loads a YOLOv8 model (`YOLO(model_type)`)
➤ Each video frame from webcam is passed to the model
➤ Bounding boxes are drawn using `.plot()`
➤ Output is streamed to the frontend via `webrtc_streamer`

---

## ➤ Author

**Chirag Kaushik**
*Data Science, Deep Learning & Computer Vision Enthusiast*
🔗 [LinkedIn Profile](https://www.linkedin.com/in/chirag-kaushik-profile)

---

## ➤ License

This project is open-source and educational.
YOLO models are provided by [Ultralytics](https://github.com/ultralytics/ultralytics).


---

Would you like a GIF/preview badge added at the top? Or help pushing this to GitHub with a `requirements.txt`? Let me know!

