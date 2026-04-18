from entradas.lectura import leer_matriz_archivo, leer_matriz_consola

def obtener_matriz(nombre="Matriz"):
    while True:
        print(f"\n--- Ingresando {nombre} ---")
        metodo = input("Deseas ingresar por Archivo o por Consola? (A/C): ").strip().upper()
        try:
            if metodo == 'A':
                ruta = input("Ingresa la ruta absoluta o relativa del archivo: ")
                return leer_matriz_archivo(ruta)
            elif metodo == 'C':
                return leer_matriz_consola()
            else:
                print("Opcion invalida. Elige A o C.")
        except Exception as e:
            print(f"[ERROR]: {e}\n intenta de nuevo.")

def obtener_escalar():
    while True:
        try:
            return float(input("Ingresa el valor del escalar: "))
        except ValueError:
            print("[ERROR]: Entrada invalida. Ingresa solo numeros.")