def ordenamiento_burbuja(lista):
    """Regresa la lista ordenada mediante el metodo burbuja 
    por medio de la comparación de los elementos.
    Argumentos:
    lista -- Debe contener unicamente valores enteros
    return lista ordenada
    """
    temporal = 0
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal
    return lista

print(ordenamiento_burbuja([3,8,4,1,2])) # [1, 2, 3, 4, 8]
