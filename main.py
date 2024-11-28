import cv2
from screen_capture import capture_screen
from model_inference import load_model, run_inference

def main():
    # Load YOLO model
    model = load_model('yolov8s.pt')

    # Capture screen and run inference
    for frame in capture_screen():
        annotated_frame = run_inference(model, frame)

        # Display the annotated frame
        cv2.imshow("Traffic Sign Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
