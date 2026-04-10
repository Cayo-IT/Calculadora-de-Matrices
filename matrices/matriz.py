class Matriz:
    def __init__(self, values):
        size 
        #for i in range(0, len(values)):
        cols = None
        for row in values:
            if cols == None:
                cols = len(row)
            elif cols != len(row):
                    raise ValueError("La matriz debe de tener las mismas columnas en cada fila")
            
        if cols == 0:
             raise ValueError("Las filas deben tener al menos una columna..")
        self.values = values
        self.columns = cols
        self.rows = len(values)

    def __getitem__(self, index):
         if index < 0 or index >= self.rows:
              raise IndexError(f"Indice para fila fuera de rango! ({index})")
         return self.values[index]
    
    #rebase github