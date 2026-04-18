from entradas.lectura import leer_matriz_archivo, leer_matriz_consola

def obtener_matriz(nombre="Matriz"):
    """Maneja la lógica y las re-solicitudes para obtener una matriz de forma segura."""
    while True:
        print(f"\n--- Ingresando {nombre} ---")
        metodo = input("¿Deseas ingresar por (A)rchivo o por (C)onsola? (A/C): ").strip().upper()
        try:
            if metodo == 'A':
                ruta = input("Ingresa la ruta absoluta o relativa del archivo: ")
                return leer_matriz_archivo(ruta)
            elif metodo == 'C':
                return leer_matriz_consola()
            else:
                print("Opción inválida. Elige A o C.")
        except Exception as e:
            print(f"[ERROR]: {e}\nPor favor, intenta de nuevo.")

def obtener_escalar():
    while True:
        try:
            return float(input("Ingresa el valor del escalar: "))
        except ValueError:
            print("[ERROR]: Entrada inválida. Por favor, ingresa solo números.")
