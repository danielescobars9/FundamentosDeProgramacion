# -*- coding: utf-8 -*-
"""
Modulo de calculadora simple
Contiene funciones basicas de matematicas
"""

def sumar(a, b):
    """Suma dos numeros"""
    return a + b

def restar(a, b):
    """Resta dos numeros"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos numeros"""
    return a * b

def dividir(a, b):
    """Divide dos numeros"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Constante del modulo
VERSION = "1.0.0"

# Variable privada (por convencion, no deberia importarse)
_contador_operaciones = 0

def obtener_contador():
    """Obtiene el numero de operaciones realizadas"""
    global _contador_operaciones
    return _contador_operaciones