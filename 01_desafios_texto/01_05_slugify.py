import re


def slugify(texto):
    """
    Regresa el texto unicamente con caracteres alfanumericos,
    separando las palabras con guion(-).
    Argumentos:
    texto -- Debe ser un string
    slug  -- return cadena modificada
    """
    slug = (texto
        .lower()
        .strip()
        .replace(" ", "-")
    )

    slug = re.sub("[^\w\-]", "", slug)
    return slug


print(slugify("texto% con caracteres$# especial-es")) # texto-con-caracteres-especial-es
print(slugify("Este es un ejemplo!!!")) # este-es-un-ejemplo
