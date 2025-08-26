from settings import BOARD_LENGTH, VICTORY_STRIKE


class LinearBoard:
    """Clase que representa el tablero de una sola columna
    x un jugador
    o otro jugador
    none un espacio vacio
    """

    def __init__(self):
        """una lista de None"""
        self._column = [None for i in range(BOARD_LENGTH)]

    def add(self, char):
        # siempre y cuando no este lleno
        if not self.is_full():
            # Juega en la primera posición disponible
            i = self._column.index(None)
            self._column[i] = char

    def is_full(self):
        # Si esta lleno, la última posición no esta vacía
        return self._column[-1] != None

    def is_victory(self, char):
        # la victoria se da cuando hay 3 'x' seguidas
        contador = 0
        for i in range(VICTORY_STRIKE):
            if self._column[i] == char:
                contador += 1
            else:
                break

        if contador == 3:
            return True
        else:
            return False
        # recorrer la lista
        # si hay una 'x', contador = + 1 y sigo
        # si hay una 'o' ó un 'None' paro y salgo
        # si contador =3 victoria

    def is_tie(self, char1, char2):
        """No hay victoria ni de char1 ni de char2"""
        return (not self.is_victory("x")) and (not self.is_victory("o"))
