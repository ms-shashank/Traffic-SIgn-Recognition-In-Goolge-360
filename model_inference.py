from ultralytics import YOLO

def load_model(model_name='yolov8s.pt'):
    return YOLO(model_name)

def run_inference(model, frame):
    results = model(frame)  # Inference on the frame
    annotated_frame = results[0].plot()  # Annotate frame with detections
    return annotated_frame
