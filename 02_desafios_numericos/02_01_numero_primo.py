def es_numero_primo(numero):
    """Regresa el valor booleano True si es el numero es primo, de lo contrario
    devuelve False.
    Argumentos:
    numero -- debe ser integer
    return valor booleano True/False"""
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(es_numero_primo(3)) # True
print(es_numero_primo(12)) # False
print(es_numero_primo(43)) # True
