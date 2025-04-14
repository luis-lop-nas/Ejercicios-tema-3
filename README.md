# Ejercicios-tema-3

https://github.com/luis-lop-nas/Ejercicios-tema-3.git

# Ejercicios-tema-3

Este repositorio contiene una serie de ejercicios prácticos diseñados para explorar conceptos de programación mediante la implementación de soluciones a problemas específicos. Cada ejercicio está contenido en su propio directorio y aborda un tema diferente. A continuación, se describe cada ejercicio en detalle.

---

## Ejercicio 1: **Torres de Hanoi**

### Descripción
Este ejercicio implementa el clásico problema de las Torres de Hanoi, un rompecabezas matemático que consiste en mover un conjunto de discos de una torre a otra siguiendo ciertas reglas:
1. Solo se puede mover un disco a la vez.
2. Un disco más grande no puede colocarse sobre uno más pequeño.
3. Se deben utilizar tres torres: origen, auxiliar y destino.

### Funcionamiento
El programa incluye una simulación visual del problema utilizando `pygame`. Los discos se representan como bloques de colores, y el usuario puede observar cómo se resuelve el problema automáticamente.

### Archivos principales
- **`hanoi.py`**: Contiene la lógica principal del juego, incluyendo la resolución recursiva del problema.
- **`pila.py`**: Implementa una estructura de datos tipo pila para manejar los discos.
- **`utils.py`**: Proporciona funciones auxiliares, como mostrar el estado de las pilas en consola.
- **`visual/juego_pygame.py`**: Implementa la visualización gráfica del juego.
- **`record_hanoi.txt`**: Archivo que guarda los récords de movimientos mínimos para diferentes números de discos.

### Ejecución
Para ejecutar este ejercicio, simplemente corre el archivo `main.py` en el directorio `Ejercicio_1`. Esto abrirá la simulación visual.

---

## Ejercicio 2: **Determinante de una Matriz**

### Descripción
Este ejercicio calcula el determinante de una matriz cuadrada utilizando dos métodos:
1. **Recursivo**: Divide la matriz en submatrices menores para calcular el determinante.
2. **Iterativo**: Utiliza eliminación gaussiana para calcular el determinante de manera más eficiente.

### Funcionamiento
El programa permite al usuario introducir manualmente los elementos de la matriz o generarlos aleatoriamente. Luego, muestra el determinante calculado por ambos métodos.

### Archivos principales
- **`matriz.py`**: Define la clase `Matriz`, que incluye métodos para manipular matrices (obtener elementos, submatrices, etc.).
- **`determinante.py`**: Contiene las funciones para calcular el determinante de forma recursiva e iterativa.
- **`utils.py`**: Incluye funciones auxiliares, como verificar si una matriz es cuadrada.

### Ejecución
Para ejecutar este ejercicio, corre el archivo `main.py` en el directorio `Ejercicio_2`. Sigue las instrucciones en consola para introducir o generar la matriz.

---

## Ejercicio 3: **Gestión de Naves Espaciales**

### Descripción
Este ejercicio simula un sistema de gestión de naves espaciales. Permite realizar operaciones como:
- Ordenar naves por nombre o longitud.
- Buscar naves por nombre.
- Encontrar la nave más grande, más pequeña o con más tripulantes.
- Modificar, añadir o eliminar naves de la lista.

### Funcionamiento
El programa comienza con una lista predefinida de naves y permite al usuario interactuar con ella mediante un menú en consola.

### Archivos principales
- **`nave.py`**: Define la clase `Nave`, que almacena información como nombre, longitud, tripulantes y pasajeros.
- **`gestor_naves.py`**: Contiene métodos estáticos para realizar operaciones sobre una lista de naves.
- **`lanzador.py`**: Implementa la lógica principal del programa, incluyendo el menú interactivo.

### Ejecución
Para ejecutar este ejercicio, corre el archivo `main.py` en el directorio `Ejercicio_3`. Sigue las instrucciones en consola para interactuar con el sistema.

---

## Ejercicio 4: **Operaciones con Polinomios**

### Descripción
Este ejercicio implementa un sistema para realizar operaciones algebraicas con polinomios, como:
- Suma y resta de polinomios.
- División de polinomios (obteniendo cociente y resto).
- Verificar la existencia de términos específicos.
- Eliminar términos de un polinomio.

### Funcionamiento
El programa permite al usuario trabajar con polinomios predefinidos, introducirlos manualmente o generarlos aleatoriamente. Luego, realiza las operaciones y muestra los resultados.

### Archivos principales
- **`polinomio.py`**: Define la clase `Polinomio`, que permite agregar, eliminar y mostrar términos.
- **`operaciones.py`**: Contiene funciones para realizar operaciones algebraicas con polinomios.
- **`lanzador.py`**: Implementa la lógica principal del programa, incluyendo un menú interactivo.

### Ejecución
Para ejecutar este ejercicio, corre el archivo `main.py` en el directorio `Ejercicio_4`. Sigue las instrucciones en consola para realizar las operaciones.

---

## Requisitos

- Python 3.10 o superior.
- Biblioteca `pygame` (solo para el Ejercicio 1).

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/luis-lop-nas/Ejercicios-tema-3.git