import json

nb_path = r'c:\Users\Victus\OneDrive\Desktop\GENE_ProjectAI\notebooks\MEMBER5_PAPERWORK_GUIDE.ipynb'

cells = []

# Cell 0: Header & Role Summary
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# 📋 Member 5 — Documentation & Paperwork Guide\n",
        "### KOE Green Jacket PPE Detection Project\n",
        "\n",
        "---\n",
        "\n",
        "## Your Role\n",
        "You are the **Documentation Lead** for this project.  \n",
        "Your work ensures the team has a professional paper trail — from initial proposal to final report.\n",
        "\n",
        "| Priority | Activity | When |\n",
        "| :---: | :--- | :--- |\n",
        "| 1 | **Project Proposal** | Week 1–2 |\n",
        "| 2 | **Bi-weekly Progress Reports** | Every 2 weeks, Weeks 1–14 |\n",
        "| 3 | **Assist Dataset Annotation** | Weeks 2–4, when no paperwork due |\n",
        "| 4 | **Slide Deck — Mid-project Briefing** | Week 7 |\n",
        "| 5 | **Final Report** | Weeks 12–14 |\n",
        "| 6 | **Final Presentation Slides** | Week 13–14 |\n",
        "\n",
        "---\n"
    ]
})

# Cell 1: Project Proposal
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 1. 📤 Project Proposal (Week 1–2)\n",
        "\n",
        "### Required Sections:\n",
        "1. **Introduction** — Why does this project exist? What is the safety problem at the KOE workshop?\n",
        "2. **Project Objectives** — What exactly will be built? (Single-class AI detector running on RDK X5 under ROS2 Humble)\n",
        "3. **Scope** — What is included and what is NOT included in this project\n",
        "4. **Team & Roles** — List all 5 members and their responsibilities (use RACI matrix from README)\n",
        "5. **Methodology** — Short summary of: data collection → training on Colab → BPU deployment in ROS2 Humble\n",
        "6. **Schedule** — 14-week Gantt chart (export image from `docs/figures/gantt_chart.png`)\n",
        "7. **Expected Deliverables** — Working edge detection system, trained model, documentation\n",
        "8. **Resources Required** — Roboflow account, Google Colab GPU, RDK X5 hardware\n",
        "\n",
        "### Tips:\n",
        "- Ask PM Lead to explain any technical terms you do not understand — do not guess\n",
        "- Use the Gantt chart and WBS images from `docs/figures/` in the proposal\n",
        "- Keep it concise — 5 to 8 pages is ideal for an engineering project proposal\n"
    ]
})

# Cell 2: Bi-weekly Progress Reports
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 2. 📈 Bi-weekly Progress Reports (Every 2 weeks)\n",
        "\n",
        "### Standard Report Template:\n",
        "```\n",
        "KOE PPE Detection — Progress Report [Week X to Week Y]\n",
        "Date: ____  Prepared by: Member 5  Approved by: PM Lead\n",
        "\n",
        "1. SUMMARY OF WORK COMPLETED\n",
        "   - (List what each team member actually completed this period)\n",
        "\n",
        "2. KEY METRICS THIS PERIOD\n",
        "   - Images collected: ___  /  Target: ___\n",
        "   - Images annotated: ___  /  Total uploaded: ___\n",
        "   - Model mAP (if training has started): ___\n",
        "   - BPU FPS (if deployed): ___\n",
        "\n",
        "3. PLANNED WORK NEXT PERIOD\n",
        "   - (List what each member plans to complete)\n",
        "\n",
        "4. ISSUES & RISKS\n",
        "   - (Any blockers, delays, or concerns raised this period)\n",
        "\n",
        "5. SCHEDULE STATUS\n",
        "   - On track / At risk / Delayed\n",
        "   - Milestones hit this period: ___\n",
        "```\n",
        "\n",
        "### How to get the information:\n",
        "- Attend weekly team stand-ups and take notes\n",
        "- Check Roboflow image count directly (ask Member 4 to share access)\n",
        "- Ask PM Lead for training metrics (mAP, FPS) each reporting period\n"
    ]
})

# Cell 3: Dataset Support Protocol
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 3. 🖼️ When to Help with Dataset Annotation\n",
        "\n",
        "**During Weeks 2–4, whenever no paperwork deadline is imminent:**\n",
        "- Log into Roboflow (Member 4 will grant access)\n",
        "- Pick any un-annotated image from the queue\n",
        "- Follow the annotation rules in `DATASET_TEAM_GUIDE.ipynb` (tight bounding boxes, KOE Green Jacket label)\n",
        "- Do NOT guess if you are unsure about an image — ask Member 4 or PM Lead first\n",
        "- Every 25 images you annotate significantly reduces pressure on the Week 4 dataset freeze deadline\n"
    ]
})

# Cell 4: Mid-project Slide Deck
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 4. 📊 Slide Deck — Mid-Project Briefing (Week 7)\n",
        "\n",
        "### Recommended Slide Structure (8–10 slides):\n",
        "| Slide | Content |\n",
        "| :---: | :--- |\n",
        "| 1 | Title: Project name, team members, supervisor, date |\n",
        "| 2 | Problem statement + why PPE compliance matters in KOE workshops |\n",
        "| 3 | System architecture diagram (ROS2 Humble + RDK X5 BPU) |\n",
        "| 4 | Team structure and RACI governance matrix |\n",
        "| 5 | Dataset statistics (positive vs negative image breakdown) |\n",
        "| 6 | YOLOv8n model training metrics (mAP@0.5, Precision, Recall) |\n",
        "| 7 | Live demo screenshot (RDK X5 running at workshop entrance) |\n",
        "| 8 | 14-Week Gantt chart tracking — Week 8 First Deployment milestone |\n",
        "| 9 | Risk management & mitigation table |\n",
        "| 10 | Next steps (post-deployment tuning & access control policy) |\n"
    ]
})

# Cell 5: Final Report Outline
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 5. 📖 Final Report Outline (Weeks 12–14)\n",
        "\n",
        "The final technical and delivery report format:\n",
        "```\n",
        "Chapter 1: Introduction\n",
        "  1.1 Background & KOE Safety Requirements\n",
        "  1.2 Objectives & Scope\n",
        "\n",
        "Chapter 2: Literature Review\n",
        "  2.1 Real-Time Object Detection (YOLO Architectures)\n",
        "  2.2 Edge AI Hardware & BPU Accelerators (RDK X5)\n",
        "  2.3 ROS2 Humble in Embedded Computer Vision\n",
        "\n",
        "Chapter 3: Methodology & System Architecture\n",
        "  3.1 Dataset Engineering Protocol (Positive & Negative Samples)\n",
        "  3.2 Roboflow Labelling, QA & Augmentation\n",
        "  3.3 YOLOv8n Training & ONNX Export\n",
        "  3.4 Horizon OpenExplorer INT8 PTQ Quantization\n",
        "  3.5 ROS2 Humble Node Pipeline (Camera -> BPU -> Access Controller)\n",
        "\n",
        "Chapter 4: Results & Discussion\n",
        "  4.1 Model Accuracy (mAP@0.5, Confusion Matrix)\n",
        "  4.2 Edge Performance (FPS, Latency, CPU/Memory Usage)\n",
        "  4.3 Multi-Student Entrance Testing Results\n",
        "  4.4 Baseline vs Actual KPI Comparison\n",
        "\n",
        "Chapter 5: Conclusion & Future Work\n",
        "```\n"
    ]
})

# Cell 6: Communication Protocol
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 6. 📢 Team Communication Protocol\n",
        "\n",
        "| Situation | Protocol |\n",
        "| :--- | :--- |\n",
        "| Progress report data missing from a member | Prompt them 48h before deadline; escalate to PM Lead if delayed |\n",
        "| Technical concept unclear (e.g., BPU INT8, ROS2) | Request a quick 10-minute briefing from PM Lead |\n",
        "| Conflicting priorities (Paperwork vs Annotation) | **Paperwork deadlines take absolute priority** — notify Members 3 & 4 |\n",
        "| Final review before formal submission | Submit draft to PM Lead 72h before official submission |\n"
    ]
})

nb = {
    "cells": cells,
    "metadata": {"language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 5
}

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("MEMBER5_PAPERWORK_GUIDE.ipynb successfully formatted with 7 modular cells.")
