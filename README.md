
# Análisis de productos de comercio electrónico mediante Web Scraping

## 1. Descripción del proyecto

Este proyecto tiene como finalidad aplicar técnicas de extracción y procesamiento de información mediante Python y BeautifulSoup, tomando como referencia un producto publicado en la plataforma de comercio electrónico Temu.

El artículo seleccionado para el análisis es un portátil SUXI 2026 de 15,6 pulgadas. Se consideran campos como el título, el precio, la calificación y la cantidad de reseñas.

La extracción implementada se prueba sobre un documento HTML local de ejemplo construido con información observada en la publicación. No realiza solicitudes automatizadas directamente a Temu.

## 2. Objetivos

- Organizar información de productos de comercio electrónico.
- Aplicar BeautifulSoup para analizar documentos HTML.
- Estructurar los datos obtenidos en formato JSON.
- Implementar pruebas automatizadas mediante Pytest.
- Gestionar el código fuente utilizando Git y GitHub.
- Automatizar la validación del proyecto mediante GitHub Actions.

## 3. Tecnologías utilizadas

- Python.
- BeautifulSoup.
- Pytest.
- Git.
- GitHub.
- GitHub Actions.

## 4. Estructura del proyecto

```text
web-scraping-temu-devops/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── data/
│   └── pagina_autorizada.html
│
├── docs/
│
├── results/
│   └── resultado_extraccion.json
│
├── src/
│   └── scraping.py
│
├── tests/
│   └── test_scraping.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Instalación y configuración

Clonar el repositorio:

```bash
git clone https://github.com/Sebastianll56/web-scraping-temu-devops.git
```

Ingresar al directorio:

```bash
cd web-scraping-temu-devops
```

Crear el entorno virtual:

```bash
python -m venv .venv
```

Instalar las dependencias:

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

## 6. Ejecución del proyecto

Ejecutar el módulo principal:

```bash
.venv/Scripts/python.exe src/scraping.py
```

Los resultados se almacenan en:

```text
results/resultado_extraccion.json
```

## 7. Pruebas automatizadas

Para ejecutar las pruebas:

```bash
.venv/Scripts/python.exe -m pytest -v
```

Las pruebas verifican la extracción de los campos principales y el comportamiento del programa cuando el documento HTML no contiene los datos esperados.

## 8. Integración continua

El proyecto utiliza GitHub Actions mediante el archivo:

`.github/workflows/ci-cd.yml`

El flujo se activa cuando se realizan cambios mediante `push` o `pull_request` dirigidos a la rama principal.

El proceso configura Python, instala las dependencias y ejecuta las pruebas automatizadas con Pytest.

## 9. Consideraciones sobre los datos

La práctica utiliza un HTML local de demostración con información transcrita de una captura del producto SUXI 2026.

Los resultados no constituyen una extracción en vivo ni una verificación independiente de la publicación de Temu. Cualquier automatización directa deberá respetar las condiciones de acceso y uso de la plataforma.

## 10. Autor

Sebastian Londoño Londoño

Proyecto académico de Programación para Análisis de Datos.

IU DIGITAL DE ANTIOQUIA.
