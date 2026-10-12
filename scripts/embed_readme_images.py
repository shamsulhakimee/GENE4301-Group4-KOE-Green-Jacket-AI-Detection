with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. WBS
if '![Work Breakdown Structure](docs/figures/wbs_structure.png)' not in content:
    content = content.replace(
        '## 🗂️ Work Breakdown Structure (WBS)\n',
        '## 🗂️ Work Breakdown Structure (WBS)\n\n![Work Breakdown Structure](docs/figures/wbs_structure.png)\n'
    )

# 2. Gantt
if '![Master Schedule Gantt Chart](docs/figures/gantt_chart.png)' not in content:
    content = content.replace(
        '## 📅 Master 14-Week Schedule & Gantt Chart (Week 8 Deployment)\n',
        '## 📅 Master 14-Week Schedule & Gantt Chart (Week 8 Deployment)\n\n![Master Schedule Gantt Chart](docs/figures/gantt_chart.png)\n'
    )

# 3. Flowchart
if '![ROS2 Humble Flowchart](docs/figures/system_flowchart.png)' not in content:
    content = content.replace(
        '## 🔄 ROS2 Humble Edge Architecture & Node Dataflow\n',
        '## 🔄 ROS2 Humble Edge Architecture & Node Dataflow\n\n![ROS2 Humble Flowchart](docs/figures/system_flowchart.png)\n'
    )

# 4. Risk Register / Pareto
if '![Pareto Analysis](docs/figures/pareto_chart.png)' not in content:
    content = content.replace(
        '## ⚠️ Risk Register & Mitigation Strategy\n',
        '## ⚠️ Risk Register & Mitigation Strategy\n\n![Pareto Analysis](docs/figures/pareto_chart.png)\n'
    )

# 5. Baseline vs Actual & Control Chart
if '![Baseline vs Actual Dashboard](docs/figures/baseline_vs_actual.png)' not in content:
    content = content.replace(
        '## 📊 Baseline vs Actual Tracking Tables\n',
        '## 📊 Baseline vs Actual Tracking Tables\n\n![Baseline vs Actual Dashboard](docs/figures/baseline_vs_actual.png)\n\n![Statistical Process Control Chart](docs/figures/control_chart.png)\n'
    )

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("README.md embedded with all figures from docs/figures/ successfully.")
