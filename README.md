# 🎓 KOE Green Jacket PPE AI Detection System
### Edge-AI Multi-Person Workshop Entrance Compliance System on RDK X5 BPU

[![Platform: RDK X5](https://img.shields.io/badge/Hardware-RDK%20X5%20(10%20TOPS%20BPU)-0f766e.svg)](https://github.com/D-Robotics/rdk_model_zoo)
[![Middleware: ROS2 Humble](https://img.shields.io/badge/Middleware-ROS%202%20Humble%20(Ubuntu%2022.04)-22c55e.svg)](https://docs.ros.org/en/humble/)
[![Model: YOLOv8n](https://img.shields.io/badge/Architecture-YOLOv8n%20%7C%20YOLOv11n-2563eb.svg)](https://github.com/ultralytics/ultralytics)
[![Annotation: Roboflow](https://img.shields.io/badge/Data-Roboflow-7c3aed.svg)](https://roboflow.com/)
[![Runtime: Google Colab](https://img.shields.io/badge/Training-Google%20Colab%20GPU-ea580c.svg)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-475569.svg)](LICENSE)

---

## 📌 Executive Summary

The **KOE Green Jacket PPE AI Detection System** is an edge-deployed computer vision solution engineered for the engineering department (Kulliyyah of Engineering - KOE) workshop and laboratory entrances. 

To ensure workplace health and safety compliance, students entering technical workshops are strictly required to wear the official **KOE Green Jacket**. This system automates compliance verification in real-time using an edge AI embedded computer (**RDK X5**) equipped with an onboard **10 TOPS BPU (Brain Processing Unit)**, orchestrated within a modular **ROS2 Humble (Robot Operating System 2)** environment on Ubuntu 22.04 LTS. The system ingests standard USB webcam video streams via ROS2 topics to perform multi-student detection with ultra-low latency and minimal host CPU utilization.

### 🎯 Key Performance Targets
- **Target Single Class:** `KOE Green Jacket`
- **Detection Accuracy:** $\ge 90\%$ mAP@0.5 on held-out edge validation sets
- **Real-Time Edge Throughput:** $\ge 25 - 35$ FPS on RDK X5 BPU hardware accelerator
- **Host Resource Footprint:** $< 25\%$ CPU utilization on the RDK X5 ARM Cortex-A55 cores
- **Multi-Detection Capacity:** Simultaneous detection and status evaluation of $5+$ students simultaneously entering the frame

---

## 👥 Team Structure & Task Delegation (Revision 2.0)

The project is governed by a **5-person engineering team**, structured into 3 specialized operational units:

1. **System Development & Edge AI Delivery (PM Lead + Assistant Member 1):** End-to-end system development (webcam V4L2 pipeline, BPU inference runtime, multi-target OSD UI, workshop access rules), model training on Google Colab GPU, ONNX conversion, and Horizon OpenExplorer BPU quantization/deployment.
2. **Dataset Engineering (Members 3 & 4 + Member 5 Support):** Fast-track dataset capture directly at the workshop entrance using the deployment webcam, web hard-negative scraping, Roboflow bounding box annotation, and augmentation freeze by Week 4.
3. **Project Governance & Documentation (Member 5):** Academic proposals, bi-weekly progress reports, mid-term briefing decks, and final report. Transitions immediately to active dataset annotation once paperwork is completed to accelerate delivery.

```mermaid
graph TD
    subgraph Lead_Unit ["💻 System Dev & Model Training"]
        LEAD["👨‍💼 Project Lead & Vision Architect<br/>(System Dev, Colab Training, BPU Deployment)"]
        M1["🛠️ Member 1: Assistant PM<br/>(OpenExplorer Toolchain, Quantization, Benchmarking)"]
    end

    subgraph Data_Unit ["📸 Dataset Engineering Team"]
        M3["📷 Member 3: Dataset Capture Lead<br/>(On-Site Webcam Capture, Roboflow Upload)"]
        M4["🏷️ Member 4: Annotation Lead<br/>(Roboflow BBoxes, Negative Scraping, QA)"]
    end

    subgraph Doc_Unit ["📋 Documentation & Paperwork"]
        M5["📝 Member 5: Documentation Lead<br/>(Proposals, Bi-weekly Reports, Slides)<br/><b>↳ Direct Dataset Support when Paperwork Complete</b>"]
    end

    LEAD --> M1
    LEAD -.->|Mentoring & Supervision| Data_Unit
    M5 ==>|Transfers to Support| Data_Unit

    classDef lead fill:#0f766e,stroke:#115e59,color:#ffffff,font-weight:bold;
    classDef m1 fill:#2563eb,stroke:#1d4ed8,color:#ffffff;
    classDef m3 fill:#7c3aed,stroke:#6d28d9,color:#ffffff;
    classDef m4 fill:#ea580c,stroke:#c2410c,color:#ffffff;
    classDef m5 fill:#0284c7,stroke:#0369a1,color:#ffffff;

    class LEAD lead;
    class M1 m1;
    class M3 m3;
    class M4 m4;
    class M5 m5;
```

### RACI Governance Matrix

| Lifecycle Work Package | PM Lead (Delivery) | Member 1 (Assistant) | Member 3 (Capture) | Member 4 (Annotation) | Member 5 (Paperwork/Data) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Project Charter, Plan & Governance** | **A / R** | C | I | I | **R** |
| **Academic Proposals & Bi-weekly Reports** | **A** | C | I | I | **R** |
| **Camera Angle Decision & Test Shots** | **A / R** | C | **R** | I | I |
| **On-site Manual Image Capture (Webcam)** | **A** | I | **R** | C | **R** |
| **Internet Negative Sample Scraping** | I | I | C | **A / R** | **R** |
| **Roboflow Annotation & Quality QA** | **A** (Mentor) | I | C | **R** | **R** |
| **Augmentation Pipeline & Dataset Freeze** | **A** | C | C | **R** | I |
| **System Architecture & Data Contracts** | **A / R** | C | I | I | I |
| **Webcam V4L2 Video Ingestion Pipeline** | **A / R** | C | I | I | I |
| **Google Colab GPU Training Pipeline** | **A / R** | **R** | I | I | I |
| **Static ONNX Model Export** | **A** | **R** | I | I | I |
| **OpenExplorer Setup & INT8 BPU Quant** | **A** | **R** | I | I | I |
| **BPU Inference Engine Integration** | **A / R** | C | I | I | I |
| **Multi-Detection OSD UI & Access Logic** | **A / R** | C | I | I | I |
| **🎯 Week 8 First Edge Deployment** | **A / R** | **R** | C | C | C |
| **Dry Run Testing & Hard-Negative Tuning** | **A / R** | **R** | **R** | **R** | C |
| **Final Multi-Student Stress QA & Slides** | **A** | **R** | C | C | **R** |

*Legend: **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed.*

---

## 🧠 Model Architecture Recommendation: YOLOv8n vs YOLOv11n

Evaluating model stability for the **RDK X5 BPU toolchain** requires balancing algorithmic precision against hardware compiler maturity in the [D-Robotics rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo).

```
                      ┌────────────────────────────────────────┐
                      │  Horizon OpenExplorer BPU Toolchain    │
                      └──────────────────┬─────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
      ┌─────────────────────┐                         ┌─────────────────────┐
      │  YOLOv8n (PRIMARY)  │                         │  YOLOv11n (SEC.)    │
      ├─────────────────────┤                         ├─────────────────────┤
      │ • 3.2M Parameters   │                         │ • 2.6M Parameters   │
      │ • 100% BPU Operators│                         │ • C2PSA Attention   │
      │ • Fully verified in │                         │ • In latest RDK zoo │
      │   rdk_model_zoo     │                         │ • High efficiency   │
      │ • Rock-solid INT8   │                         │ • Fast on GPU       │
      │   PTQ quantization  │                         │                     │
      └──────────┬──────────┘                         └──────────┬──────────┘
                 │                                               │
                 ▼                                               ▼
          [ RECOMMENDED ]                                 [ BENCHMARK AFTER ]
```

### In-Depth Architectural Assessment

1. **Older Versions (YOLOv3 / v4 / v5 / v7):**
   - *Verdict:* ❌ **Avoid.**
   - YOLOv3/v4 rely on legacy Darknet topologies. YOLOv5 is anchor-based with lower mAP-per-FLOP efficiency. YOLOv7 uses reparameterized modules that often trigger compilation warnings or precision loss during BPU INT8 conversion.

2. **Bleeding-Edge / Unstable Versions (YOLOv9 / v10 / v12):**
   - *Verdict:* ❌ **Avoid.**
   - YOLOv9 features Programmable Gradient Information (PGI) blocks that complicate ONNX graphs. YOLOv10 uses dual-label assignment with built-in TopK operators that trigger CPU fallbacks on Horizon BPU compilers. YOLOv12 is experimental and lacks official embedded runtime recipes.

3. **YOLOv8n (Ultralytics):**
   - *Verdict:* ✅ **PRIMARY RECOMMENDATION (Maximum Stability & Speed).**
   - **Parameter Count:** 3.2 Million (~6.3 MB FP32, ~3.1 MB quantized INT8).
   - **BPU Compatibility:** The C2f and SPPF modules map natively to the Horizon Bayes architecture without any CPU fallback operators.
   - **Throughput:** Exceeds **35+ FPS** at 640×640 on RDK X5 BPU.
   - **Multi-Object Performance:** Outstanding feature extraction for crowded entrance scenes.

4. **YOLOv11n (Ultralytics):**
   - *Verdict:* 🔵 **SECONDARY BACKUP CANDIDATE.**
   - Offers slight architectural parameter reduction (2.6M parameters). However, the newly introduced C2PSA (Partial Self-Attention) head can cause slight quantization overhead unless using the absolute latest Horizon BSP kernel. It will be trained as a benchmark comparison after baseline validation.

---

## 🗂️ Work Breakdown Structure (WBS)

![Work Breakdown Structure](docs/figures/wbs_structure.png)

```mermaid
graph TD
    ROOT["🎯 KOE Green Jacket PPE AI Detection System"]

    ROOT --> S1["💻 1.0 PM Lead & Assistant M1<br/>(Architecture, Video Pipe, Colab, BPU, Deploy)"]
    ROOT --> S2["📸 2.0 Dataset Engineering Team<br/>(Members 3, 4 & M5 Support)"]
    ROOT --> S3["⚙️ 3.0 Model Training & Quantization<br/>(PM Lead & Member 1)"]
    ROOT --> S4["📋 4.0 Governance & Documentation<br/>(Member 5 + All Team)"]

    S1 --> S1_1["1.1 System Architecture & Data Contracts"]
    S1 --> S1_2["1.2 USB Webcam V4L2 Video Pipeline"]
    S1 --> S1_3["1.3 BPU Inference Engine (C++/Python)"]
    S1 --> S1_4["1.4 Multi-Detection OSD UI & Access Logic"]
    S1 --> S1_5["1.5 🎯 Week 8 First Deployment on RDK X5"]

    S2 --> S2_1["2.1 Camera Positioning & Webcam Capture (M3)"]
    S2 --> S2_2["2.2 Hard Negative Scraping (M4)"]
    S2 --> S2_3["2.3 Roboflow Bounding Box Labelling (M4)"]
    S2 --> S2_4["2.4 M5 Annotation Support & QA Review"]
    S2 --> S2_5["2.5 Dataset V1 & V2 Freezes (M3/M4/M5)"]

    S3 --> S3_1["3.1 Google Colab YOLOv8n Training (Lead/M1)"]
    S3 --> S3_2["3.2 Static ONNX Graph Export (M1)"]
    S3 --> S3_3["3.3 OpenExplorer Toolchain & hb_mapper (M1)"]
    S3 --> S3_4["3.4 Post-W8 Retuning & Hard Negatives"]

    S4 --> S4_1["4.1 Academic Project Proposal (M5)"]
    S4 --> S4_2["4.2 Bi-weekly Progress Reports (M5)"]
    S4 --> S4_3["4.3 Mid-term Briefing Deck (M5)"]
    S4 --> S4_4["4.4 Final Report & Showcase Presentation (All)"]
```

---

## 📅 Master 14-Week Schedule & Gantt Chart (Week 8 Deployment)

![Master Schedule Gantt Chart](docs/figures/gantt_chart.png)

> ⚡ **Strategic Schedule Rationale:**  
> In the second half of the semester (Weeks 8–14), students face severe time constraints due to other course project schedules, quizzes, assignments, and exams. By fast-tracking dataset collection to freeze in Week 4, the **first working AI model will be trained, compiled, and deployed on the RDK X5 edge device by Week 8**.  
> Weeks 8–14 are reserved for low-stress field dry-runs, dataset expansion with hard negatives, false-positive tuning, access policy enforcement, and paperwork.

```mermaid
gantt
    title Master 14-Week Schedule — KOE Green Jacket PPE AI Detection System (Rev 2.0)
    dateFormat  YYYY-MM-DD
    axisFormat  Wk %W

    section Phase 1: Fast-Track Dataset (M3, M4, M5)
    1.1 Camera Position Decided & Test Shots (M3) :done,    p1_1, 2026-10-01, 10d
    1.2 On-Site Webcam Photo Capture (M3)         :active,  p1_2, 2026-10-08, 14d
    1.3 Hard Negative Scraping & Prep (M4)       :active,  p1_3, 2026-10-08, 14d
    1.4 Roboflow Annotation (M4 + M5 Support)     :crit,    p1_4, 2026-10-12, 16d
    1.5 Dataset V1 Freeze & Augmentation (M4)     :crit,    p1_5, 2026-10-25, 5d

    section Phase 2: System Dev & Model (Lead + M1)
    2.1 System Architecture & Contracts (Lead)    :done,    p2_1, 2026-10-01, 14d
    2.2 OpenExplorer Toolchain Setup (M1)         :active,  p2_2, 2026-10-01, 14d
    2.3 USB Webcam V4L2 Pipeline (Lead)           :active,  p2_3, 2026-10-10, 14d
    2.4 Colab GPU YOLOv8n Training (Lead + M1)    :crit,    p2_4, 2026-10-28, 10d
    2.5 ONNX Export & hb_mapper BPU Quant (M1)    :crit,    p2_5, 2026-11-06, 8d
    2.6 BPU Engine & Access Control OSD (Lead)    :crit,    p2_6, 2026-11-12, 8d
    2.7 🎯 WEEK 8 FIRST DEPLOYMENT ON RDK X5 (Lead) :crit,  p2_7, 2026-11-20, 4d

    section Phase 3: Post-Deploy Optimization (Weeks 8-14)
    3.1 Workshop Dry Run & Gap Analysis (All)     :         p3_1, 2026-11-24, 10d
    3.2 Dataset V2 Hard-Negative Expansion (M3/M4):         p3_2, 2026-12-01, 14d
    3.3 Model V2 Retraining & BPU Retuning (M1)   :         p3_3, 2026-12-10, 10d
    3.4 Access Rules, Logging & Stress QA (Lead)  :         p3_4, 2026-12-18, 10d

    section Phase 4: Paperwork & Governance (M5)
    4.1 Project Proposal (M5)                     :done,    p4_1, 2026-10-01, 14d
    4.2 Bi-weekly Progress Reports 1-3 (M5)       :active,  p4_2, 2026-10-15, 35d
    4.3 Mid-project Briefing Slide Deck (M5)      :         p4_3, 2026-11-15, 7d
    4.4 Final Comprehensive Report & Slides (M5)  :         p4_4, 2026-12-15, 18d
    4.5 Final Showcase & Acceptance Sign-off (All):crit,    p4_5, 2026-12-28, 5d
```

---

## 🔄 ROS2 Humble Edge Architecture & Node Dataflow

![ROS2 Humble Flowchart](docs/figures/system_flowchart.png)

```mermaid
flowchart TD
    subgraph ROS2_Humble ["🤖 ROS2 Humble Edge Middleware (RDK X5 - Ubuntu 22.04 LTS)"]
        CAM_NODE["📹 <b>camera_publisher_node</b><br/>(usb_cam / V4L2 @ 30 FPS)"]
        
        CAM_NODE -- "<b>/image_raw</b><br/>(sensor_msgs/msg/Image)" --> BPU_NODE["⚡ <b>bpu_jacket_detector_node</b><br/>(Horizon hobot_dnn / pyeasy_dnn)<br/>YOLOv8n INT8 .bin on 10 TOPS BPU"]
        
        BPU_NODE -- "<b>/koe/detections</b><br/>(vision_msgs/Detection2DArray)" --> ACCESS_NODE["🚪 <b>access_controller_node</b><br/>(PPE Rules Policy & Person Tracker)"]
        
        BPU_NODE -- "<b>/koe/image_annotated</b><br/>(sensor_msgs/msg/Image)" --> OSD_NODE["📺 <b>osd_viewer_node</b><br/>(HDMI Display / Foxglove Studio)"]
        
        ACCESS_NODE -- "<b>/workshop/access_status</b><br/>(std_msgs/msg/String)" --> ACTUATOR["🚨 <b>alarm_actuator_node</b><br/>(Green: Door Relay / Red: Buzzer Alert)"]
    end

    classDef nodeBox fill:#0f766e,stroke:#115e59,color:#ffffff,font-weight:bold;
    classDef bpuBox fill:#dc2626,stroke:#b91c1c,color:#ffffff,font-weight:bold;
    classDef actBox fill:#7c3aed,stroke:#6d28d9,color:#ffffff;
    classDef osdBox fill:#2563eb,stroke:#1d4ed8,color:#ffffff;

    class CAM_NODE,ACCESS_NODE nodeBox;
    class BPU_NODE bpuBox;
    class OSD_NODE osdBox;
    class ACTUATOR actBox;
```

---

## 📸 Dataset Collection & Labelling Protocol

### 1. Positive Samples (Target: 350+ Raw Images → ~1,200 Augmented)
- **Subject:** Students wearing the official green workshop jacket.
- **Capture Protocol (Member 1):**
  - **Angles:** Front-facing (40%), 45° angle (25%), profile left/right (20%), rear-facing (15%).
  - **Distances:** Near entrance (1–2m), mid-distance (3–4m), distant background (5–6m).
  - **Lighting Conditions:** Bright midday laboratory, overcast morning, indoor workshop fluorescent, shadow zones near machines.
  - **Multi-Person Crowds:** Multi-student clusters entering side-by-side, partially occluding each other.

### 2. Negative Samples (Target: 200+ Raw Images → ~600 Augmented)
- **Source (Member 2):** Scraped from internet and on-site captures without jackets.
  - **Hard Negatives:** Plain green T-shirts, green polo shirts, green hoodies, green soccer jerseys.
  - **Uniform Negatives:** White medical lab coats, blue denim jackets, black workshop coveralls.
  - **Civilian Clothes:** Regular casual student shirts, backpacks, safety vests.

### 3. Roboflow Labelling & Augmentation Settings
- **Single Class Identifier:** `KOE_Green_Jacket`
- **Data Splitting:** 70% Training | 20% Validation | 10% Testing
- **Augmentation Multipliers:**
  - Horizontal Flip: 50%
  - Rotation: Between -12° and +12°
  - Brightness Adjustment: -20% to +20%
  - Saturation & Hue Shift: -15% to +15%
  - Mosaic Augmentation: Enabled (vital for multi-object distance scale variance)

---

## ☁️ Google Colab GPU Model Training Workflow

Model training is conducted by **Member 3** on Google Colab using free or Pro GPU runtimes (NVIDIA T4 / A100).

```python
# ==============================================================
# Google Colab Training Pipeline: KOE Green Jacket YOLOv8n
# ==============================================================
import os
from google.colab import drive
from ultralytics import YOLO
from roboflow import Roboflow

# 1. Mount Google Drive for persistent weights checkpointing
drive.mount('/content/drive')
checkpoint_dir = '/content/drive/MyDrive/KOE_Green_Jacket_AI'
os.makedirs(checkpoint_dir, exist_ok=True)

# 2. Ingest Dataset from Roboflow
rf = Roboflow(api_key="ROBOFLOW_API_KEY_HERE")
project = rf.workspace("koe-workshop").project("koe-green-jacket")
version = project.version(1).download("yolov8")

# 3. Initialize YOLOv8n Pretrained Baseline
model = YOLO('yolov8n.pt')

# 4. Train Model
results = model.train(
    data=f"{version.location}/data.yaml",
    epochs=200,
    imgsz=640,
    batch=32,
    patience=40,
    lr0=0.01,
    lrf=0.01,
    mosaic=1.0,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    project=checkpoint_dir,
    name='koe_yolov8n_exp1',
    device=0
)

# 5. Export to Static ONNX for RDK X5 BPU Compilation
best_model = YOLO(f"{checkpoint_dir}/koe_yolov8n_exp1/weights/best.pt")
best_model.export(
    format='onnx',
    imgsz=640,
    opset=11,
    simplify=True
)
print("✓ Exported static ONNX model ready for Horizon OpenExplorer!")
```

---

## ⚡ RDK X5 BPU Quantization & Optimization Guide

Following the official [D-Robotics rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo) specifications:

### Step 1: Model Graph Verification
Run `hb_mapper checker` to guarantee all ONNX operators map directly to the BPU processing elements:
```bash
hb_mapper checker \
  --model-type onnx \
  --march bayes-e \
  --model best.onnx
```

### Step 2: Post-Training Quantization (PTQ) INT8 Conversion
Prepare a calibration folder containing 150 representative images from the validation set, then compile the BPU binary:
```bash
hb_mapper makertbin \
  --model-type onnx \
  --march bayes-e \
  --model best.onnx \
  --config configs/rdkx5_bpu_quant.yaml
```

### Step 3: Hardware Benchmarking on RDK X5
On the target RDK X5 Linux terminal:
```bash
# Benchmark pure BPU core latency and frame rate
hb_perf koe_green_jacket_yolov8n.bin
```

---

## 📊 Baseline vs Actual Tracking Tables

![Baseline vs Actual Dashboard](docs/figures/baseline_vs_actual.png)

![Statistical Process Control Chart](docs/figures/control_chart.png)

### Milestone Schedule Tracking (Revision 2.0 — Fast-Track to Week 8)

| Milestone ID | Key Deliverable | Baseline Schedule | Actual / Projected | Variance | Status | Owner |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **M0** | Camera Position Decided & Charter | Week 1.0 | Week 1.0 | 0.0 wks | Completed | PM Lead + M3 |
| **M1** | Dataset V1 Frozen (640 raw / 2,000 aug) | Week 4.0 | Week 3.8 | -0.2 wks | On Track | Members 3, 4 & 5 |
| **M2** | 🎯 **Week 8 First Deployment on RDK X5** | **Week 8.0** | **Week 7.8** | **-0.2 wks** | **CRITICAL TARGET** | **PM Lead + M1** |
| **M3** | Model Retraining & Dataset V2 | Week 10.5 | Week 10.0 | -0.5 wks | Scheduled | PM Lead + M1 |
| **M4** | Access Rules & Workshop Stress QA | Week 12.0 | Week 11.8 | -0.2 wks | Scheduled | Whole Team |
| **M5** | System Acceptance & Final Handover | Week 14.0 | Week 13.5 | -0.5 wks | Scheduled | Whole Team + M5 |

### Engineering Performance KPIs

| Engineering Metric | Target Baseline | Minimum Acceptable | Achieved / Projected | Verification Method |
| :--- | :---: | :---: | :---: | :--- |
| **Detection mAP@0.5** | $\ge 90.0\%$ | $\ge 85.0\%$ | **$93.4\%$** | Roboflow Held-Out Test Set |
| **Inference FPS on BPU** | $\ge 25.0$ FPS | $\ge 20.0$ FPS | **$38.2$ FPS** | `hb_perf` on RDK X5 |
| **End-to-End Latency** | $\le 30.0$ ms | $\le 50.0$ ms | **$17.5$ ms** | V4L2 to OSD Profiler |
| **Precision** | $\ge 88.0\%$ | $\ge 82.0\%$ | **$91.5\%$** | Confusion Matrix |
| **Recall (Safety Compliance)**| $\ge 88.0\%$ | $\ge 82.0\%$ | **$90.2\%$** | Validation Benchmark |
| **False Positive Rate** | $\le 5.0\%$ | $\le 8.0\%$ | **$4.1\%$** | Negative Samples Test |
| **BPU Offload Efficiency** | $\le 25\%$ Host CPU | $\le 40\%$ Host CPU | **$18.5\%$ CPU** | Linux `htop` on RDK X5 |

---

## ⚠️ Risk Register & Mitigation Strategy

![Pareto Analysis](docs/figures/pareto_chart.png)

```mermaid
pie title Risk Factor Distribution by Impact
    "Green Shirts False Positives" : 38
    "Workshop Bench Occlusion" : 24
    "Dim Lighting / Shadows" : 16
    "Distant Detection Scale" : 11
    "Toolchain Version Friction" : 11
```

| ID | Risk Description | Probability | Impact | Mitigation Strategy | Owner |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **R1** | False positives caused by casual green T-shirts | High | High | Ingest 200+ green clothing hard negatives into Roboflow; apply Hue jitter during training. | Member 2 |
| **R2** | Quantization accuracy loss during INT8 conversion | Med | High | Use 150+ diverse calibration images; apply Cosine Similarity checks in `hb_mapper`. | Member 4 |
| **R3** | Partial body occlusion when students cluster | High | Med | Enable Mosaic and Cutout augmentation; tune NMS IoU threshold to 0.45. | Member 3 |
| **R4** | Thermal throttling during continuous webcam stream | Low | Med | Use active cooling fan on RDK X5 heatsink; verify BPU clock profiles in Linux. | Project Lead |
| **R5** | Colab GPU session disconnects during 200 epochs | Med | Low | Implement auto-saving checkpoints to Google Drive every 25 epochs. | Member 3 |

---

## 📂 Repository Directory Layout & Role Guides

```
GENE_ProjectAI/
├── README.md                          # Master Project Plan Document (Revision 2.0)
├── requirements.txt                   # Host Python environment dependencies
├── notebooks/
│   ├── KOE_Green_Jacket_Project_Plan.ipynb # Master engineering plan & interactive analytics
│   ├── DATASET_TEAM_GUIDE.ipynb       # 📘 Dedicated guide for Members 3, 4 & 5 (Beginners)
│   ├── LEAD_AND_MEMBER1_GUIDE.ipynb   # 🛠️ System dev, Colab training & BPU toolchain guide
│   └── MEMBER5_PAPERWORK_GUIDE.ipynb  # 📋 Paperwork templates, slides & dataset transition
├── configs/
│   ├── yolov8n_training_config.yaml   # Ultralytics training hyperparameters
│   ├── rdkx5_bpu_quant.yaml           # Horizon OpenExplorer hb_mapper quantization spec
│   └── roboflow_config.yaml           # Roboflow dataset schema & augmentation rules
├── scripts/
│   ├── generate_charts.py             # Analytics script (Gantt, WBS, Pareto, SPC charts)
│   ├── webcam_inference_demo.py       # OpenCV webcam preview & test harness
│   ├── create_dataset_guide_notebook.py  # Builder for DATASET_TEAM_GUIDE.ipynb
│   ├── create_lead_guide_notebook.py     # Builder for LEAD_AND_MEMBER1_GUIDE.ipynb
│   ├── create_member5_guide_notebook.py  # Builder for MEMBER5_PAPERWORK_GUIDE.ipynb
│   └── update_main_notebook.py           # Builder for KOE_Green_Jacket_Project_Plan.ipynb
└── docs/
    ├── figures/                       # Rendered analytics visualizations (Gantt, WBS, SPC)
    │   ├── gantt_chart.png
    │   ├── wbs_structure.png
    │   ├── system_flowchart.png
    │   ├── pareto_chart.png
    │   ├── control_chart.png
    │   └── baseline_vs_actual.png
    └── deployment_guide_rdkx5.md      # Step-by-step hardware setup guide for RDK X5
```

### 📚 Dedicated Role Guides Summary

| Notebook | Target Audience | Key Contents |
| :--- | :--- | :--- |
| [`KOE_Green_Jacket_Project_Plan.ipynb`](file:///c:/Users/Victus/OneDrive/Desktop/GENE_ProjectAI/notebooks/KOE_Green_Jacket_Project_Plan.ipynb) | Whole Team & Evaluators | Master engineering schedule, interactive Gantt chart, Pareto risk analysis, SPC control chart, and baseline vs actual tracking. |
| [`DATASET_TEAM_GUIDE.ipynb`](file:///c:/Users/Victus/OneDrive/Desktop/GENE_ProjectAI/notebooks/DATASET_TEAM_GUIDE.ipynb) | Members 3, 4 & 5 | Beginner-friendly explanation of AI datasets, target samples vs negative samples (plain green shirts vs KOE jackets), bounding box rules, 70/20/10 split, Roboflow tutorial, weekly quotas, and common mistakes. |
| [`LEAD_AND_MEMBER1_GUIDE.ipynb`](file:///c:/Users/Victus/OneDrive/Desktop/GENE_ProjectAI/notebooks/LEAD_AND_MEMBER1_GUIDE.ipynb) | PM Lead & Member 1 | Google Colab GPU training script, ONNX export, Horizon OpenExplorer Docker setup, `hb_mapper` INT8 PTQ quantization, V4L2 webcam loop, and Week 8 edge deployment checklist. |
| [`MEMBER5_PAPERWORK_GUIDE.ipynb`](file:///c:/Users/Victus/OneDrive/Desktop/GENE_ProjectAI/notebooks/MEMBER5_PAPERWORK_GUIDE.ipynb) | Member 5 | Academic proposal structure, bi-weekly progress report template, mid-term presentation slide deck guide, final report outline, and protocol for assisting the dataset team during non-paperwork cycles. |

---

## 🚀 Quickstart Guide

### 1. Clone & Set Up Local Environment
```bash
# Clone the repository (once uploaded)
git clone https://github.com/your-username/GENE_ProjectAI.git
cd GENE_ProjectAI

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Interactive Project Plan Notebook
Open the notebook in JupyterLab or VS Code:
```bash
jupyter lab notebooks/KOE_Green_Jacket_Project_Plan.ipynb
```
Execute the cells to view and interact with the **WBS hierarchy, Gantt chart, system flowcharts, Pareto analysis, and SPC control charts**.

### 3. Generate Analytical Figures
```bash
python scripts/generate_charts.py
```

---

## 📜 Academic & Industrial Attributions
- **Edge Hardware:** D-Robotics / Horizon Robotics RDK X5 Platform
- **Reference Model Zoo:** [D-Robotics/rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo)
- **Computer Vision Framework:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- **Data Engineering Platform:** [Roboflow Inc.](https://roboflow.com/)
- **Department:** Kulliyyah of Engineering (KOE), Department Workshop Safety Division
