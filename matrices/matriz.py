class Matriz:
    def __init__(self, values):
        cols = None
        for row in values:
            if cols == None:
                cols = len(row)
            elif cols != len(row):
                    raise ValueError("La matriz debe de tener las mismas columnas en cada fila")
            
        if cols == 0:
             raise ValueError("Las filas deben tener al menos una columna")
        self.values = values
        self.columns = cols
        self.rows = len(values)

    def __getitem__(self, index):
         if index < 0 or index >= self.rows:
              raise IndexError(f"Indice para fila fuera de rango ({index})")
         return self.values[index]

    def __str__(self):
        #conviertir la matriz en una cadena de texto formateada.
        #crear una lista vacia que contendra las cadenas de cada fila.
        filas_formateadas = []
        for fila_numerica in self.values:
            #Para cada fila, se crea otra lista para los numeros convertidos a texto.
            items_en_texto = []
            for item in fila_numerica:
                #se redondea, convertimos a texto y añadimos a la lista de la fila.
                items_en_texto.append(str(round(item, 4)))
            
            #se une los numeros de la fila con una tabulacion para alinear las columnas.
            filas_formateadas.append('\t'.join(items_en_texto))
            
        #unimos todas las filas con un salto de linea.
        return '\n'.join(filas_formateadas)