def encontrar_duplicados(lista):
    """Regresa una lista con los valores duplicados.
    Argumentos
    lista -- tipo similar en los valores de la lista de entrada
    return lista duplicados
    """
    elementos_lista = []
    duplicados = []

    for elemento in lista:
        if elemento in elementos_lista:
            duplicados.append(elemento)
        else:
            elementos_lista.append(elemento)
    return duplicados

print(encontrar_duplicados(["ana", "paco", "paco", "emilio", "javier", "ana"])) # ["paco", "ana"]
# ["paco", "ana"]
print(encontrar_duplicados(["1", "3", "6", "3", "2", "6"])) #["3","6"]
print(encontrar_duplicados([1, 3, 6, 3, 2, 6]))  # [3,6]
