# RDK X5 Hardware Deployment & BPU Optimization Guide

## 1. Overview
The **RDK X5** is an edge AI developer board by D-Robotics (Horizon Robotics), featuring a quad-core 64-bit ARM Cortex-A55 processor and a **10 TOPS Brain Processing Unit (BPU)** built on the **Bayes** architecture.

By offloading the YOLO feature extractor and detection heads to the BPU, host CPU utilization remains under $25\%$, preserving computational headroom for video decoding, multi-student tracking, and visual user interfaces.

---

## 2. Toolchain Prerequisites
Reference Repository: [D-Robotics/rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo)

Install the Horizon OpenExplorer Toolchain on your x86_64 Ubuntu host machine (Docker environment):
```bash
# Pull official Horizon OpenExplorer docker image
docker pull openexplorer/ai_toolchain_ubuntu_20_bayes:latest

# Launch container mounting the project directory
docker run -it --rm \
  -v $(pwd):/workspace \
  openexplorer/ai_toolchain_ubuntu_20_bayes:latest \
  /bin/bash
```

---

## 3. ONNX Preparation for BPU
In your Google Colab training notebook:
```python
from ultralytics import YOLO

# Load best checkpoint
model = YOLO("runs/detect/koe_green_jacket_yolov8n/weights/best.pt")

# Export to ONNX with static input dimensions (640x640)
model.export(
    format="onnx",
    imgsz=640,
    opset=11,
    simplify=True
)
```

Transfer `best.onnx` to the host compilation directory.

---

## 4. Post-Training Quantization (PTQ)
1. **Prepare Calibration Data:**  
   Extract 100 to 150 images from the Roboflow validation set and place them in `./calibration_dataset`.
2. **Execute Verification:**
   ```bash
   hb_mapper checker \
     --model-type onnx \
     --march bayes-e \
     --model best.onnx
   ```
3. **Build BPU Binary:**
   ```bash
   hb_mapper makertbin \
     --model-type onnx \
     --march bayes-e \
     --model best.onnx \
     --config configs/rdkx5_bpu_quant.yaml
   ```
   This generates `koe_green_jacket_yolov8n.bin`.

---

## 5. Deployment on RDK X5 Board
Transfer `koe_green_jacket_yolov8n.bin` to the RDK X5 board via SCP:
```bash
scp koe_green_jacket_yolov8n.bin sunrise@<RDK_X5_IP>:~/models/
```

### Run Benchmarking:
```bash
# Benchmark raw BPU inference latency and FPS
hb_perf ~/models/koe_green_jacket_yolov8n.bin
```

### Launch Real-Time Webcam Application:
Connect a standard USB webcam to the USB 3.0 port:
```bash
python3 scripts/webcam_inference_demo.py \
  --model ~/models/koe_green_jacket_yolov8n.bin \
  --device /dev/video0 \
  --conf 0.50 \
  --iou 0.45
```
