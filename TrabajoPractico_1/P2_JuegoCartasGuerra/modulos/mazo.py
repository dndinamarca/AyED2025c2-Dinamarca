# mazo.py


from modulos.ListaDobleEnlazada import ListaDobleEnlazada

class DequeEmptyError(Exception):
    "Excepción personalizada para cuando el mazo está vacío."
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()  # Contenedor principal de cartas

    def poner_carta_arriba(self, carta):
        "Agrega una carta al inicio del mazo (para repartir o voltear)."
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        "Agrega una carta al final del mazo (para ganar el turno)."
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self):
        "Saca y devuelve la carta del inicio del mazo. Lanza excepción si está vacío."
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.extraer(0)  # Extrae la primera carta
        return carta

    def __len__(self):
        "Devuelve la cantidad de cartas en el mazo."
        return len(self.cartas)
