import os
from pathlib import Path 

def read_file():
    archivo1 = Path(__file__).parent / ".." #Muestra la direccion exacta / ".." / "resources" / "matrices" / "matriz.txt"
    archivo2 = Path(os.getcwd()) #Esta es la carpeta en donde estoy trabajando / ".." / "resources" / "matrices"/ "matriz.txt"
    print("getcwd():", archivo1.resolve())
    print("__file__:", archivo2.resolve())

    #with open(archivo1.resolve(), "r") as readfile:
        #print(readfile.readlines())
if __name__ == "__main__":
    read_file()
