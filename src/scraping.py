
"""
Módulo de extracción y procesamiento de datos HTML.

Proyecto: Análisis de productos de comercio electrónico.
Producto de referencia: Portátil SUXI 2026 publicado en Temu.

El programa analiza un archivo HTML local mediante BeautifulSoup.
No realiza solicitudes automatizadas a Temu.
"""

from pathlib import Path
import json
import re

from bs4 import BeautifulSoup


# Directorio principal del proyecto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Ubicación de los archivos de entrada y salida.
HTML_FILE = PROJECT_ROOT / "data" / "pagina_autorizada.html"
OUTPUT_FILE = PROJECT_ROOT / "results" / "resultado_extraccion.json"


def clean_text(value):
    """Normaliza los espacios y elimina caracteres innecesarios."""
    if value is None:
        return ""

    return re.sub(r"\s+", " ", str(value)).strip()


def get_element_value(element):
    """Obtiene el contenido de un elemento HTML."""
    if element is None:
        return None

    value = element.get("content")

    if not value:
        value = element.get_text(" ", strip=True)

    return clean_text(value) or None


def extract_product_data(html_text):
    """
    Analiza el HTML y extrae los campos principales del producto.

    Args:
        html_text (str): Contenido del documento HTML.

    Returns:
        dict: Información estructurada del producto.
    """

    soup = BeautifulSoup(html_text, "html.parser")

    title = soup.find("h1") or soup.find("title")
    price = soup.select_one('[itemprop="price"]')
    rating = soup.select_one('[itemprop="ratingValue"]')
    reviews = soup.select_one('[itemprop="reviewCount"]')

    return {
        "titulo": clean_text(title.get_text(" ", strip=True))
        if title else None,

        "precio": get_element_value(price),

        "calificacion": get_element_value(rating),

        "cantidad_resenas": get_element_value(reviews),

        "fuente": HTML_FILE.name,

        "metodo": "BeautifulSoup sobre archivo HTML local"
    }


def main():
    """Ejecuta la extracción y guarda los resultados."""

    if not HTML_FILE.is_file():
        raise FileNotFoundError(
            f"No se encontró el archivo de entrada: {HTML_FILE}"
        )

    # Leer el documento HTML.
    html_text = HTML_FILE.read_text(
        encoding="utf-8",
        errors="replace"
    )

    # Procesar la información.
    result = extract_product_data(html_text)

    # Crear la carpeta de resultados si no existe.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Exportar los datos en formato JSON.
    OUTPUT_FILE.write_text(
        json.dumps(result, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    print("Extracción local completada.")
    print(json.dumps(result, ensure_ascii=False, indent=4))
    print(f"\nResultado guardado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
