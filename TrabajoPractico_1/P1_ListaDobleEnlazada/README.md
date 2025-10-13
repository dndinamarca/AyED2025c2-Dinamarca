# Lista Doblemente Enlazada

Este proyecto implementa una Lista Doblemente Enlazada (LDE) desde cero, con el objetivo de desarrollar las operaciones básicas del TAD de manera eficiente y sin utilizar estructuras de Python que dupliquen los datos.
Se incluyen métodos fundamentales como agregar al inicio y al final, insertar en posición, extraer, copiar, invertir, concatenar y la sobrecarga de operadores como + y len().

---
## 🏗Arquitectura General

La estructura se basa en las clases Nodo y ListaDobleEnlazada:
Cada Nodo contiene un valor y punteros a los nodos siguiente y anterior.
La ListaDobleEnlazada mantiene referencias a la cabeza, la cola y un atributo tamanio, que permite acceder al tamaño en tiempo constante.
Todas las operaciones manipulan los punteros directamente, garantizando un uso óptimo de memoria y evitando la creación de listas intermedias.
Además, para corroborar el correcto funcionamiento de la implementación, se incluye el test provisto por la cátedra, junto con el análisis y las gráficas de rendimiento correspondientes a los métodos len(), copiar() e invertir().

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. time (biblioteca estándar de Python)


---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Dinamarca Daiana Nicole

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
