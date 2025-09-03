import os

import cv2
import numpy as np

entrypoint = os.path.abspath(os.path.dirname(__file__))

image_path = os.path.join(
    entrypoint,
    "media",
    "jinx.jpeg"
)
img = cv2.imread(image_path)



def activity1():
    cv2.imshow("Jinx", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity2():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Colorida", img)
    cv2.imshow("Cinza", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity3():
    small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    large = cv2.resize(img, (0, 0), fx=2, fy=2)
    cv2.imshow("Original", img)
    cv2.imshow("Reduzida", small)
    cv2.imshow("Ampliada", large)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity4():
    img = np.zeros((500, 500, 3), dtype="uint8")

    cv2.rectangle(img, (50, 50), (200, 200), (0, 255 ,0), -1) # Retângulo verde
    cv2.circle(img, (300, 300), 50, (255, 0, 0), -1) # Círculo azul
    cv2.line(img, (0,0), (500, 500), (0, 0, 255), 5) # Linha vermelha

    cv2.putText(
        img,
        "William",
        (150, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("Desenho", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity5():
    negativo = 255 - img

    cv2.imshow("Original", img)
    cv2.imshow("Negativo", negativo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity6():
    roi = img[50:200, 100:300]

    cv2.imshow("Original", img)
    cv2.imshow("Recorte", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity7():
    # Rotação 90 graus
    rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotação 45 graus em torno do centro
    (h, w) = img.shape[:2]
    centro = (w//2, h//2)
    matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)
    rot45 = cv2.warpAffine(img, matriz, (w, h))

    cv2.imshow("Original", img)
    cv2.imshow("90 graus", rot90)
    cv2.imshow("45 graus", rot45)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity8():
    gauss = cv2.GaussianBlur(img, (7,7), 0)
    median = cv2.medianBlur(img, 7)

    cv2.imshow("Original", img)
    cv2.imshow("Gaussian", gauss)
    cv2.imshow("Median", median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def activity9():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def activity10():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        lado_a_lado = np.hstack((frame, gray_bgr))

        cv2.imshow("Colorido e Cinza", lado_a_lado)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def activity11():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        bordas = cv2.Canny(frame, 100, 200)

        cv2.imshow("Bordas", bordas)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def activity12():
    img = np.zeros((500,500,3), dtype="uint8")

    def desenhar(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x,y), 20, (0,255,0), -1)

    cv2.namedWindow("Desenho")
    cv2.setMouseCallback("Desenho", desenhar)

    while True:
        cv2.imshow("Desenho", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

