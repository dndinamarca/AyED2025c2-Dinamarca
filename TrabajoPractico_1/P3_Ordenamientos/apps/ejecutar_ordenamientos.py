import time
import random
import matplotlib.pyplot as plt
import pandas as pd
from modules.ordenamientos import burbuja, quicksort, radix_sort

TAMANIOS = [10, 50, 100, 200, 300, 500, 700, 1000]
REPETICIONES = 3  # para promediar tiempos
ARCHIVO_SALIDA = "data/tiempos_ordenamientos.csv"


def medir_tiempo(funcion, lista):
    """Mide el tiempo de ejecución de una función de ordenamiento."""
    inicio = time.perf_counter()
    funcion(lista)
    fin = time.perf_counter()
    return fin - inicio


def generar_lista(n):
    """Genera una lista de n números aleatorios de cinco dígitos."""
    return [random.randint(10000, 99999) for _ in range(n)]


resultados = []

for n in TAMANIOS:
    lista = generar_lista(n)
    print(f"\n🔹 Midiendo para lista de tamaño {n}...")

    tiempos = {"n": n}

    # Burbuja (solo para tamaños pequeños, porque es muy lenta)
    if n <= 300:
        tiempos["burbuja"] = sum(medir_tiempo(burbuja, lista) for _ in range(REPETICIONES)) / REPETICIONES
    else:
        tiempos["burbuja"] = None

    # Quicksort
    tiempos["quicksort"] = sum(medir_tiempo(quicksort, lista) for _ in range(REPETICIONES)) / REPETICIONES

    # Radix sort
    tiempos["radix_sort"] = sum(medir_tiempo(radix_sort, lista) for _ in range(REPETICIONES)) / REPETICIONES

    # sorted() de Python
    tiempos["sorted"] = sum(medir_tiempo(sorted, lista) for _ in range(REPETICIONES)) / REPETICIONES

    resultados.append(tiempos)


df = pd.DataFrame(resultados)
df.to_csv(ARCHIVO_SALIDA, index=False)
print(f"\n✅ Resultados guardados en {ARCHIVO_SALIDA}")

plt.figure(figsize=(8, 5))
if df["burbuja"].notnull().any():
    plt.plot(df["n"], df["burbuja"], label="Burbuja", marker="o")
plt.plot(df["n"], df["quicksort"], label="Quicksort", marker="o")
plt.plot(df["n"], df["radix_sort"], label="Radix Sort", marker="o")
plt.plot(df["n"], df["sorted"], label="sorted() (Python)", marker="o")

plt.title("Comparación de tiempos de ordenamiento")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()