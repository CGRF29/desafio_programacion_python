def calcular_factorial(numero):
    """
    Regresa el factorial de un numero.
    Argumentos:
    numero -- Debe ser entero
    factorial -- Debe ser entero
    """
    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i
    return factorial

def calcular_factorial_recursivo(numero):
    """
    Regresa el factorial de un numero.
    Argumentos:
    numero -- Debe ser entero
    factorial -- Debe ser entero
    """
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_factorial_recursivo(numero-1)


print('Ciclo for:',calcular_factorial(0),'- Recursivo:', calcular_factorial_recursivo(0))  # 1
print('Ciclo for:',calcular_factorial(3),'- Recursivo:',calcular_factorial_recursivo(3))  # 6
print('Ciclo for:',calcular_factorial(4),'- Recursivo:',calcular_factorial_recursivo(4))  # 24
print('Ciclo for:', calcular_factorial(5),'- Recursivo:',calcular_factorial_recursivo(5))  # 120

