
"""
Pruebas automatizadas del módulo de extracción.
"""

from src.scraping import extract_product_data


def test_extraer_datos_producto():
    """Verifica la extracción de los campos principales."""

    html = """
    <html>
        <body>
            <h1>Portátil SUXI 2026</h1>

            <span itemprop="price" content="900646">
                900646
            </span>

            <span itemprop="ratingValue" content="5.0">
                5.0
            </span>

            <span itemprop="reviewCount" content="5">
                5
            </span>
        </body>
    </html>
    """

    resultado = extract_product_data(html)

    assert resultado["titulo"] == "Portátil SUXI 2026"
    assert resultado["precio"] == "900646"
    assert resultado["calificacion"] == "5.0"
    assert resultado["cantidad_resenas"] == "5"


def test_html_sin_datos():
    """Verifica que el programa gestione HTML sin información."""

    html = "<html><body><p>Sin datos</p></body></html>"

    resultado = extract_product_data(html)

    assert resultado["titulo"] is None
    assert resultado["precio"] is None
    assert resultado["calificacion"] is None
    assert resultado["cantidad_resenas"] is None
