import os

import cv2

# Subindo o vídeo
entrypoint = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(entrypoint, "media", "race.mp4")
cap = cv2.VideoCapture(VIDEO_PATH)

# Mostrar o vídeo
if not cap.isOpened():
    raise FileNotFoundError(f"Não foi possível carregar o vídeo:{VIDEO_PATH}")

while True:
    ok, frame = cap.read()

    if not ok:
        cap.release()

        raise RuntimeError("Falha ao carregar o primeiro frame")

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
