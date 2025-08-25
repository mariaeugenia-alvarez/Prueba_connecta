from settings import BOARD_LENGTH


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
        return False

    def is_tie(self, char1, char2):
        return False
