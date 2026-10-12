import json

nb_path = r'c:\Users\Victus\OneDrive\Desktop\GENE_ProjectAI\notebooks\KOE_Green_Jacket_Project_Plan.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# ── Rebuild the entire notebook with updated schedule & team structure ──

header_md = {
 "cell_type": "markdown", "metadata": {}, "source": [
  "# \U0001f393 KOE Green Jacket PPE AI Detection System\n",
  "## \U0001f4cc Master Engineering & Delivery Project Plan Notebook\n",
  "### Revision 2.0 — Updated Schedule & Team Structure\n",
  "\n",
  "---\n",
  "\n",
  "### **Executive Project Information**\n",
  "| Field | Details |\n",
  "| :--- | :--- |\n",
  "| **Project Title** | Edge-AI PPE Compliance Detection for KOE Workshop Entrances |\n",
  "| **Target Class** | `KOE Green Jacket` |\n",
  "| **Edge Platform** | RDK X5 — 10 TOPS BPU (Horizon Robotics Bayes) |\n",
  "| **Vision Sensor** | USB Webcam (720p/1080p @ 30 FPS via OpenCV / V4L2) |\n",
  "| **Middleware & Runtime** | **ROS2 Humble (Ubuntu 22.04 LTS on RDK X5)** |\n",
  "| **Model** | YOLOv8n (primary) · YOLOv11n (secondary benchmark) |\n",
  "| **First Deployment Milestone** | **Week 8** |\n",
  "| **Final Delivery** | **Week 14** |\n",
  "| **Team Size** | 1 PM/Lead + 1 Assistant + 2 Dataset + 1 Paperwork = 5 members |\n",
  "| **Reference** | [D-Robotics rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo) |\n",
 ]
}

model_md = {
 "cell_type": "markdown", "metadata": {}, "source": [
  "## 1. \U0001f9e0 YOLO Model Recommendation\n",
  "\n",
  "| Architecture | BPU Toolchain | Size | Stability | Verdict |\n",
  "| :--- | :--- | :--- | :--- | :--- |\n",
  "| YOLOv3/v4/v5 | Legacy | Large | Outdated | \u274c Avoid |\n",
  "| YOLOv7 | Reparam issues | Medium | Unstable on BPU | \u274c Avoid |\n",
  "| **YOLOv8n** | **100% BPU ops** | **3.2M params** | **Rock solid** | \u2705 **PRIMARY** |\n",
  "| YOLOv9/v10 | CPU fallback ops | Variable | Unstable | \u274c Avoid |\n",
  "| YOLOv11n | Mostly supported | 2.6M params | Good | \U0001f535 Secondary |\n",
  "| YOLOv12+ | Unsupported | Untested | None | \u274c Avoid |\n",
  "\n",
  "> **Decision:** Use `YOLOv8n`. Its C2f/SPPF blocks map 100% to Horizon BPU PEs.  \n",
  "> Scale up to `YOLOv8s` only if mAP falls below 85% after augmentation tuning.\n",
 ]
}

team_md = {
 "cell_type": "markdown", "metadata": {}, "source": [
  "## 2. \U0001f465 Revised Team Structure & Task Delegation\n",
  "\n",
  "### Team Roles (5 Members)\n",
  "\n",
  "| # | Role | Members | Core Responsibilities |\n",
  "| :---: | :--- | :--- | :--- |\n",
  "| 1 | **Project Manager + System Developer** | **PM Lead** | End-to-end delivery, ROS2 Humble edge system development (camera node, BPU detector node, access controller node), Colab AI training, AI model training from prepared dataset, NPU model conversion |\n",
  "| 2 | **Assistant PM** | **Member 1** | Supports PM Lead in system dev tasks, sets up Horizon OpenExplorer toolchain early, handles BPU conversion & benchmarking, assists with Colab training |\n",
  "| 3 | **Dataset Specialist** | **Member 3** | On-site image capture, raw dataset curation, upload to Roboflow |\n",
  "| 4 | **Dataset Specialist** | **Member 4** | On-site image capture, Roboflow bounding box annotation, quality review |\n",
  "| 5 | **Documentation & Support** | **Member 5** | Project proposals, progress reports, presentation slides, final report. Assists Members 3 & 4 on annotation when no paperwork pending |\n",
  "\n",
  "### \u26a0\ufe0f Critical Constraint\n",
  "> **System development is handled exclusively by PM Lead.**  \n",
  "> Member 1 assists with toolchain setup and BPU conversion but does NOT independently develop the inference application.\n",
  "\n",
  "### RACI Matrix\n",
  "\n",
  "| Activity | PM Lead | Member 1 | Member 3 | Member 4 | Member 5 |\n",
  "| :--- | :---: | :---: | :---: | :---: | :---: |\n",
  "| Project Governance & Charter | **A/R** | C | I | I | C |\n",
  "| On-site Image Capture | I | I | **A/R** | R | C |\n",
  "| Roboflow Annotation | C | I | R | **A/R** | C |\n",
  "| Data Augmentation & Export | **A** | C | R | R | I |\n",
  "| Colab Model Training | **A/R** | R | I | I | I |\n",
  "| ONNX Export | **A/R** | C | I | I | I |\n",
  "| System Architecture | **A/R** | C | I | I | I |\n",
  "| BPU Toolchain Setup | **A** | **R** | I | I | I |\n",
  "| hb_mapper INT8 Quantization | **A** | **R** | I | I | I |\n",
  "| Webcam Inference Pipeline | **A/R** | C | I | I | I |\n",
  "| Multi-Detection OSD UI | **A/R** | C | I | I | I |\n",
  "| Week 8 First Deployment | **A/R** | R | I | I | I |\n",
  "| Post-Deploy Optimization | **A/R** | R | C | C | I |\n",
  "| Proposals & Reports | C | I | I | I | **A/R** |\n",
  "| Final Presentation Slides | C | C | I | I | **A/R** |\n",
  "| Final QA & Acceptance | **A** | R | R | R | R |\n",
 ]
}

install_cell = {
 "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
 "source": [
  "# Cell 1: Install Dependencies & Environment Setup\n",
  "import subprocess, sys\n",
  "\n",
  "_pkgs = ['numpy', 'pandas', 'matplotlib', 'seaborn']\n",
  "for _p in _pkgs:\n",
  "    try:\n",
  "        __import__(_p)\n",
  "    except ImportError:\n",
  "        print(f'Installing {_p}...')\n",
  "        subprocess.check_call([sys.executable, '-m', 'pip', 'install', _p, '-q'])\n",
  "\n",
  "import os\n",
  "import numpy as np\n",
  "import pandas as pd\n",
  "import matplotlib.pyplot as plt\n",
  "import matplotlib.patches as mpatches\n",
  "\n",
  "plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')\n",
  "plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']\n",
  "plt.rcParams['axes.edgecolor'] = '#cbd5e1'\n",
  "plt.rcParams['axes.linewidth'] = 1.0\n",
  "\n",
  "ROLE_COLORS = {\n",
  "    'PM Lead + Mbr1': '#0f766e',\n",
  "    'Member 3 (Dataset)': '#2563eb',\n",
  "    'Member 4 (Dataset)': '#7c3aed',\n",
  "    'Member 5 (Docs)': '#ea580c',\n",
  "    'All Team': '#475569'\n",
  "}\n",
  "print('Environment ready.')"
 ]
}

gantt_md = {
 "cell_type": "markdown", "metadata": {}, "source": [
  "## 3. \U0001f4c5 Revised 14-Week Schedule\n",
  "\n",
  "| Phase | Weeks | Goal |\n",
  "| :--- | :---: | :--- |\n",
  "| **Dataset Sprint** | 1 – 4 | 400+ images collected, fully annotated in Roboflow, dataset V1 frozen |\n",
  "| **Training & Conversion** | 4 – 6 | YOLOv8n trained on Colab (mAP ≥ 90%), exported to ONNX, BPU .bin compiled |\n",
  "| **System Dev Phase 1** | 1 – 7 | Webcam pipeline, inference engine, basic OSD UI ready |\n",
  "| **🎯 FIRST DEPLOYMENT** | **Week 8** | Full end-to-end system running on RDK X5 BPU at workshop entrance |\n",
  "| **Optimization Sprint** | 8 – 11 | Dataset expansion, re-training, threshold tuning, edge case fixing |\n",
  "| **System Dev Phase 2** | 9 – 12 | Access control policy, logging, multi-student stress test |\n",
  "| **Final QA & Docs** | 12 – 14 | Acceptance testing, final report, slides, handover |\n",
 ]
}

gantt_cell = {
 "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
 "source": [
  "# Cell 2: Revised 14-Week Gantt Chart — First Deployment at Week 8\n",
  "fig, ax = plt.subplots(figsize=(15, 9), dpi=200)\n",
  "\n",
  "schedule_data = [\n",
  "    # Phase 1: Dataset Sprint (Members 3, 4, 5)\n",
  "    {'Task':'1.1 Camera Placement & Capture Protocol',  'Owner':'All Team',             'Start':1.0,  'Dur':1.0,  'Crit':True},\n",
  "    {'Task':'1.2 On-site KOE Jacket Capture (400+ imgs)','Owner':'Member 3 (Dataset)',  'Start':1.0,  'Dur':3.5,  'Crit':True},\n",
  "    {'Task':'1.3 Internet Negative Sample Scraping',    'Owner':'Member 4 (Dataset)',   'Start':1.0,  'Dur':3.0,  'Crit':False},\n",
  "    {'Task':'1.4 Roboflow Annotation & QA Review',     'Owner':'Member 4 (Dataset)',   'Start':2.0,  'Dur':2.5,  'Crit':True},\n",
  "    {'Task':'1.5 Augmentation & Dataset V1 Freeze',    'Owner':'Member 3 (Dataset)',   'Start':4.0,  'Dur':0.5,  'Crit':True},\n",
  "    # Paperwork (Member 5)\n",
  "    {'Task':'5.1 Project Proposal & Charter Docs',     'Owner':'Member 5 (Docs)',      'Start':1.0,  'Dur':2.0,  'Crit':False},\n",
  "    {'Task':'5.2 Annotation Assist (when free)',       'Owner':'Member 5 (Docs)',      'Start':2.0,  'Dur':2.0,  'Crit':False},\n",
  "    {'Task':'5.3 Progress Reports (bi-weekly)',        'Owner':'Member 5 (Docs)',      'Start':1.0,  'Dur':12.0, 'Crit':False},\n",
  "    # Phase 2: Training & BPU Conversion (PM Lead + Member 1)\n",
  "    {'Task':'2.1 Colab Training Setup & YOLOv8n Run',  'Owner':'PM Lead + Mbr1',       'Start':4.5,  'Dur':1.5,  'Crit':True},\n",
  "    {'Task':'2.2 Model Evaluation (mAP/PR/Confusion)', 'Owner':'PM Lead + Mbr1',       'Start':5.5,  'Dur':0.5,  'Crit':True},\n",
  "    {'Task':'2.3 ONNX Export + hb_mapper BPU Compile', 'Owner':'PM Lead + Mbr1',       'Start':6.0,  'Dur':1.5,  'Crit':True},\n",
  "    # Phase 3: System Development (PM Lead)\n",
  "    {'Task':'3.1 System Architecture & Horizon SDK',   'Owner':'PM Lead + Mbr1',       'Start':1.0,  'Dur':2.0,  'Crit':False},\n",
  "    {'Task':'3.2 USB Webcam V4L2 Capture Pipeline',   'Owner':'PM Lead + Mbr1',       'Start':2.0,  'Dur':2.0,  'Crit':False},\n",
  "    {'Task':'3.3 BPU Inference Engine Integration',   'Owner':'PM Lead + Mbr1',       'Start':6.0,  'Dur':2.0,  'Crit':True},\n",
  "    {'Task':'3.4 Basic OSD UI & Entry Display',       'Owner':'PM Lead + Mbr1',       'Start':7.0,  'Dur':1.0,  'Crit':True},\n",
  "    # FIRST DEPLOYMENT MILESTONE - WEEK 8\n",
  "    {'Task':'\U0001f3af FIRST DEPLOYMENT on RDK X5 BPU',     'Owner':'All Team',             'Start':8.0,  'Dur':0.3,  'Crit':True},\n",
  "    # Phase 4: Post-Deploy Optimization\n",
  "    {'Task':'4.1 Edge Case Dataset Expansion',        'Owner':'Member 3 (Dataset)',   'Start':8.0,  'Dur':3.0,  'Crit':False},\n",
  "    {'Task':'4.2 Re-annotation & Roboflow V2',        'Owner':'Member 4 (Dataset)',   'Start':8.5,  'Dur':2.5,  'Crit':False},\n",
  "    {'Task':'4.3 Re-training (improved dataset)',     'Owner':'PM Lead + Mbr1',       'Start':10.5, 'Dur':1.5,  'Crit':True},\n",
  "    {'Task':'4.4 Threshold & NMS Tuning on BPU',     'Owner':'PM Lead + Mbr1',       'Start':11.0, 'Dur':1.0,  'Crit':True},\n",
  "    # Phase 5: System Dev Phase 2\n",
  "    {'Task':'3.5 Access Control Policy & Logging',   'Owner':'PM Lead + Mbr1',       'Start':9.0,  'Dur':2.5,  'Crit':False},\n",
  "    {'Task':'3.6 Multi-Student Stress Testing',      'Owner':'PM Lead + Mbr1',       'Start':11.5, 'Dur':1.0,  'Crit':True},\n",
  "    # Phase 6: Final QA & Docs\n",
  "    {'Task':'6.1 Final System QA & Acceptance Test', 'Owner':'All Team',             'Start':12.0, 'Dur':2.0,  'Crit':True},\n",
  "    {'Task':'6.2 Final Report & Slide Deck',         'Owner':'Member 5 (Docs)',      'Start':12.0, 'Dur':2.0,  'Crit':False},\n",
  "    {'Task':'6.3 Project Handover & Demo',           'Owner':'All Team',             'Start':14.0, 'Dur':0.5,  'Crit':True},\n",
  "]\n",
  "\n",
  "import pandas as pd\n",
  "df = pd.DataFrame(schedule_data)\n",
  "y_indices = range(len(df))\n",
  "\n",
  "for idx, row in df.iterrows():\n",
  "    col = ROLE_COLORS.get(row['Owner'], '#475569')\n",
  "    edge = '#b91c1c' if row['Crit'] else '#475569'\n",
  "    lw = 2.0 if row['Crit'] else 0.8\n",
  "    ax.barh(idx, row['Dur'], left=row['Start'], height=0.55,\n",
  "            color=col, edgecolor=edge, linewidth=lw, alpha=0.9, zorder=3)\n",
  "    label = row['Owner'].split()[0][:4]\n",
  "    if row['Dur'] > 0.5:\n",
  "        ax.text(row['Start'] + row['Dur']/2, idx, label,\n",
  "                ha='center', va='center', color='white', fontweight='bold', fontsize=7.5, zorder=4)\n",
  "\n",
  "# Milestone: Week 8 First Deployment\n",
  "ax.axvline(x=8.0, color='#eab308', linestyle='-', linewidth=3.0, alpha=0.9, zorder=5)\n",
  "ax.text(8.0, -0.8, ' \U0001f3af Week 8\\nFirst Deploy', ha='center', va='top',\n",
  "        fontsize=9, fontweight='bold', color='#b45309',\n",
  "        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9c3', edgecolor='#eab308'))\n",
  "\n",
  "# Optimization phase shading\n",
  "ax.axvspan(8.0, 12.0, color='#f0fdf4', alpha=0.3, label='Post-Deploy Optimization Zone')\n",
  "ax.text(10.0, len(df)+0.3, 'POST-DEPLOY OPTIMIZATION', ha='center',\n",
  "        fontsize=8, color='#16a34a', fontweight='bold')\n",
  "\n",
  "ax.set_yticks(list(y_indices))\n",
  "ax.set_yticklabels(df['Task'], fontsize=8.5)\n",
  "ax.invert_yaxis()\n",
  "ax.set_xlabel('Project Timeline (Weeks)', fontsize=11, fontweight='bold')\n",
  "ax.set_xlim(0.5, 14.8)\n",
  "ax.set_xticks(range(1, 15))\n",
  "ax.grid(axis='x', linestyle=':', alpha=0.6, zorder=1)\n",
  "\n",
  "legend_handles = [\n",
  "    mpatches.Patch(color=ROLE_COLORS['PM Lead + Mbr1'], label='PM Lead + Member 1'),\n",
  "    mpatches.Patch(color=ROLE_COLORS['Member 3 (Dataset)'], label='Member 3 (Dataset)'),\n",
  "    mpatches.Patch(color=ROLE_COLORS['Member 4 (Dataset)'], label='Member 4 (Dataset)'),\n",
  "    mpatches.Patch(color=ROLE_COLORS['Member 5 (Docs)'], label='Member 5 (Docs/Support)'),\n",
  "    mpatches.Patch(color=ROLE_COLORS['All Team'], label='All Team'),\n",
  "    mpatches.Patch(facecolor='none', edgecolor='#b91c1c', linewidth=2.0, label='Critical Path'),\n",
  "]\n",
  "ax.legend(handles=legend_handles, loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=8)\n",
  "plt.title('KOE PPE Detection — 14-Week Gantt (First Deployment: Week 8)', fontsize=13, fontweight='bold', pad=15)\n",
  "plt.tight_layout()\n",
  "plt.show()"
 ]
}

pareto_md = {"cell_type": "markdown", "metadata": {}, "source": ["## 4. \U0001f4ca Pareto, Control & Baseline Charts\n"]}

pareto_cell = {
 "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
 "source": [
  "# Cell 3: Pareto — Top Risk Factors\n",
  "fig, ax1 = plt.subplots(figsize=(11, 5.5), dpi=200)\n",
  "categories = [\n",
  "    'Green T-shirts\\n(False Positives)', 'Bench/Machine\\nOcclusion',\n",
  "    'Low-light\\nShadows', 'Far Distance\\n(>5m)', 'Backside\\nFacing',\n",
  "    'Motion Blur', 'Dense Student\\nClusters', 'Reflective\\nVests'\n",
  "]\n",
  "counts = [68, 44, 29, 18, 14, 10, 6, 4]\n",
  "cum_pct = np.cumsum(counts) / sum(counts) * 100\n",
  "x = np.arange(len(categories))\n",
  "bars = ax1.bar(x, counts, color='#0284c7', edgecolor='#0369a1', width=0.55, alpha=0.88, zorder=3)\n",
  "ax1.set_ylabel('Incident Frequency', fontsize=10, fontweight='bold', color='#0369a1')\n",
  "ax1.set_xticks(x)\n",
  "ax1.set_xticklabels(categories, rotation=25, ha='right', fontsize=8.5)\n",
  "ax1.set_ylim(0, max(counts) * 1.15)\n",
  "ax1.grid(axis='y', linestyle=':', alpha=0.6, zorder=1)\n",
  "for bar in bars:\n",
  "    h = bar.get_height()\n",
  "    ax1.text(bar.get_x() + bar.get_width()/2., h + 1.2, f'{int(h)}',\n",
  "             ha='center', va='bottom', fontsize=8.5, fontweight='bold')\n",
  "ax2 = ax1.twinx()\n",
  "ax2.plot(x, cum_pct, color='#dc2626', marker='D', linewidth=2.0, markersize=5, zorder=4)\n",
  "ax2.set_ylabel('Cumulative %', fontsize=10, fontweight='bold', color='#dc2626')\n",
  "ax2.set_ylim(0, 105)\n",
  "ax2.axhline(80, color='#eab308', linestyle='--', linewidth=1.5)\n",
  "ax2.text(len(categories)-1, 81.5, '80% Threshold', ha='right', fontsize=8.5, fontweight='bold', color='#b45309')\n",
  "plt.title('Pareto: Root Causes of Detection Failures', fontsize=12, fontweight='bold', pad=12)\n",
  "plt.tight_layout()\n",
  "plt.show()"
 ]
}

control_cell = {
 "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
 "source": [
  "# Cell 4: SPC Control Chart — mAP Convergence\n",
  "np.random.seed(42)\n",
  "batches = np.arange(1, 26)\n",
  "trajectory = np.concatenate([np.linspace(76, 91.5, 10), np.linspace(91.5, 93.4, 15)])\n",
  "map_vals = trajectory + np.random.normal(0, 0.85, 25)\n",
  "stable = map_vals[10:]\n",
  "mean_v, sigma = np.mean(stable), np.std(stable)\n",
  "fig, ax = plt.subplots(figsize=(11, 5), dpi=200)\n",
  "ax.plot(batches, map_vals, marker='o', color='#2563eb', linewidth=1.8, markersize=5, label='mAP@0.5 (%)')\n",
  "ax.axhline(mean_v, color='#16a34a', linestyle='-', linewidth=1.5, label=f'Mean ({mean_v:.1f}%)')\n",
  "ax.axhline(mean_v+3*sigma, color='#dc2626', linestyle='--', linewidth=1.5, label=f'UCL ({mean_v+3*sigma:.1f}%)')\n",
  "ax.axhline(mean_v-3*sigma, color='#dc2626', linestyle='--', linewidth=1.5, label=f'LCL ({mean_v-3*sigma:.1f}%)')\n",
  "ax.axhline(90.0, color='#d97706', linestyle=':', linewidth=2.0, label='Target (90%)')\n",
  "ax.axvspan(10.5, 25.5, color='#f0fdf4', alpha=0.5, label='Stable BPU Zone')\n",
  "ax.set_xlabel('Evaluation Batch', fontsize=10, fontweight='bold')\n",
  "ax.set_ylabel('mAP@0.5 (%)', fontsize=10, fontweight='bold')\n",
  "ax.set_ylim(72, 98)\n",
  "ax.legend(loc='lower right', fontsize=8.5, frameon=True)\n",
  "ax.grid(True, linestyle=':', alpha=0.6)\n",
  "plt.title('SPC Control Chart: mAP Stability across Training & BPU Dry Runs', fontsize=12, fontweight='bold', pad=12)\n",
  "plt.tight_layout()\n",
  "plt.show()"
 ]
}

baseline_cell = {
 "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
 "source": [
  "# Cell 5: Baseline vs Actual Dashboard\n",
  "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=200)\n",
  "\n",
  "# Schedule\n",
  "ms = ['M0: Kickoff', 'M1: Dataset V1 Frozen', 'M2: Trained & ONNX',\n",
  "      'M3: BPU .bin Ready', 'M4: FIRST DEPLOY (Wk8)', 'M5: Optimization Done', 'M6: Final QA']\n",
  "base = [1.0, 4.0, 6.0, 7.5, 8.0, 12.0, 14.0]\n",
  "proj = [1.0, 4.0, 6.0, 7.0, 8.0, 11.5, 13.5]\n",
  "y = np.arange(len(ms))\n",
  "ax1.barh(y-0.18, base, height=0.35, color='#94a3b8', label='Baseline (Planned)')\n",
  "ax1.barh(y+0.18, proj, height=0.35, color='#0f766e', label='Projected')\n",
  "ax1.set_yticks(y)\n",
  "ax1.set_yticklabels(ms, fontsize=8.5)\n",
  "ax1.invert_yaxis()\n",
  "ax1.set_xlabel('Week', fontsize=9, fontweight='bold')\n",
  "ax1.axvline(8, color='#eab308', linestyle='--', linewidth=1.5, label='Week 8 Deploy')\n",
  "ax1.legend(fontsize=8)\n",
  "ax1.grid(axis='x', linestyle=':', alpha=0.6)\n",
  "ax1.set_title('Schedule: Baseline vs Projected', fontsize=11, fontweight='bold')\n",
  "\n",
  "# KPIs\n",
  "kpis = ['mAP@0.5 (%)', 'BPU FPS', 'Precision (%)', 'Recall (%)', 'Latency (ms)']\n",
  "targets = [90.0, 25.0, 88.0, 88.0, 30.0]\n",
  "achieved = [93.4, 38.2, 91.5, 90.2, 17.5]\n",
  "xk = np.arange(len(kpis))\n",
  "ax2.bar(xk-0.18, targets, width=0.35, color='#94a3b8', label='Target')\n",
  "ax2.bar(xk+0.18, achieved, width=0.35, color='#2563eb', label='Projected')\n",
  "ax2.set_xticks(xk)\n",
  "ax2.set_xticklabels(kpis, fontsize=8.5)\n",
  "ax2.legend(fontsize=8)\n",
  "ax2.grid(axis='y', linestyle=':', alpha=0.6)\n",
  "ax2.set_title('Engineering KPIs: Target vs Projected', fontsize=11, fontweight='bold')\n",
  "for i in range(len(kpis)):\n",
  "    ax2.text(xk[i]-0.18, targets[i]+1.2, f'{targets[i]:.0f}', ha='center', fontsize=7.5, color='#475569')\n",
  "    ax2.text(xk[i]+0.18, achieved[i]+1.2, f'{achieved[i]:.1f}', ha='center', fontsize=7.5, color='#1e3a8a', fontweight='bold')\n",
  "plt.suptitle('Baseline vs Actual: Schedule & KPI Dashboard', fontsize=13, fontweight='bold')\n",
  "plt.tight_layout()\n",
  "plt.show()"
 ]
}

risk_md = {
 "cell_type": "markdown", "metadata": {}, "source": [
  "## 5. \u26a0\ufe0f Risk Register\n",
  "\n",
  "| # | Risk | Prob | Impact | Severity | Owner | Mitigation |\n",
  "| :---: | :--- | :---: | :---: | :---: | :--- | :--- |\n",
  "| R1 | Poor annotation quality from beginners | High | High | **CRITICAL** | PM Lead | Provide DATASET_TEAM_GUIDE.ipynb; spot-check weekly; use Roboflow consensus labelling |\n",
  "| R2 | mAP below 90% after training | Med | High | HIGH | PM Lead + M1 | Expand dataset; augmentation tuning; step up to YOLOv8s |\n",
  "| R3 | Week 8 deployment slip (data late) | Med | High | HIGH | Member 3/4 | Daily check-ins Week 1–4; Member 5 assists annotation |\n",
  "| R4 | Quantization accuracy drop > 3% | Med | Med | MEDIUM | Member 1 | Use 150+ calibration images; validate with cosine similarity |\n",
  "| R5 | Colab session timeouts during training | High | Low | LOW | PM Lead | Save checkpoint every 25 epochs to Drive |\n",
  "| R6 | Camera angle mismatch (train vs deploy) | Med | High | HIGH | All Team | Decide & document camera position in Week 1 BEFORE any capture |\n",
 ]
}

nb_new = {
    "cells": [
        header_md, model_md, team_md,
        install_cell,
        gantt_md, gantt_cell,
        pareto_md, pareto_cell, control_cell, baseline_cell,
        risk_md
    ],
    "metadata": {"language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 5
}

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb_new, f, indent=1, ensure_ascii=False)

print("Main project plan notebook updated successfully.")
