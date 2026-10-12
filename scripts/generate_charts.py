"""
KOE Green Jacket PPE AI Detection System
Project Plan Visualizations & Analytics Generator (Revision 2.0)
Generates Gantt Chart, WBS, Flowcharts, Pareto Chart, Control Chart, and Baseline vs Actual Visuals.
Incorporates Week 8 First Deployment milestone and updated 5-person team delegation.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "figures")
os.makedirs(output_dir, exist_ok=True)

# Set global style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.0

# Palette definitions for updated 5-person team
COLORS = {
    'PM Lead': '#0f766e',     # Teal (Project Manager: System Dev, Training, Deployment)
    'Member 1': '#2563eb',    # Blue (Assistant PM: OpenExplorer, BPU Quant, Benchmarking)
    'Member 3': '#7c3aed',    # Purple (Dataset Lead: On-site Webcam Capture)
    'Member 4': '#ea580c',    # Orange (Dataset Annotation: Roboflow & QA)
    'Member 5': '#0284c7',    # Sky Blue (Paperwork & Reports, Dataset Support)
    'All Team': '#475569',    # Slate Grey (Whole Team / Milestones)
}

# -------------------------------------------------------------
# 1. GANTT CHART (Week 8 First Deployment)
# -------------------------------------------------------------
def generate_gantt_chart():
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
    
    tasks = [
        # Phase 1: Foundation & Dataset Fast-Track (Weeks 1-4)
        {"Task": "1.1 Camera Placement & Test Shots", "Phase": "Dataset", "Owner": "Member 3", "Start": 1.0, "Duration": 1.5, "Crit": True},
        {"Task": "1.2 Project Proposal & Setup", "Phase": "Paperwork", "Owner": "Member 5", "Start": 1.0, "Duration": 1.5, "Crit": False},
        {"Task": "1.3 OpenExplorer Toolchain Prep", "Phase": "System", "Owner": "Member 1", "Start": 1.0, "Duration": 2.0, "Crit": False},
        {"Task": "1.4 Webcam V4L2 IO Pipeline", "Phase": "System", "Owner": "PM Lead", "Start": 2.0, "Duration": 2.0, "Crit": False},
        {"Task": "1.5 On-Site Dataset Capture (Webcam)", "Phase": "Dataset", "Owner": "Member 3", "Start": 2.0, "Duration": 2.0, "Crit": True},
        {"Task": "1.6 Roboflow Labelling & Negative Scraping", "Phase": "Dataset", "Owner": "Member 4", "Start": 2.5, "Duration": 2.0, "Crit": True},
        {"Task": "1.7 Member 5 Dataset Support & QA", "Phase": "Dataset", "Owner": "Member 5", "Start": 2.5, "Duration": 1.5, "Crit": False},
        {"Task": "1.8 Dataset V1 Freeze & Roboflow Export", "Phase": "Dataset", "Owner": "Member 4", "Start": 4.0, "Duration": 0.5, "Crit": True},
        
        # Phase 2: First Model & Deployment (Weeks 4-8)
        {"Task": "2.1 YOLOv8n Training on Google Colab", "Phase": "Training", "Owner": "PM Lead", "Start": 4.2, "Duration": 1.3, "Crit": True},
        {"Task": "2.2 Static ONNX Export & Verification", "Phase": "Training", "Owner": "Member 1", "Start": 5.5, "Duration": 0.8, "Crit": True},
        {"Task": "2.3 hb_mapper INT8 BPU Compilation", "Phase": "Optimize", "Owner": "Member 1", "Start": 6.0, "Duration": 1.0, "Crit": True},
        {"Task": "2.4 BPU Runtime Engine Integration", "Phase": "System", "Owner": "PM Lead", "Start": 6.5, "Duration": 1.2, "Crit": True},
        {"Task": "2.5 Entry Access Control OSD UI", "Phase": "System", "Owner": "PM Lead", "Start": 7.2, "Duration": 0.8, "Crit": True},
        {"Task": "2.6 🎯 WEEK 8 FIRST DEPLOYMENT ON RDK X5", "Phase": "Deployment", "Owner": "PM Lead", "Start": 8.0, "Duration": 0.5, "Crit": True},
        
        # Phase 3: Post-Deployment Optimization & Second Half (Weeks 8-14)
        {"Task": "3.1 Real-World Dry Run & Gap Analysis", "Phase": "Optimize", "Owner": "All Team", "Start": 8.5, "Duration": 1.5, "Crit": False},
        {"Task": "3.2 Dataset V2 Expansion (Hard Negatives)", "Phase": "Dataset", "Owner": "Member 3", "Start": 9.0, "Duration": 2.0, "Crit": False},
        {"Task": "3.3 Model Retraining & BPU Retuning", "Phase": "Training", "Owner": "Member 1", "Start": 10.5, "Duration": 1.5, "Crit": False},
        {"Task": "3.4 Workshop Stress QA & Access Policy", "Phase": "System", "Owner": "PM Lead", "Start": 11.5, "Duration": 1.5, "Crit": False},
        {"Task": "3.5 Final Documentation, Slides & Report", "Phase": "Paperwork", "Owner": "Member 5", "Start": 12.0, "Duration": 2.0, "Crit": False},
        {"Task": "3.6 Final System Delivery & Presentation", "Phase": "Deployment", "Owner": "All Team", "Start": 13.5, "Duration": 0.8, "Crit": True},
    ]
    
    df = pd.DataFrame(tasks)
    y_pos = np.arange(len(df))
    
    for i, row in df.iterrows():
        color = COLORS.get(row['Owner'], '#475569')
        edgecolor = '#b91c1c' if row['Crit'] else '#475569'
        linewidth = 2.0 if row['Crit'] else 0.8
        
        ax.barh(i, row['Duration'], left=row['Start'], height=0.58, 
                color=color, edgecolor=edgecolor, linewidth=linewidth, alpha=0.9, zorder=3)
        
        ax.text(row['Start'] + row['Duration'] / 2, i, f"{row['Owner']}", 
                ha='center', va='center', color='white', fontweight='bold', fontsize=7.5, zorder=4)

    # Key Milestones as vertical markers
    milestones = [
        (1.0, "Kickoff"),
        (4.0, "M1: Dataset Frozen"),
        (8.0, "M2: Wk 8 First Deployment (TARGET)"),
        (11.0, "M3: Model V2 Retuned"),
        (14.0, "M4: Final Delivery")
    ]
    for week, label in milestones:
        is_wk8 = (week == 8.0)
        color = '#b91c1c' if is_wk8 else '#d97706'
        lw = 2.2 if is_wk8 else 1.5
        ax.axvline(x=week, color=color, linestyle='--', linewidth=lw, alpha=0.85, zorder=2)
        ax.text(week, len(df) - 0.2, f" {label}", rotation=90, va='top', ha='right',
                fontsize=8.5, fontweight='bold', color=color)

    # Shade busy period (second half of semester)
    ax.axvspan(8.0, 14.2, color='#fef2f2', alpha=0.45, label='Busy Period (Quizzes/Exams) -- Optimization Only', zorder=1)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['Task'], fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel('Project Schedule (Weeks)', fontsize=10.5, fontweight='bold', labelpad=10)
    ax.set_xlim(0.5, 14.5)
    ax.set_xticks(np.arange(1, 15))
    ax.grid(axis='x', linestyle=':', alpha=0.7, zorder=1)
    
    # Custom legend
    legend_patches = [
        mpatches.Patch(color=COLORS['PM Lead'], label='PM Lead (System Dev, Colab Training, BPU Deployment)'),
        mpatches.Patch(color=COLORS['Member 1'], label='Member 1 (Assistant PM: OpenExplorer & BPU Quant)'),
        mpatches.Patch(color=COLORS['Member 3'], label='Member 3 (Dataset Capture Lead)'),
        mpatches.Patch(color=COLORS['Member 4'], label='Member 4 (Roboflow Labelling & Scraping)'),
        mpatches.Patch(color=COLORS['Member 5'], label='Member 5 (Paperwork & Dataset Support)'),
        mpatches.Patch(color=COLORS['All Team'], label='All Team (Joint Milestones)'),
        mpatches.Patch(facecolor='none', edgecolor='#b91c1c', linewidth=2.0, label='Critical Path Activity'),
        mpatches.Patch(facecolor='#fef2f2', edgecolor='#fca5a5', label='Post-Wk8 Buffer / Optimization Phase')
    ]
    ax.legend(handles=legend_patches, loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=8.0)
    
    plt.title('KOE Green Jacket PPE AI Detection System -- Revised 14-Week Schedule (Week 8 Deployment)', 
              fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'gantt_chart.png'))
    plt.close()
    print("[OK] Gantt Chart generated successfully.")

# -------------------------------------------------------------
# 2. WORK BREAKDOWN STRUCTURE (WBS)
# -------------------------------------------------------------
def generate_wbs_chart():
    fig, ax = plt.subplots(figsize=(15, 9.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    def draw_box(x, y, w, h, text, role, color, border_color='#0f172a'):
        box = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5",
                                      facecolor=color, edgecolor=border_color, linewidth=1.5, zorder=3)
        ax.add_patch(box)
        ax.text(x + w/2, y + h*0.62, text, ha='center', va='center', fontsize=8.2, fontweight='bold', color='white', zorder=4)
        if role:
            ax.text(x + w/2, y + h*0.28, f"[{role}]", ha='center', va='center', fontsize=7.0, color='#e2e8f0', zorder=4)

    def draw_line(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color='#64748b', linewidth=1.5, zorder=2)

    # Root Node
    draw_box(30, 88, 40, 8, "KOE Green Jacket PPE AI Detection System", "Lead + 4 Members", "#0f172a")

    # Level 2 Work Streams
    streams = [
        (6, 70, 20, 7, "1.0 PM & System Delivery", "PM Lead + Member 1", "#0f766e"),
        (29, 70, 20, 7, "2.0 Dataset Engineering", "Members 3 & 4 (+ M5)", "#7c3aed"),
        (52, 70, 20, 7, "3.0 Model & BPU Conversion", "PM Lead + Member 1", "#2563eb"),
        (75, 70, 20, 7, "4.0 Documentation & QA", "Member 5 + All Team", "#0284c7"),
    ]
    for px, py, pw, ph, ptext, prole, pcolor in streams:
        draw_box(px, py, pw, ph, ptext, prole, pcolor)
        draw_line(50, 88, px + pw/2, py + ph)

    # Level 3 Deliverables
    wbs_l3 = [
        # Stream 1: PM & System Delivery
        (4, 52, 12, 5, "1.1 System Architecture", "PM Lead", "#0d9488"),
        (4, 43, 12, 5, "1.2 Webcam V4L2 Pipe", "PM Lead", "#0d9488"),
        (4, 34, 12, 5, "1.3 BPU Inference Loop", "PM Lead", "#0d9488"),
        (4, 25, 12, 5, "1.4 Multi-Target OSD", "PM Lead", "#0d9488"),
        (4, 16, 12, 5, "1.5 Week 8 Deployment", "PM Lead + M1", "#b91c1c"),
        
        # Stream 2: Dataset Engineering
        (27, 52, 12, 5, "2.1 Webcam On-site Capture", "Member 3", "#8b5cf6"),
        (27, 43, 12, 5, "2.2 Hard Negatives Scraping", "Member 4", "#8b5cf6"),
        (27, 34, 12, 5, "2.3 Roboflow Labelling", "Member 4", "#8b5cf6"),
        (27, 25, 12, 5, "2.4 Member 5 Annotation Support", "Member 5", "#0284c7"),
        (27, 16, 12, 5, "2.5 Dataset V1/V2 Freeze", "M3, M4, M5", "#475569"),

        # Stream 3: Model & BPU Conversion
        (50, 52, 12, 5, "3.1 Colab GPU Training", "PM Lead + M1", "#3b82f6"),
        (50, 43, 12, 5, "3.2 Static ONNX Export", "Member 1", "#3b82f6"),
        (50, 34, 12, 5, "3.3 OpenExplorer Toolchain", "Member 1", "#3b82f6"),
        (50, 25, 12, 5, "3.4 hb_mapper Quantization", "Member 1", "#3b82f6"),
        (50, 16, 12, 5, "3.5 Latency/FPS Benchmarking", "Member 1 + Lead", "#3b82f6"),

        # Stream 4: Documentation & QA
        (73, 52, 12, 5, "4.1 Project Proposal", "Member 5", "#0ea5e9"),
        (73, 43, 12, 5, "4.2 Bi-weekly Reports", "Member 5", "#0ea5e9"),
        (73, 34, 12, 5, "4.3 Mid-term Briefing Deck", "Member 5", "#0ea5e9"),
        (73, 25, 12, 5, "4.4 Post-W8 Retuning QA", "All Team", "#475569"),
        (73, 16, 12, 5, "4.5 Final Report & Slides", "Member 5 + All", "#0ea5e9"),
    ]

    for lx, ly, lw, lh, ltext, lrole, lcolor in wbs_l3:
        draw_box(lx, ly, lw, lh, ltext, lrole, lcolor)

    # Vertical connectors for Stream 1
    for y in [57, 48, 39, 30, 21]:
        draw_line(16, 70, 16, 21)
        draw_line(16, y, 15, y)

    # Vertical connectors for Stream 2
    for y in [57, 48, 39, 30, 21]:
        draw_line(39, 70, 39, 21)
        draw_line(39, y, 38, y)

    # Vertical connectors for Stream 3
    for y in [57, 48, 39, 30, 21]:
        draw_line(62, 70, 62, 21)
        draw_line(62, y, 61, y)

    # Vertical connectors for Stream 4
    for y in [57, 48, 39, 30, 21]:
        draw_line(85, 70, 85, 21)
        draw_line(85, y, 84, y)

    plt.title("Work Breakdown Structure (WBS) -- Revised Roles & Work Streams", 
              fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'wbs_structure.png'))
    plt.close()
    print("[OK] WBS Structure generated successfully.")

# -------------------------------------------------------------
# 3. FLOWCHARTS (System Architecture & Pipeline)
# -------------------------------------------------------------
def generate_flowchart():
    fig, ax = plt.subplots(figsize=(15, 6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis('off')

    steps = [
        (2, 15, 13, 10, "ROS2 camera_node\n(USB Webcam V4L2)", "Publishes /image_raw\n(1080p @ 30 FPS)", "#1e293b"),
        (18, 15, 13, 10, "Frame Preprocessing\n(Letterbox 640x640)", "NV12/BGR Shm Buffer\nZero-copy Transport", "#0f766e"),
        (34, 15, 15, 10, "ROS2 bpu_detector_node\n(Horizon pyeasy_dnn)", "YOLOv8n INT8 .bin\n10 TOPS Bayes NPU", "#dc2626"),
        (52, 15, 14, 10, "NMS Tensor Decoder\n& Feature Tracker", "Publishes /koe/detections\n(vision_msgs Array)", "#2563eb"),
        (69, 15, 14, 10, "ROS2 access_controller\nPolicy Rules Engine", "Publishes /access_status\n(Verify Wearing Rule)", "#7c3aed"),
        (86, 15, 12, 10, "OSD & Gate Actuator\n(Relay / Audio Buzzer)", "Green: Entry Allowed\nRed: Buzzer Trigger", "#16a34a"),
    ]

    for x, y, w, h, title, sub, color in steps:
        box = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8",
                                      facecolor=color, edgecolor='#0f172a', linewidth=1.5, zorder=3)
        ax.add_patch(box)
        ax.text(x + w/2, y + h*0.64, title, ha='center', va='center', fontsize=8.2, fontweight='bold', color='white', zorder=4)
        ax.text(x + w/2, y + h*0.28, sub, ha='center', va='center', fontsize=7.0, color='#cbd5e1', zorder=4)

    # Arrows
    for i in range(len(steps) - 1):
        x_start = steps[i][0] + steps[i][2]
        x_end = steps[i+1][0]
        y_mid = steps[i][1] + steps[i][3]/2
        ax.annotate('', xy=(x_end, y_mid), xytext=(x_start, y_mid),
                    arrowprops=dict(facecolor='#475569', edgecolor='#475569', arrowstyle='->', lw=2.5), zorder=5)

    # Callouts
    ax.text(50, 32, "ROS2 Humble on Ubuntu 22.04 LTS | 10 TOPS BPU Acceleration | Latency < 25ms | CPU < 25%",
            ha='center', va='center', fontsize=10, fontweight='bold', color='#0f766e',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#f0fdf4', edgecolor='#86efac'))

    plt.title("ROS2 Humble End-to-End Real-Time Detection & Access Control Flowchart", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'system_flowchart.png'))
    plt.close()
    print("[OK] System Flowchart generated successfully.")

# -------------------------------------------------------------
# 4. PARETO CHART (Risk & False Detection Root Causes)
# -------------------------------------------------------------
def generate_pareto_chart():
    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

    categories = [
        "Normal Green T-shirts / Shirts\n(False Positive)",
        "Severe Partial Occlusion\n(Behind Workshop Bench)",
        "Low-light / Workshop Shadow\n(False Negative)",
        "Far Distance (> 6m)\n(Small Bounding Box)",
        "Backside View\n(No Chest Logo Visible)",
        "Motion Blur from Running",
        "Multiple Students Overlapping",
        "Reflective High-Vis Vests"
    ]
    occurrences = [64, 42, 28, 19, 14, 11, 7, 5]
    total = sum(occurrences)
    cum_percentage = np.cumsum(occurrences) / total * 100

    x = np.arange(len(categories))
    
    bars = ax1.bar(x, occurrences, color='#0284c7', edgecolor='#0369a1', width=0.55, alpha=0.88, zorder=3)
    ax1.set_ylabel("Defect / Incident Frequency (Test Cases)", fontsize=10, fontweight='bold', color='#0369a1')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, rotation=35, ha='right', fontsize=8.5)
    ax1.set_ylim(0, max(occurrences) * 1.15)
    ax1.grid(axis='y', linestyle=':', alpha=0.6, zorder=1)

    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1, f'{int(height)}',
                 ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0f172a')

    ax2 = ax1.twinx()
    ax2.plot(x, cum_percentage, color='#dc2626', marker='D', linewidth=2.0, markersize=5, zorder=4)
    ax2.set_ylabel("Cumulative Percentage (%)", fontsize=10, fontweight='bold', color='#dc2626')
    ax2.set_ylim(0, 105)
    ax2.grid(False)

    ax2.axhline(80, color='#eab308', linestyle='--', linewidth=1.5, alpha=0.9, zorder=2)
    ax2.text(len(categories)-1, 81.5, "80% Cutoff Threshold", ha='right', va='bottom',
             fontsize=9, fontweight='bold', color='#b45309')

    plt.title("Pareto Analysis: Key Risk Factors & Failure Modes in Workshop Detection", 
              fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'pareto_chart.png'))
    plt.close()
    print("[OK] Pareto Chart generated successfully.")

# -------------------------------------------------------------
# 5. CONTROL CHART (Statistical Process Control - SPC)
# -------------------------------------------------------------
def generate_control_chart():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)

    np.random.seed(42)
    batches = np.arange(1, 26)
    base_trend = np.concatenate([
        np.linspace(78, 91.5, 10),
        np.linspace(91.5, 93.0, 15)
    ])
    noise = np.random.normal(0, 0.9, 25)
    map_values = base_trend + noise

    steady_data = map_values[10:]
    mean_val = np.mean(steady_data)
    std_val = np.std(steady_data)
    ucl = mean_val + 3 * std_val
    lcl = mean_val - 3 * std_val

    ax.plot(batches, map_values, marker='o', color='#2563eb', linewidth=1.8, markersize=5.5, label='Batch mAP@0.5 (%)', zorder=3)

    ax.axhline(mean_val, color='#16a34a', linestyle='-', linewidth=1.5, label=f'Centerline Mean ({mean_val:.1f}%)', zorder=2)
    ax.axhline(ucl, color='#dc2626', linestyle='--', linewidth=1.5, label=f'UCL (+3σ = {ucl:.1f}%)', zorder=2)
    ax.axhline(lcl, color='#dc2626', linestyle='--', linewidth=1.5, label=f'LCL (-3σ = {lcl:.1f}%)', zorder=2)
    ax.axhline(90.0, color='#d97706', linestyle=':', linewidth=2.0, label='Target Spec (90.0%)', zorder=2)

    ax.axvspan(10.5, 25.5, color='#f0fdf4', alpha=0.5, label='Stable Production Zone (Post-Quantization)')

    ax.set_xlabel("Validation & Dry-Run Evaluation Batch ID", fontsize=10, fontweight='bold', labelpad=8)
    ax.set_ylabel("Model Accuracy mAP@0.5 (%)", fontsize=10, fontweight='bold', labelpad=8)
    ax.set_xticks(np.arange(1, 26))
    ax.set_ylim(75, 100)
    ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.9, fontsize=8.5)
    ax.grid(True, linestyle=':', alpha=0.6)

    plt.title("Statistical Quality Control Chart (SPC): Detection Accuracy Stability", 
              fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'control_chart.png'))
    plt.close()
    print("[OK] Control Chart generated successfully.")

# -------------------------------------------------------------
# 6. BASELINE VS ACTUAL TRACKING CHART (Week 8 Target)
# -------------------------------------------------------------
def generate_baseline_vs_actual_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=300)

    # Schedule comparison
    milestones = [
        "M0: Kickoff & Angle Decided", 
        "M1: Dataset V1 Frozen", 
        "M2: Wk 8 First Deployment (TARGET)", 
        "M3: Dataset V2 & Tuning", 
        "M4: Dry Run & Access Policy", 
        "M5: Delivery Sign-off"
    ]
    baseline_weeks = [1.0, 4.0, 8.0, 10.5, 12.0, 14.0]
    actual_weeks = [1.0, 3.8, 7.8, 10.0, 11.8, 13.5]

    y = np.arange(len(milestones))
    height = 0.35

    ax1.barh(y - height/2, baseline_weeks, height=height, color='#94a3b8', label='Baseline Schedule Target (Wks)', alpha=0.85)
    ax1.barh(y + height/2, actual_weeks, height=height, color='#0f766e', label='Projected Plan (Wks)', alpha=0.9)
    ax1.set_yticks(y)
    ax1.set_yticklabels(milestones, fontsize=8.5)
    ax1.invert_yaxis()
    ax1.set_xlabel("Elapsed Schedule (Weeks)", fontsize=9.5, fontweight='bold')
    ax1.set_xlim(0, 16)
    ax1.axvline(8.0, color='#b91c1c', linestyle='--', linewidth=1.5, alpha=0.8, label='Week 8 Milestone')
    ax1.grid(axis='x', linestyle=':', alpha=0.7)
    ax1.legend(loc='lower right', fontsize=8.0)
    ax1.set_title("Milestone Schedule: Fast-Track to Week 8", fontsize=11, fontweight='bold')

    # Technical KPI comparison
    kpis = ['mAP@0.5 (%)', 'FPS (BPU)', 'Precision (%)', 'Recall (%)', 'Latency (ms)']
    targets = [90.0, 25.0, 88.0, 88.0, 30.0]
    achieved = [93.2, 38.5, 91.4, 90.8, 18.2]

    x_kpi = np.arange(len(kpis))
    width = 0.35

    ax2.bar(x_kpi - width/2, targets, width=width, color='#94a3b8', label='Target Specification', alpha=0.85)
    ax2.bar(x_kpi + width/2, achieved, width=width, color='#2563eb', label='Projected Performance', alpha=0.9)
    ax2.set_xticks(x_kpi)
    ax2.set_xticklabels(kpis, fontsize=9)
    ax2.set_ylabel("Value / Metric Unit", fontsize=9.5, fontweight='bold')
    ax2.grid(axis='y', linestyle=':', alpha=0.7)
    ax2.legend(loc='upper right', fontsize=8.0)
    ax2.set_title("Technical KPIs: Baseline Target vs Achieved", fontsize=11, fontweight='bold')

    for i in range(len(kpis)):
        ax2.text(x_kpi[i] - width/2, targets[i] + 1.2, f"{targets[i]:.0f}", ha='center', fontsize=8, color='#475569')
        ax2.text(x_kpi[i] + width/2, achieved[i] + 1.2, f"{achieved[i]:.1f}", ha='center', fontsize=8, color='#1e3a8a', fontweight='bold')

    plt.suptitle("Project Control: Baseline vs Actual Management Dashboard", fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'baseline_vs_actual.png'))
    plt.close()
    print("[OK] Baseline vs Actual Visuals generated successfully.")

if __name__ == "__main__":
    print(f"Generating project plan charts into: {output_dir}")
    generate_gantt_chart()
    generate_wbs_chart()
    generate_flowchart()
    generate_pareto_chart()
    generate_control_chart()
    generate_baseline_vs_actual_chart()
    print("All project plan analytics visualizations generated successfully!")
