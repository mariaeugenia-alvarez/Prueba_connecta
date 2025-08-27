from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import *


class LinearBoard:
    """Clase que representa el tablero de una sola columna
    x un jugador
    o otro jugador
    none un espacio vacio
    """

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._column = list
        return board

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
        return find_streak(self._column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        """No hay victoria ni de char1 ni de char2"""
        return (not self.is_victory(char1)) and (not self.is_victory(char2))
