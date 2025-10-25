import time
import matplotlib.pyplot as plt
from modules.ListaDobleEnlazada import ListaDobleEnlazada

# Configuración
tamanios = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
repeticiones = 5

# Listas para guardar tiempos promedio
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for N in tamanios:
    # Crear lista con N elementos
    lista = ListaDobleEnlazada()
    for i in range(N):
        lista.agregar_al_final(i)
    
    # ----- len() -----
    t_start = time.time()
    for _ in range(repeticiones):
        _ = len(lista)
    t_end = time.time()
    tiempos_len.append((t_end - t_start) / repeticiones)
    
    # ----- copiar() -----
    t_start = time.time()
    for _ in range(repeticiones):
        copia = lista.copiar()
    t_end = time.time()
    tiempos_copiar.append((t_end - t_start) / repeticiones)
    
    # ----- invertir() -----
    t_start = time.time()
    for _ in range(repeticiones):
        lista.invertir()
    t_end = time.time()
    tiempos_invertir.append((t_end - t_start) / repeticiones)

# ----- Graficar -----
plt.figure(figsize=(10,6))
plt.plot(tamanios, tiempos_len, marker='o', label='len()')
plt.plot(tamanios, tiempos_copiar, marker='o', label='copiar()')
plt.plot(tamanios, tiempos_invertir, marker='o', label='invertir()')
plt.xlabel('N (cantidad de elementos)')
plt.ylabel('Tiempo promedio (s)')
plt.title('Tiempo de ejecución vs tamaño de lista')
plt.legend()
plt.grid(True)
plt.show()
