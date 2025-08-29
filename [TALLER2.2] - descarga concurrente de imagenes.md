# Descarga concurrente de imágenes

En este taller pondrás a prueba lo que aprendiste sobre concurrencia y manipulación de archivos. Tu tarea será descargar un conjunto de archivos utilizando las 3 formas de concurrencia disponibles en Python. 

Se deberá descargar un conjunto de archivos que permitan comparar la duración total del proceso en las diferentes modalidades de operación.

### Imágenes de Unsplash
```python
image_urls = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
    "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800"
]
```

### Imágenes aleatorias (Lorem Picsum)
```python
random_image_urls = [
    "https://picsum.photos/800/600?random=1",
    "https://picsum.photos/800/600?random=2",
    "https://picsum.photos/800/600?random=3",
    "https://picsum.photos/1200/800?random=4",
    "https://picsum.photos/1200/800?random=5",
]
```

### Datos JSON (APIs públicas)
```python
json_urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/albums/1",
    "https://api.github.com/users/octocat",
    "https://httpbin.org/json",
]
```

### Archivos CSV de datos
```python
csv_urls = [
    "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv",
    "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv",
    "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv",
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv",
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv",
]
```

### Archivos de texto y documentos
```python
text_urls = [
    "https://www.gutenberg.org/files/11/11-0.txt",  # Alice in Wonderland
    "https://www.gutenberg.org/files/84/84-0.txt",  # Frankenstein
    "https://raw.githubusercontent.com/python/cpython/main/README.rst",
    "https://raw.githubusercontent.com/microsoft/vscode/main/README.md",
    "https://raw.githubusercontent.com/tensorflow/tensorflow/master/README.md",
]
```

### Archivos XML y RSS
```python
xml_urls = [
    "https://rss.cnn.com/rss/edition.rss",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.w3schools.com/xml/note.xml",
    "https://www.w3schools.com/xml/books.xml",
]
```

### Archivos PDF (pequeños)
```python
pdf_urls = [
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://www.africau.edu/images/default/sample.pdf",
    "https://www.orimi.com/pdf-test.pdf",
]
```

### Archivos de audio (pequeños)
```python
audio_urls = [
    "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
]
```

### Archivos comprimidos
```python
zip_urls = [
    "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip",
    "https://github.com/python/cpython/archive/refs/heads/main.zip",
]
```

### Archivos de configuración y código
```python
config_urls = [
    "https://raw.githubusercontent.com/django/django/main/setup.cfg",
    "https://raw.githubusercontent.com/pallets/flask/main/pyproject.toml",
    "https://raw.githubusercontent.com/numpy/numpy/main/requirements.txt",
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/setup.py",
]
```

### Archivos de imagen en diferentes formatos
```python
various_image_formats = [
    "https://via.placeholder.com/800x600.png",
    "https://via.placeholder.com/800x600.jpg", 
    "https://via.placeholder.com/800x600.gif",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
]
```

### APIs que devuelven diferentes tipos de datos
```python
api_urls = [
    "https://httpbin.org/xml",           # XML
    "https://httpbin.org/json",          # JSON
    "https://httpbin.org/html",          # HTML
    "https://httpbin.org/robots.txt",    # Texto plano
    "https://api.quotegarden.com/api/v3/quotes/random",  # API de citas
]
```

## Sugerencias adicionales

**Tip**: Puedes combinar diferentes tipos de archivos para hacer el ejercicio más interesante:

```python
mixed_urls = [
    # Imágenes
    "https://picsum.photos/600/400?random=1",
    "https://picsum.photos/600/400?random=2",
    # JSON
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    # CSV
    "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv",
    # Texto
    "https://raw.githubusercontent.com/python/cpython/main/README.rst",
    # XML
    "https://httpbin.org/xml",
    # PDF
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
]


## Evaluación

- Implementación de la versión usando `multiprocessing`: 30%
- Implementación de la versión usando `threading`: 30%
- Implementación usando `asyncio`: 40%

Muchos éxitos!