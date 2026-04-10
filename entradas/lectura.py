import os
from pathlib import Path 

def read_file(ruta):
    archivo = Path(os.getcwd() / ".." / "resources" / matriz.txt)
    print(archivo.resolve())


    if __name__ == "__main__":
        read_file()
