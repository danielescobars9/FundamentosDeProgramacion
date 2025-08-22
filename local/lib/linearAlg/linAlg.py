"""
Módulo principal de la librería de álgebra lineal
=================================================

Este módulo contiene las implementaciones de las clases Vector y Matrix,
así como las funciones de álgebra lineal asociadas.
"""

import math
from typing import List, Union, Tuple, Optional


class Vector:
    """
    Clase para representar y manipular vectores.
    
    Un vector es una lista de números que puede representar
    puntos en el espacio, direcciones, o cualquier secuencia ordenada de valores.
    """
    
    def __init__(self, components: List[Union[int, float]]):
        """
        Inicializa un vector con sus componentes.
        
        Args:
            components: Lista de números que representan las componentes del vector
        """
        pass
    
    def __str__(self) -> str:
        """Representación en string del vector."""
        pass
    
    def __repr__(self) -> str:
        """Representación detallada del vector."""
        pass
    
    def __len__(self) -> int:
        """Retorna la dimensión del vector."""
        pass
    
    def __getitem__(self, index: int) -> Union[int, float]:
        """Permite acceder a los componentes del vector usando índices."""
        pass
    
    def __setitem__(self, index: int, value: Union[int, float]):
        """Permite modificar componentes del vector usando índices."""
        pass
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """Suma de vectores usando el operador +."""
        pass
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Resta de vectores usando el operador -."""
        pass
    
    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        """Multiplicación por escalar usando el operador *."""
        pass
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        """Multiplicación por escalar (orden invertido)."""
        pass
    
    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        """División por escalar usando el operador /."""
        pass
    
    def __eq__(self, other: 'Vector') -> bool:
        """Igualdad entre vectores usando el operador ==."""
        pass
    
    def __ne__(self, other: 'Vector') -> bool:
        """Desigualdad entre vectores usando el operador !=."""
        pass
    
    @property
    def magnitude(self) -> float:
        """Calcula y retorna la magnitud (norma) del vector."""
        pass
    
    @property
    def unit_vector(self) -> 'Vector':
        """Retorna el vector unitario (normalizado)."""
        pass
    
    def dot(self, other: 'Vector') -> float:
        """
        Calcula el producto punto con otro vector.
        
        Args:
            other: Otro vector para el producto punto
            
        Returns:
            El producto punto como un número
        """
        pass
    
    def cross(self, other: 'Vector') -> 'Vector':
        """
        Calcula el producto cruz con otro vector (solo para vectores 3D).
        
        Args:
            other: Otro vector para el producto cruz
            
        Returns:
            Un nuevo vector resultado del producto cruz
        """
        pass
    
    def angle_with(self, other: 'Vector') -> float:
        """
        Calcula el ángulo entre este vector y otro.
        
        Args:
            other: Otro vector
            
        Returns:
            El ángulo en radianes
        """
        pass


class Matrix:
    """
    Clase para representar y manipular matrices.
    
    Una matriz es una colección rectangular de números organizados en filas y columnas.
    """
    
    def __init__(self, data: List[List[Union[int, float]]]):
        """
        Inicializa una matriz con sus datos.
        
        Args:
            data: Lista de listas que representa las filas de la matriz
        """
        pass
    
    def __str__(self) -> str:
        """Representación en string de la matriz."""
        pass
    
    def __repr__(self) -> str:
        """Representación detallada de la matriz."""
        pass
    
    def __getitem__(self, key: Union[int, Tuple[int, int]]) -> Union[List[Union[int, float]], Union[int, float]]:
        """Permite acceder a filas o elementos específicos de la matriz."""
        pass
    
    def __setitem__(self, key: Union[int, Tuple[int, int]], value: Union[List[Union[int, float]], Union[int, float]]):
        """Permite modificar filas o elementos específicos de la matriz."""
        pass
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Suma de matrices usando el operador +."""
        pass
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Resta de matrices usando el operador -."""
        pass
    
    def __mul__(self, other: Union['Matrix', 'Vector', int, float]) -> Union['Matrix', 'Vector']:
        """Multiplicación de matrices/vectores/escalares usando el operador *."""
        pass
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Matrix':
        """Multiplicación por escalar (orden invertido)."""
        pass
    
    def __eq__(self, other: 'Matrix') -> bool:
        """Igualdad entre matrices usando el operador ==."""
        pass
    
    def __ne__(self, other: 'Matrix') -> bool:
        """Desigualdad entre matrices usando el operador !=."""
        pass
    
    @property
    def num_rows(self) -> int:
        """Retorna el número de filas de la matriz."""
        pass
    
    @property
    def num_columns(self) -> int:
        """Retorna el número de columnas de la matriz."""
        pass
    
    @property
    def shape(self) -> Tuple[int, int]:
        """Retorna las dimensiones de la matriz como (filas, columnas)."""
        pass
    
    @property
    def T(self) -> 'Matrix':
        """Retorna la transpuesta de la matriz."""
        pass
    
    @property
    def trace(self) -> Union[int, float]:
        """Calcula y retorna la traza de la matriz (suma de elementos diagonales)."""
        pass
    
    @property
    def determinant(self) -> Union[int, float]:
        """Calcula y retorna el determinante de la matriz."""
        pass
    
    @property
    def inverse(self) -> 'Matrix':
        """Calcula y retorna la matriz inversa."""
        pass
    
    def is_square(self) -> bool:
        """Verifica si la matriz es cuadrada."""
        pass
    
    def is_symmetric(self) -> bool:
        """Verifica si la matriz es simétrica."""
        pass
    
    def is_diagonal(self) -> bool:
        """Verifica si la matriz es diagonal."""
        pass
    
    def get_row(self, index: int) -> 'Vector':
        """
        Obtiene una fila específica como vector.
        
        Args:
            index: Índice de la fila
            
        Returns:
            Vector con los elementos de la fila
        """
        pass
    
    def get_column(self, index: int) -> 'Vector':
        """
        Obtiene una columna específica como vector.
        
        Args:
            index: Índice de la columna
            
        Returns:
            Vector con los elementos de la columna
        """
        pass


# =============================================================================
# FUNCIONES DE VECTOR
# =============================================================================

def dot_product(v1: Vector, v2: Vector) -> float:
    """
    Calcula el producto punto entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El producto punto como un número
    """
    pass


def magnitude(v: Vector) -> float:
    """
    Calcula la magnitud (norma) de un vector.
    
    Args:
        v: El vector
        
    Returns:
        La magnitud del vector
    """
    pass


def normalize(v: Vector) -> Vector:
    """
    Normaliza un vector (lo convierte en vector unitario).
    
    Args:
        v: El vector a normalizar
        
    Returns:
        Un nuevo vector normalizado
    """
    pass


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calcula el producto cruz entre dos vectores 3D.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        Un nuevo vector resultado del producto cruz
    """
    pass


def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calcula el ángulo entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El ángulo en radianes
    """
    pass


# =============================================================================
# FUNCIONES DE MATRIZ
# =============================================================================

def scale(matrix: Matrix, scalar: Union[int, float]) -> Matrix:
    """
    Multiplica una matriz por un escalar.
    
    Args:
        matrix: La matriz
        scalar: El escalar
        
    Returns:
        Una nueva matriz escalada
    """
    pass


def add(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Suma dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la suma
    """
    pass


def subtract(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Resta dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la resta
    """
    pass


def vector_multiply(matrix: Matrix, vector: Vector) -> Vector:
    """
    Multiplica una matriz por un vector.
    
    Args:
        matrix: La matriz
        vector: El vector
        
    Returns:
        Un nuevo vector resultado de la multiplicación
    """
    pass


def matrix_multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiplica dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la multiplicación
    """
    pass


def transpose(matrix: Matrix) -> Matrix:
    """
    Calcula la transpuesta de una matriz.
    
    Args:
        matrix: La matriz
        
    Returns:
        Una nueva matriz transpuesta
    """
    pass


def determinant(matrix: Matrix) -> Union[int, float]:
    """
    Calcula el determinante de una matriz cuadrada.
    
    Args:
        matrix: La matriz cuadrada
        
    Returns:
        El determinante
    """
    pass


def inverse(matrix: Matrix) -> Matrix:
    """
    Calcula la matriz inversa.
    
    Args:
        matrix: La matriz cuadrada invertible
        
    Returns:
        Una nueva matriz inversa
    """
    pass


def identity_matrix(size: int) -> Matrix:
    """
    Crea una matriz identidad de tamaño especificado.
    
    Args:
        size: El tamaño de la matriz (size x size)
        
    Returns:
        Una nueva matriz identidad
    """
    pass


def zeros_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de ceros con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de ceros
    """
    pass


def ones_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de unos con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de unos
    """
    pass
