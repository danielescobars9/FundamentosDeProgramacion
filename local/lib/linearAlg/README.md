# Librería de Álgebra Lineal (LAC)

Una librería personalizada para operaciones de álgebra lineal desarrollada como proyecto educativo para el curso de Fundamentos de Programación.

## Estructura del proyecto

```
linearAlg/
├── __init__.py          # Configuración del módulo y exportaciones
├── linAlg.py           # Implementación principal de clases y funciones
├── ejemplo_uso.py      # Ejemplos de cómo usar la librería
└── README.md           # Esta documentación
```

## Clases principales

### Vector
Representa un vector matemático con sus componentes.

**Propiedades principales:**
- `magnitude`: Magnitud del vector
- `unit_vector`: Vector normalizado

**Métodos principales:**
- `dot(other)`: Producto punto
- `cross(other)`: Producto cruz (vectores 3D)
- `angle_with(other)`: Ángulo entre vectores

**Operadores soportados:**
- `+`, `-`: Suma y resta de vectores
- `*`, `/`: Multiplicación y división por escalar
- `==`, `!=`: Comparación de vectores

### Matrix
Representa una matriz matemática.

**Propiedades principales:**
- `num_rows`, `num_columns`: Dimensiones
- `shape`: Forma como tupla (filas, columnas)
- `T`: Transpuesta
- `trace`: Traza (suma diagonal)
- `determinant`: Determinante
- `inverse`: Matriz inversa

**Métodos principales:**
- `is_square()`: Verifica si es cuadrada
- `is_symmetric()`: Verifica si es simétrica
- `get_row(index)`, `get_column(index)`: Obtiene fila/columna

**Operadores soportados:**
- `+`, `-`: Suma y resta de matrices
- `*`: Multiplicación (matriz-matriz, matriz-vector, matriz-escalar)
- `==`, `!=`: Comparación de matrices

## Funciones del módulo

### Funciones de Vector
- `dot_product(v1, v2)`: Producto punto
- `magnitude(v)`: Magnitud
- `normalize(v)`: Normalización
- `cross_product(v1, v2)`: Producto cruz
- `angle_between(v1, v2)`: Ángulo entre vectores

### Funciones de Matrix
- `scale(matrix, scalar)`: Multiplicación por escalar
- `add(m1, m2)`: Suma de matrices
- `subtract(m1, m2)`: Resta de matrices
- `vector_multiply(matrix, vector)`: Multiplicación matriz-vector
- `matrix_multiply(m1, m2)`: Multiplicación matriz-matriz
- `transpose(matrix)`: Transpuesta
- `determinant(matrix)`: Determinante
- `inverse(matrix)`: Matriz inversa

### Funciones de creación
- `identity_matrix(size)`: Matriz identidad
- `zeros_matrix(rows, cols)`: Matriz de ceros
- `ones_matrix(rows, cols)`: Matriz de unos

## Ejemplo de uso

```python
from linearAlg import Vector, Matrix
from linearAlg import dot_product, matrix_multiply, identity_matrix

# Crear vectores
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Operaciones con vectores
resultado = v1 + v2
producto_punto = dot_product(v1, v2)
magnitud = v1.magnitude

# Crear matrices
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Operaciones con matrices
suma = m1 + m2
producto = matrix_multiply(m1, m2)
identidad = identity_matrix(3)
```

## Criterios de evaluación

- **Clase Vector (30%)**
  - Constructor y métodos básicos
  - Operadores aritméticos
  - Propiedades como `magnitude`
  - Métodos como `dot()`, `cross()`

- **Funciones de vector (20%)**
  - `dot_product`, `magnitude`, `normalize`
  - `cross_product`, `angle_between`

- **Clase Matrix**
  - Propiedades básicas `num_columns`, `num_rows`, `shape` (5%)
  - Propiedades `T`, `trace` (10%)
  - Propiedad `determinant` (15%)
  - Operadores `__add__`, `__mul__`, etc. (3%)

- **Funciones de matriz**
  - `scale`, `add`, `subtract` (5%)
  - `vector_multiply` (5%)
  - `matrix_multiply` (7%)

## Notas para estudiantes

1. **Todas las funciones están declaradas pero vacías** - necesitas implementarlas
2. **Usa `pass` como placeholder** - reemplázalo con tu código
3. **Valida entradas** - considera casos como dimensiones incompatibles
4. **Maneja errores** - usa excepciones apropiadas para casos inválidos
5. **Documenta tu código** - usa docstrings y comentarios
6. **Prueba tu código** - usa `ejemplo_uso.py` como referencia

## Consejos de implementación

1. **Empieza por lo básico**: Constructor de Vector, operadores simples
2. **Valida dimensiones**: Antes de operar, verifica que las dimensiones sean compatibles
3. **Reutiliza código**: Las funciones pueden usar los métodos de las clases
4. **Maneja casos especiales**: Vectores vacíos, matrices no cuadradas, etc.
5. **Usa comprensiones de lista**: Son útiles para operaciones elemento por elemento
