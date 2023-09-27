def es_palindromo(texto):
    """Regresa valor booleando a fin de verificar si el enunciado es palindrome.
    Argumentos:
    texto -- debe ser string
    """
    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False
