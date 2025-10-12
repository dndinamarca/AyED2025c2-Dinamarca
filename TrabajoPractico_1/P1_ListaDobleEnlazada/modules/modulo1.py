from modulos import ListaDobleEnlazada

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def agregar_al_inicio(self, carta):
        self.cartas.agregar_al_inicio(carta)

    def agregar_al_final(self, carta):
        self.cartas.agregar_al_final(carta)

    def insertar(self, carta, posicion):
        self.cartas.insertar(carta, posicion)

    def extraer(self, posicion=None):
        return self.cartas.extraer(posicion)

    def copiar(self):
        copia = Mazo()
        copia.cartas = self.cartas.copiar()
        return copia

    def invertir(self):
        self.cartas.invertir()

    def concatenar(self, otro_mazo):
        self.cartas.concatenar(otro_mazo.cartas)

    def __add__(self, otro_mazo):
        nuevo = Mazo()
        nuevo.cartas = self.cartas + otro_mazo.cartas
        return nuevo

    def __len__(self):
        return len(self.cartas)

    def __iter__(self):
        return iter(self.cartas)

    def __repr__(self):
        return repr(self.cartas)
