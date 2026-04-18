import os
from pathlib import Path 
from matrices.matriz import Matriz

def leer_matriz_archivo(ruta):
    #Lee una matriz desde un archivo de texto donde las columnas se separan por espacios y las filas por saltos de linea
    try:
        with open(ruta, "r") as f:
            valores = []
            for linea in f:
                fila = [float(x) for x in linea.strip().split()]
                if fila:
                    valores.append(fila)
            return Matriz(valores)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontro el archivo en la ruta: {ruta}")
    except ValueError:
        raise ValueError("El archivo contiene caracteres invalidos. Asegúrate de que solo existan numeros.")

def leer_matriz_consola():
    #Lee una matriz desde la consola pidiendole fila por fila al usuario
    print("Ingresa los valores de la matriz fila por fila (separa los numeros con un espacio).")
    print("Escribe 'fin' cuando hayas terminado de ingresar todas las filas.")
    valores = []
    while True:
        entrada = input("Fila (o 'fin'): ")
        if entrada.lower() == 'fin':
            if not valores:
                 print("La matriz no puede estar vacia. Intenta de nuevo.")
                 continue
            break
        try:
            fila = [float(x) for x in entrada.strip().split()]
            if fila: valores.append(fila)
        except ValueError:
            print("Error: ingresa solo numeros separados por espacios.")
    return Matriz(valores)

def guardar_resultado(matriz, ruta):
    with open(ruta, "w") as f:
        f.write(str(matriz) + "\n")
    print(f"Resultado guardado exitosamente en: {ruta}")
