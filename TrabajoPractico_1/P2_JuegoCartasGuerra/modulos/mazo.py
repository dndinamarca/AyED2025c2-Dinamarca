# mazo.py

from modulos.ListaDobleEnlazada import ListaDobleEnlazada
from modulos.carta import Carta

class DequeEmptyError(Exception):
    """Excepción personalizada cuando el mazo está vacío."""
    pass

class Mazo:
    def __init__(self):
        # El mazo se implementa con una lista doblemente enlazada
        self.cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        """Coloca una carta en la parte superior del mazo."""
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Coloca una carta en la parte inferior del mazo."""
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self):
        """Saca y devuelve la carta de la parte superior del mazo."""
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        return self.cartas.extraer(0)
    def __len__(self):
        return len(self.cartas)