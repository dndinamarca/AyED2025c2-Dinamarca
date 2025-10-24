
import random

def burbuja(lista):
    """
    Ordena una lista utilizando el método de burbuja.
    Complejidad: O(n²)
    """
    lista = lista.copy()  # para no modificar la original
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def quicksort(lista):
    """
    Ordena una lista utilizando el algoritmo quicksort.
    Complejidad promedio: O(n log n)
    Peor caso: O(n²)
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

def radix_sort(lista):
    """
    Ordena una lista de números enteros utilizando radix sort (base 10).
    Complejidad: O(d * (n + k)) donde
    d = número de dígitos y k = base.
    """
    lista = lista.copy()
    if not lista:
        return []

    max_num = max(lista)
    exp = 1  # 1, 10, 100, ...
    while max_num // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10
    return lista

def counting_sort_por_digito(lista, exp):
    """Función auxiliar para radix_sort."""
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10  # base 10

    # Contar ocurrencias según el dígito actual
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # Acumular las posiciones
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la salida (de derecha a izquierda para estabilidad)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    # Copiar a la lista original
    for i in range(n):
        lista[i] = salida[i]

if __name__ == "__main__":
    datos = [random.randint(10000, 99999) for _ in range(10)]
    print("Lista original:", datos)
    print("Burbuja:", burbuja(datos))
    print("Quicksort:", quicksort(datos))
    print("Radix sort:", radix_sort(datos))
