import os
from pdf2image import convert_from_path
from src.config.paths import INPUT_PDF, PROC_TEMP

def pdf_to_images(pdf_filename, dpi=300):
    """
    Convierte un PDF en imágenes PNG (una por página).
    Guarda las imágenes en la carpeta de procesamiento temporal.
    """

    pdf_path = os.path.join(INPUT_PDF, pdf_filename)

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No se encontró el PDF: {pdf_path}")

    print(f"📄 Procesando PDF: {pdf_filename}")

    # Convertir PDF → lista de imágenes PIL
    pages = convert_from_path(pdf_path, dpi=dpi)

    output_paths = []

    for i, page in enumerate(pages):
        output_file = os.path.join(PROC_TEMP, f"{pdf_filename}_page_{i+1}.png")
        page.save(output_file, "PNG")
        output_paths.append(output_file)
        print(f"🖼️ Página {i+1} guardada: {output_file}")

    print("✅ Conversión completada.")
    return output_paths


if __name__ == "__main__":
    # EJEMPLO DE USO:
    # Coloca un PDF dentro de: 01_Input/PDFs/
    # Luego ejecuta este script desde tu PC.
    pdf_name = "plano1.pdf"  # Cambia esto por tu archivo real
    pdf_to_images(pdf_name)
