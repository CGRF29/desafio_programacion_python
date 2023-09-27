def numero_triangular(fila):
    """Regresa la suma de los puntos correspondientes a cada fila.
    Argumentos:
    fila -- Debe ser entero
    triangular -- Debe ser entero"""
    triangular = 0
    for i in range(1, fila+1):
        #print(i)
        triangular += i
    return triangular


print(numero_triangular(2)) # 3
print(numero_triangular(4)) # 10
print(numero_triangular(6)) # 21
