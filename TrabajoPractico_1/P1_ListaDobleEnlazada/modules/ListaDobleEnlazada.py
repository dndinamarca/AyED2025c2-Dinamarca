class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if not self.cola:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            previo = actual.anterior
            previo.siguiente = nuevo
            nuevo.anterior = previo
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.cabeza is None:
            raise Exception("No se puede extraer de una lista vacía")

        # Si no se pasa posición, eliminar el último
        if posicion is None:
            posicion = self.tamanio - 1

        # Soporte para índices negativos
        if posicion < 0:
            posicion = self.tamanio + posicion  # ej: -1 → último

        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        self.tamanio -= 1
        return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        """Concatena otra lista al final de la actual, ajustando todos los punteros correctamente."""
        if otra_lista.cabeza is None:
            return  # nada que concatenar

        # Si la lista actual está vacía, la lista resultante será otra_lista
        if self.cabeza is None:
            # Crear nodos nuevos para no compartir referencias
            nodo_actual = otra_lista.cabeza
            while nodo_actual:
                self.agregar_al_final(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
            return

        # Lista no vacía: añadir cada elemento de otra_lista al final
        nodo_actual = otra_lista.cabeza
        while nodo_actual:
            self.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        # Asegurar que los extremos estén correctos
        if self.cabeza:
            self.cabeza.anterior = None
        if self.cola:
            self.cola.siguiente = None

    def __add__(self, otra_lista):
        """Retorna una nueva lista resultante de la concatenación sin modificar las originales."""
        nueva = self.copiar()  # copia profunda
        nueva.concatenar(otra_lista)

        # 🔧 asegurarse que la cabeza y cola estén correctas
        if nueva.cabeza:
            nueva.cabeza.anterior = None
        if nueva.cola:
            nueva.cola.siguiente = None
        return nueva

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

            
if __name__ == "__main__":
    print("=== Prueba de la Lista Doble Enlazada ===\n")

    lista = ListaDobleEnlazada()
    print("Agregando elementos al final: 10, 20, 30")
    lista.agregar_al_final(10)
    lista.agregar_al_final(20)
    lista.agregar_al_final(30)

    print("Contenido actual:", [x for x in lista])

    print("\nAgregando elemento al inicio: 5")
    lista.agregar_al_inicio(5)
    print("Contenido actual:", [x for x in lista])

    print("\nInsertando 15 en posición 2")
    lista.insertar(15, 2)
    print("Contenido actual:", [x for x in lista])

    print("\nExtrayendo posición 1:", lista.extraer(1))
    print("Contenido actual:", [x for x in lista])

    print("\nInvirtiendo lista...")
    lista.invertir()
    print("Contenido actual:", [x for x in lista])

    print("\nCopiando lista...")
    copia = lista.copiar()
    print("Copia:", [x for x in copia])

    print("\nConcatenando con otra lista [100, 200]")
    otra = ListaDobleEnlazada()
    otra.agregar_al_final(100)
    otra.agregar_al_final(200)
    lista.concatenar(otra)
    print("Lista concatenada:", [x for x in lista])

    print("\nProbando operador + con [300, 400]")
    otra2 = ListaDobleEnlazada()
    otra2.agregar_al_final(300)
    otra2.agregar_al_final(400)
    nueva = lista + otra2
    print("Lista original:", [x for x in lista])
    print("Nueva lista:", [x for x in nueva])
