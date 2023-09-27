def es_anagrama(palabra_1, palabra_2):
    """
    Regresa el valor booleano True si las dos palabras contienen las mismas letras
    De lo contrario, regresa False
    Argumentos:
    palabra_1 -- Debe ser string
    palabra_2 -- Debe ser string
    return True or False
    """
    letras_palabra_1 = sorted(palabra_1.lower())
    letras_palabra_2 = sorted(palabra_2.lower())
    # print(letras_palabra_1,letras_palabra_2)
    return letras_palabra_1 == letras_palabra_2


print(es_anagrama("lama", "Mala"))   # True
print(es_anagrama("calor", "coral")) # True
print(es_anagrama("cama", "casa"))   # False
