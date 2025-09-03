import os
import sys

import cv2

entrypoint = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(entrypoint, "media", "video_street.mp4")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file at {video_path}")
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Reached the end of the video or an error occurred.")
        break

    cv2.imshow('Video Player', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
