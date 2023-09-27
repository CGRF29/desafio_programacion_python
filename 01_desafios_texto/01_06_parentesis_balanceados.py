def parentesis_balanceados(texto):
    """Indica si la cantidad de parentesis esta balanceada o no.
    Argumentos:
    texto -- Debe contener parentesis
    return Valor booleano True/ False correspondientemente."""        
    balance = 0
    for parentesis in texto:
        if parentesis == "(":
            balance += 1
        elif parentesis == ")":
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


print(parentesis_balanceados("((()))()"))
print(parentesis_balanceados(")(()"))
print(parentesis_balanceados("(()"))
