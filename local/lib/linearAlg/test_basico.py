"""
Pruebas básicas para la librería de álgebra lineal
==================================================

Este archivo contiene pruebas simples que los estudiantes pueden usar
para verificar que sus implementaciones funcionan correctamente.

Para ejecutar las pruebas, simplemente ejecuta este archivo:
python test_basico.py
"""

def test_vector_basico():
    """Pruebas básicas para la clase Vector."""
    print("Probando clase Vector...")
    
    try:
        from linearAlg import Vector
        
        # Test constructor
        v1 = Vector([1, 2, 3])
        print("✓ Constructor Vector funciona")
        
        # Test __str__
        print(f"✓ Vector v1: {v1}")
        
        # Test __len__
        if hasattr(v1, '__len__'):
            print(f"✓ Longitud de v1: {len(v1)}")
        
        # Test suma
        v2 = Vector([4, 5, 6])
        if hasattr(v1, '__add__'):
            resultado = v1 + v2
            print(f"✓ Suma v1 + v2: {resultado}")
        
        # Test magnitud
        if hasattr(v1, 'magnitude'):
            mag = v1.magnitude
            print(f"✓ Magnitud de v1: {mag}")
            
    except Exception as e:
        print(f"✗ Error en Vector: {e}")


def test_matrix_basico():
    """Pruebas básicas para la clase Matrix."""
    print("\nProbando clase Matrix...")
    
    try:
        from linearAlg import Matrix
        
        # Test constructor
        m1 = Matrix([[1, 2], [3, 4]])
        print("✓ Constructor Matrix funciona")
        
        # Test __str__
        print(f"✓ Matriz m1:\n{m1}")
        
        # Test propiedades básicas
        if hasattr(m1, 'num_rows'):
            print(f"✓ Filas: {m1.num_rows}")
        
        if hasattr(m1, 'num_columns'):
            print(f"✓ Columnas: {m1.num_columns}")
        
        if hasattr(m1, 'shape'):
            print(f"✓ Forma: {m1.shape}")
        
        # Test transpuesta
        if hasattr(m1, 'T'):
            print(f"✓ Transpuesta:\n{m1.T}")
        
        # Test traza
        if hasattr(m1, 'trace'):
            print(f"✓ Traza: {m1.trace}")
            
    except Exception as e:
        print(f"✗ Error en Matrix: {e}")


def test_funciones_vector():
    """Pruebas básicas para funciones de vector."""
    print("\nProbando funciones de vector...")
    
    try:
        from linearAlg import Vector, dot_product, magnitude, normalize
        
        v1 = Vector([3, 4])
        v2 = Vector([1, 0])
        
        # Test producto punto
        try:
            dp = dot_product(v1, v2)
            print(f"✓ Producto punto: {dp}")
        except:
            print("✗ dot_product no implementado")
        
        # Test magnitud
        try:
            mag = magnitude(v1)
            print(f"✓ Magnitud: {mag}")
        except:
            print("✗ magnitude no implementado")
        
        # Test normalización
        try:
            norm = normalize(v1)
            print(f"✓ Vector normalizado: {norm}")
        except:
            print("✗ normalize no implementado")
            
    except Exception as e:
        print(f"✗ Error en funciones de vector: {e}")


def test_funciones_matrix():
    """Pruebas básicas para funciones de matriz."""
    print("\nProbando funciones de matriz...")
    
    try:
        from linearAlg import Matrix, Vector, add, scale, vector_multiply
        
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        v = Vector([1, 2])
        
        # Test suma
        try:
            suma = add(m1, m2)
            print(f"✓ Suma de matrices:\n{suma}")
        except:
            print("✗ add no implementado")
        
        # Test escalado
        try:
            escalada = scale(m1, 2)
            print(f"✓ Matriz escalada:\n{escalada}")
        except:
            print("✗ scale no implementado")
        
        # Test multiplicación matriz-vector
        try:
            mv = vector_multiply(m1, v)
            print(f"✓ Matriz × vector: {mv}")
        except:
            print("✗ vector_multiply no implementado")
            
    except Exception as e:
        print(f"✗ Error en funciones de matriz: {e}")


def test_matrices_especiales():
    """Pruebas para funciones de creación de matrices."""
    print("\nProbando matrices especiales...")
    
    try:
        from linearAlg import identity_matrix, zeros_matrix, ones_matrix
        
        # Test matriz identidad
        try:
            I = identity_matrix(3)
            print(f"✓ Matriz identidad 3x3:\n{I}")
        except:
            print("✗ identity_matrix no implementado")
        
        # Test matriz de ceros
        try:
            zeros = zeros_matrix(2, 3)
            print(f"✓ Matriz de ceros 2x3:\n{zeros}")
        except:
            print("✗ zeros_matrix no implementado")
        
        # Test matriz de unos
        try:
            ones = ones_matrix(2, 2)
            print(f"✓ Matriz de unos 2x2:\n{ones}")
        except:
            print("✗ ones_matrix no implementado")
            
    except Exception as e:
        print(f"✗ Error en matrices especiales: {e}")


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas básicas."""
    print("=" * 60)
    print("PRUEBAS BÁSICAS DE LA LIBRERÍA DE ÁLGEBRA LINEAL")
    print("=" * 60)
    
    test_vector_basico()
    test_matrix_basico()
    test_funciones_vector()
    test_funciones_matrix()
    test_matrices_especiales()
    
    print("\n" + "=" * 60)
    print("PRUEBAS COMPLETADAS")
    print("=" * 60)
    print("\nNota: Las funciones marcadas con ✗ necesitan ser implementadas.")
    print("Las funciones marcadas con ✓ están funcionando (al menos básicamente).")


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
