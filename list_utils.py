def find_one(list, needle):
    """Devuelve True si encuentra una o más ocurrencias de needle en list"""

    return find_n(list, needle, 1)


def find_n(list, needle, n):
    """Devuelve True si en list hay n o más ocurrencias de needle, False si hay un menos o si n <0"""
    # si n>=0 ...
    if n >= 0:
        # inicializamos el indice y el contador
        index = 0
        count = 0
        # mientras no se encuentre al elemento n veces o no estemos al final de la lista
        while count < n and index < len(list):
            # si lo encuentra: actualizar contador
            if needle == list[index]:
                count += 1
            # avanzar al siguiente elementos
            index += 1
        # devolver el resultado de comparar contador con n
        return count >= n
    else:
        return False


def find_streak(list, needle, n):
    """Devuelve True si en list hay n o más needles seguidos y False para lo demás"""
    # si n>=0...
    if n >= 0:
        # inicializamos indice, contador e indicador de racha
        index = 0
        count = 0
        streak = False
        # mientras no se encuentre n veces seguidos y no se haya acabado
        while count < n and index < len(list):
            # si lo encuentro activo el indicador de racha y actualizo contador
            if needle == list[index]:
                streak = True
                count += 1
            # si no lo encuentro desactivo el indicador de racha y pongo a cero el contador
            else:
                streak = False
                count = 0
            # avanzo al siguiente elemento
            index += 1
        # devuelvo el resultado de comparar el contador con n siempre y cuando estemos en racha
        return count >= n and streak
    else:
        return False
