import numpy as np
from matrices.matriz import Matriz

def sumar_matrices(m1, m2):
    if m1.rows != m2.rows or m1.columns != m2.columns:
        raise ValueError("Las matrices deben tener el mismo tamaño para sumar.")
    return Matriz([[m1.values[i][j] + m2.values[i][j] for j in range(m1.columns)] for i in range(m1.rows)])

def restar_matrices(m1, m2):
    if m1.rows != m2.rows or m1.columns != m2.columns:
        raise ValueError("Las matrices deben tener el mismo tamaño para restar.")
    return Matriz([[m1.values[i][j] - m2.values[i][j] for j in range(m1.columns)] for i in range(m1.rows)])

def multiplicacion_escalar(m, escalar):
    return Matriz([[m.values[i][j] * escalar for j in range(m.columns)] for i in range(m.rows)])

def multiplicar_matrices(m1, m2):
    if m1.columns != m2.rows:
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")
    resultado = [[sum(m1.values[i][k] * m2.values[k][j] for k in range(m1.columns)) for j in range(m2.columns)] for i in range(m1.rows)]
    return Matriz(resultado)

def transpuesta(m):
    return Matriz([[m.values[j][i] for j in range(m.rows)] for i in range(m.columns)])

def inversa(m):
    np_mat = np.array(m.values)
    if m.rows != m.columns:
        raise ValueError("La matriz debe ser cuadrada para poder calcular su inversa.")
    try:
        inv = np.linalg.inv(np_mat)
        return Matriz(inv.tolist())
    except np.linalg.LinAlgError:
        raise ValueError("La matriz no es invertible (su determinante es 0).")
