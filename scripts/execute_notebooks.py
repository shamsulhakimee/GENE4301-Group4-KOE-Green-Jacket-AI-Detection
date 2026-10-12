import json
import os
import sys
import io
import base64
import contextlib

def run_notebook(nb_path):
    print(f"Executing and embedding outputs for: {nb_path}")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    global_namespace = {
        "__name__": "__main__",
        "__file__": os.path.abspath(nb_path),
    }

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    exec_count = 1

    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue

        source_code = "".join(cell["source"])
        outputs = []

        # Hook plt.show to capture figures as base64 PNG
        captured_figs = []
        orig_show = plt.show

        def custom_show(*args, **kwargs):
            fig_nums = plt.get_fignums()
            for num in fig_nums:
                fig = plt.figure(num)
                buf = io.BytesIO()
                fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
                buf.seek(0)
                img_b64 = base64.b64encode(buf.read()).decode("utf-8")
                captured_figs.append(img_b64)
                plt.close(fig)

        plt.show = custom_show

        # Capture stdout
        stdout_capture = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stdout_capture):
                exec(source_code, global_namespace)
        except Exception as e:
            print(f"  Error in Cell {idx}: {e}")
            raise e
        finally:
            plt.show = orig_show

        stdout_text = stdout_capture.getvalue()
        if stdout_text:
            outputs.append({
                "output_type": "stream",
                "name": "stdout",
                "text": [line + "\n" for line in stdout_text.splitlines()]
            })

        for img_b64 in captured_figs:
            outputs.append({
                "output_type": "display_data",
                "data": {
                    "image/png": img_b64,
                    "text/plain": ["<Figure size ...>"]
                },
                "metadata": {}
            })

        cell["outputs"] = outputs
        cell["execution_count"] = exec_count
        exec_count += 1
        print(f"  Cell {idx} executed: {len(outputs)} output item(s) captured.")

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Saved {nb_path} with embedded outputs successfully!\n")

if __name__ == "__main__":
    run_notebook("notebooks/KOE_Green_Jacket_Project_Plan.ipynb")
    run_notebook("notebooks/DATASET_TEAM_GUIDE.ipynb")
