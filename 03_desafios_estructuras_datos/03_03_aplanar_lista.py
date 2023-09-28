def aplanar_lista(lista):
    """Regresa una lista de una sola dimensión.
    Argumentos:
    lista -- debe ser una lista anidada
    nueva_lista -- una dimensión"""
    nueva_lista = []
    for elemento in lista:
        if isinstance(elemento, list):
            nueva_lista.extend(aplanar_lista(elemento))
        else:
            nueva_lista.append(elemento)
        """
        #Opción para dos dimensiones
        if type(elemento) is list:
            nueva_lista.extend(elemento)
        else:
            nueva_lista.append(elemento)
        """
    return nueva_lista


print(aplanar_lista([2, 3, 4, [3, 2]]))  # [2, 3, 4, 3, 2]
print(aplanar_lista([2, 3, 4, [[2]]]))  # [2, 3, 4, 2]
