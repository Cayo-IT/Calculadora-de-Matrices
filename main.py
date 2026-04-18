'''
Calculadora de Matrices
-Entrada de matrices: Por archivo, por consola 
-Operaciones:
Suma, Resta,  Multiplicacion por escalar, Multiplicacion de Matrices,
Matriz inversa, Transpuesta
-Solucion de sistema de ecuaciones lineales con matriz inversa
-Validacion de entrada del usuario:
Verificar entrada, Dar mensajes de error, Repetir la solicitud de entrada
-Guardar resultados en un archivo 
Modulos:
-Validacion de una matriz
-Entrada y salida de matrices en archivos
-Operaciones de matrices
-Main
-Interfaz de usuario 
'''

from matrices.matriz import Matriz
from entradas.lectura import guardar_resultado
import matrices.operaciones as op
from entradas.input_validacion import obtener_matriz, obtener_escalar

def mostrar_menu():
    print("\nCALCULADORA DE MATRICES")
    print("-"*45)
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación por escalar")
    print("4. Multiplicación de matrices")
    print("5. Matriz inversa")
    print("6. Matriz transpuesta")
    print("7. Solucion de sistema de ecuaciones lineales")
    print("8. Salir")
    print("-"*45)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-8): ").strip()
        if opcion == '8':
            print("Gracias por utilizar la calculadora de matrices!")
            break
        if opcion not in [str(i) for i in range(1, 9)]:
            print("Opcion invalida. Intentalo de nuevo.")
            continue  
        try:
            resultado = None
            if opcion in ['1', '2', '4']:
                m1 = obtener_matriz("Matriz 1")
                m2 = obtener_matriz("Matriz 2")
                if opcion == '1': resultado = op.sumar_matrices(m1, m2)
                elif opcion == '2': resultado = op.restar_matrices(m1, m2)
                elif opcion == '4': resultado = op.multiplicar_matrices(m1, m2)
            elif opcion == '3':
                m1 = obtener_matriz()
                escalar = obtener_escalar()
                resultado = op.multiplicacion_escalar(m1, escalar)
            elif opcion in ['5', '6']:
                m1 = obtener_matriz()
                if opcion == '5': resultado = op.inversa(m1)
                elif opcion == '6': resultado = op.transpuesta(m1)
            elif opcion == '7':
                print("Para resolver un sistema Ax = B, necesitamos la Matriz A y el vector B.")
                A = obtener_matriz("Matriz de coeficientes (A)")
                B = obtener_matriz("Vector de constantes (B) (ingresalo como una columna)")
                #solucion de Ax=B a traves de matriz inversa: x = A^(-1) * B
                resultado = op.multiplicar_matrices(op.inversa(A), B)
            print("\nEl resultado de la operacion es:\n")
            print(resultado)
            guardar = input("\nDeseas guardar el resultado en un archivo? (S/N): ").strip().upper()
            if guardar == 'S':
                ruta_guardado = input("Ingresa la ruta y nombre de destino (ej. resultado.txt): ")
                guardar_resultado(resultado, ruta_guardado)
        except Exception as e:
            print(f"\n[ERROR EN LA OPERACION]: {e}")

if __name__ == "__main__":
    main()