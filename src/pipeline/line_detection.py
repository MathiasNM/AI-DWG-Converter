import cv2
import numpy as np
import os
from src.config.paths import PROC_TEMP, PROC_LINES

def detect_lines(image_name):
    image_path = os.path.join(PROC_TEMP, image_name)

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No se encontró la imagen: {image_path}")

    print(f"Procesando imagen: {image_path}")

    # Cargar imagen en escala de grises
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Detectar bordes
    edges = cv2.Canny(img, 50, 150, apertureSize=3)

    # Detectar líneas con Hough
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=50,
        maxLineGap=10
    )

    # Crear carpeta de salida si no existe
    os.makedirs(PROC_LINES, exist_ok=True)

    # Imagen de salida con líneas dibujadas
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    line_data = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(output_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            line_data.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    # Guardar imagen con líneas
    output_path = os.path.join(PROC_LINES, image_name.replace(".png", "_lines.png"))
    cv2.imwrite(output_path, output_img)

    print(f"Líneas detectadas: {len(line_data)}")
    print(f"Imagen guardada: {output_path}")

    return line_data


if __name__ == "__main__":
    # Cambia esto por el nombre de tu imagen
    detect_lines("plano1.pdf_page_1.png")
