"""
Ejemplo de uso de la librería de álgebra lineal
===============================================

Este archivo muestra cómo usar las clases Vector y Matrix,
y las funciones de la librería LAC (Linear Algebra Course).

NOTA: Este archivo es solo para referencia. Las funciones no están implementadas
y devolverán errores hasta que los estudiantes las completen.
"""

from linearAlg import Vector, Matrix
from linearAlg import dot_product, magnitude, normalize, cross_product, angle_between
from linearAlg import scale, add, subtract, vector_multiply, matrix_multiply
from linearAlg import transpose, determinant, inverse, identity_matrix, zeros_matrix, ones_matrix

def ejemplo_vectores():
    """Ejemplos de uso de la clase Vector."""
    print("=== EJEMPLOS DE VECTORES ===")
    
    # Crear vectores
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}")
    
    # Operaciones básicas
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 / 2 = {v1 / 2}")
    
    # Propiedades
    print(f"Magnitud de v1: {v1.magnitude}")
    print(f"Vector unitario de v1: {v1.unit_vector}")
    
    # Productos
    print(f"Producto punto v1 · v2: {v1.dot(v2)}")
    print(f"Producto cruz v1 × v2: {v1.cross(v2)}")
    print(f"Ángulo entre v1 y v2: {v1.angle_with(v2)} radianes")
    
    # Usando funciones del módulo
    print(f"Producto punto (función): {dot_product(v1, v2)}")
    print(f"Magnitud (función): {magnitude(v1)}")
    print(f"Vector normalizado (función): {normalize(v1)}")


def ejemplo_matrices():
    """Ejemplos de uso de la clase Matrix."""
    print("\n=== EJEMPLOS DE MATRICES ===")
    
    # Crear matrices
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    v = Vector([1, 2])
    
    print(f"Matriz m1:\n{m1}")
    print(f"Matriz m2:\n{m2}")
    print(f"Vector v: {v}")
    
    # Propiedades básicas
    print(f"Forma de m1: {m1.shape}")
    print(f"Número de filas: {m1.num_rows}")
    print(f"Número de columnas: {m1.num_columns}")
    
    # Operaciones básicas
    print(f"m1 + m2:\n{m1 + m2}")
    print(f"m1 - m2:\n{m1 - m2}")
    print(f"m1 * 2:\n{m1 * 2}")
    
    # Propiedades avanzadas
    print(f"Transpuesta de m1:\n{m1.T}")
    print(f"Traza de m1: {m1.trace}")
    print(f"Determinante de m1: {m1.determinant}")
    print(f"¿Es cuadrada?: {m1.is_square()}")
    
    # Multiplicaciones
    print(f"m1 * v:\n{m1 * v}")
    print(f"m1 * m2:\n{m1 * m2}")
    
    # Usando funciones del módulo
    print(f"Suma (función):\n{add(m1, m2)}")
    print(f"Multiplicación matriz-vector (función):\n{vector_multiply(m1, v)}")
    print(f"Multiplicación matriz-matriz (función):\n{matrix_multiply(m1, m2)}")


def ejemplo_matrices_especiales():
    """Ejemplos de creación de matrices especiales."""
    print("\n=== MATRICES ESPECIALES ===")
    
    # Matriz identidad
    I = identity_matrix(3)
    print(f"Matriz identidad 3x3:\n{I}")
    
    # Matriz de ceros
    zeros = zeros_matrix(2, 3)
    print(f"Matriz de ceros 2x3:\n{zeros}")
    
    # Matriz de unos
    ones = ones_matrix(3, 2)
    print(f"Matriz de unos 3x2:\n{ones}")


if __name__ == "__main__":
    print("Ejemplos de uso de la librería de álgebra lineal")
    print("=" * 50)
    
    try:
        ejemplo_vectores()
        ejemplo_matrices()
        ejemplo_matrices_especiales()
    except NotImplementedError:
        print("\n¡Las funciones aún no están implementadas!")
        print("Los estudiantes deben completar las implementaciones en linAlg.py")
    except Exception as e:
        print(f"\nError: {e}")
        print("Asegúrate de que las funciones estén implementadas correctamente.")
