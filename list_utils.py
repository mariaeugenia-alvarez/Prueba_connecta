def find_one(list, needle):
    """Devuelve True si encuentra una o más ocurrencias de needle en list"""

    # inicializamos el bool que representa la condición de haber encontrado o no y el indice
    found = False
    index = 0
    # mientras no se encuentre o no estemos al final de la lista
    while not found and index < len(list):
        # mira si esta en la posicion actual y actualiza condición
        if needle == list[index]:
            found = True
        # avanza al siguiente elemento
        index += 1
    # devolver si se ha encontrado o no
    return found
