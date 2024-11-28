import cv2
import numpy as np
import mss

def capture_screen():
    sct = mss.mss()
    monitor = sct.monitors[1]  # Adjust for your primary monitor

    while True:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)  # Convert RGBA to BGR
        yield frame
