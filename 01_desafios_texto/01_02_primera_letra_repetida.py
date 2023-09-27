def primera_letra_repetida(texto):
    """Regresa la primera letra repetida en un texto.
    Argumentos:
    texto -- Debe ser string
    letra -- Debe ser string
    """
    texto_minsucula = texto.lower()
    texto_sin_espacios = texto_minsucula.replace(" ", "")
    lista_letras = []
    for letra in texto_sin_espacios:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)

    return None



print(primera_letra_repetida("hola"))  # None
print(primera_letra_repetida("hola mundo"))   # o
