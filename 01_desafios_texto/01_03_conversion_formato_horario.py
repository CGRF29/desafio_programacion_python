def convertir_horario(hora):
    """Regresa el formato de 12 hrs convertido a formato de 24 hrs.
    Argumentos:
    hora -- debe ser string, debe contener am/pm al final.
    hora_convertida -- formato 24 hrs"""
    hora_lista = hora.split(":")
    if hora[-2:].lower() == "pm":
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0]) + 12)
    elif hora[-2:].lower() == "am":
        if hora_lista[0] == "12":
            hora_lista[0] = "00"
    else:
        return ('Verificar el formato.')

    hora_convertida = ":".join(hora_lista)
    # print(hora_convertida)
    return hora_convertida[:-2]

print(convertir_horario("12:40AM")) # 00:40
print(convertir_horario("04:59pm")) # 16:59
print(convertir_horario("10:00")) # 22:00
