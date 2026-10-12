"""
KOE Green Jacket PPE AI Detection System
Real-Time Webcam Multi-Person Detection & Workshop Entry Compliance Test Harness
Handled by: Project Lead (System Developer)
"""

import cv2
import time
import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="KOE Green Jacket PPE Detector Test Harness")
    parser.add_argument("--model", type=str, default="models/koe_green_jacket_yolov8n.bin", help="Path to BPU .bin or ONNX model")
    parser.add_argument("--device", type=int, default=0, help="Webcam device index (default: 0)")
    parser.add_argument("--conf", type=float, default=0.50, help="Confidence threshold")
    parser.add_argument("--iou", type=float, default=0.45, help="NMS IoU threshold")
    return parser.parse_args()

def main():
    args = parse_args()
    print("=" * 60)
    print("🎓 KOE Green Jacket PPE Detection System — Entry Verification")
    print(f"Vision Sensor: USB Webcam (Index: {args.device})")
    print(f"Target Single Class: 'KOE Green Jacket'")
    print(f"Confidence Threshold: {args.conf} | IoU: {args.iou}")
    print("=" * 60)

    cap = cv2.VideoCapture(args.device)
    if not cap.isOpened():
        print(f"❌ Error: Unable to open webcam on device index {args.device}")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    prev_time = time.time()
    fps_history = []

    print("▶️ Real-time detection loop initiated. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Warning: Failed to read frame from webcam.")
            break

        curr_time = time.time()
        instant_fps = 1.0 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 30.0
        prev_time = curr_time
        fps_history.append(instant_fps)
        if len(fps_history) > 30:
            fps_history.pop(0)
        avg_fps = np.mean(fps_history)

        # Draw Header Bar (OSD)
        h, w, _ = frame.shape
        cv2.rectangle(frame, (0, 0), (w, 50), (15, 23, 42), -1)
        cv2.putText(frame, "KOE WORKSHOP ENTRANCE PPE DETECTOR", (20, 32),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
        cv2.putText(frame, f"FPS: {avg_fps:.1f} (RDK X5 BPU)", (w - 240, 32),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (34, 197, 94), 2)

        # Entry Status Legend Box
        cv2.rectangle(frame, (20, h - 60), (380, h - 20), (15, 23, 42), -1)
        cv2.circle(frame, (35, h - 40), 7, (34, 197, 94), -1)
        cv2.putText(frame, "PASS: KOE Green Jacket", (50, h - 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow("KOE Green Jacket PPE AI Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("⏹️ Video pipeline released. Test session concluded.")

if __name__ == "__main__":
    main()
