# Conjunto Independiente Maximo en un Camino

## Descripcion del Problema

Un **conjunto independiente** en un grafo es un subconjunto de vertices donde ningun par de vertices es adyacente (no estan conectados por una arista). El problema consiste en encontrar el conjunto independiente de **peso maximo** en un grafo tipo camino.

### Definicion Formal

Dado un camino con `n` nodos, donde cada nodo `i` tiene un peso `W[i]`, queremos encontrar un subconjunto de nodos tal que:
1. Ningun par de nodos en el subconjunto sea adyacente
2. La suma de los pesos de los nodos seleccionados sea maxima

### Ejemplo

Supongamos un camino con 4 nodos con pesos: `[1, 4, 5, 4]`

```
Nodo:  1 --- 2 --- 3 --- 4
Peso:  1     4     5     4
```

La solucion optima es seleccionar los nodos **2** y **4** (no son adyacentes), con un peso total de **4 + 4 = 8**.

Si seleccionaramos los nodos 1, 3 tendriamos: 1 + 5 = 6 (menor)
Si seleccionaramos solo el nodo 3 tendriamos: 5 (menor)

---

## Fundamentos Teoricos

### Programacion Dinamica

El problema se resuelve usando **programacion dinamica**, una tecnica que divide el problema en subproblemas mas pequenos y reutiliza sus soluciones.

#### Subestructura Optima

Para un camino con `n` nodos, la solucion optima depende de dos casos:

1. **Incluir el nodo n**: Si incluimos el nodo `n`, no podemos incluir el nodo `n-1` (son adyacentes). Por lo tanto, debemos sumar el peso de `n` mas la solucion optima para los primeros `n-2` nodos.
   - Peso = `W[n] + M[n-2]`

2. **No incluir el nodo n**: Si no incluimos el nodo `n`, la solucion es la misma que para los primeros `n-1` nodos.
   - Peso = `M[n-1]`

La solucion optima es el **maximo** de estos dos casos:
```
M[n] = max(W[n] + M[n-2], M[n-1])
```

#### Casos Base

- `M[0] = 0`: Un grafo vacio tiene peso 0
- `M[1] = W[1]`: Un grafo con un solo nodo tiene como peso el peso de ese nodo

### Complejidad

- **Tiempo**: O(n) - Se calcula cada subproblema una sola vez
- **Espacio**: O(n) - Se almacena la tabla de memorizacion

---

## Estructura del Proyecto

```
Trabajo Remedial - Independent Set/
│
├── algoritmos.py          # Algoritmo de programacion dinamica (peso_maximo_independiente, reconstruir_solucion)
├── entrada_datos.py       # Gestion de entrada de datos y menu principal
├── independent_set.py     # Archivo principal para ejecutar el programa
├── visualizacion.py       # Visualizacion grafica del camino y la solucion
└── README.md             # Documentacion del proyecto
```

### Descripcion de Modulos

- **`algoritmos.py`**: Contiene las funciones principales del algoritmo de programacion dinamica
- **`visualizacion.py`**: Maneja la representacion grafica del camino y la solucion
- **`entrada_datos.py`**: Gestiona la entrada de datos del usuario y el menu
- **`independent_set.py`**: Archivo principal que orquesta la ejecucion del programa

### Modulo: algoritmos.py

Este modulo contiene las funciones principales del algoritmo de programacion dinamica.

#### 1. `peso_maximo_independiente(pesos: List[int])`

**Archivo**: algoritmos.py

**Que hace**: Implementa el algoritmo de programacion dinamica para calcular el peso maximo del conjunto independiente optimo.

**Como funciona**:
- Crea un arreglo `M` de tamano `n+1` para memorizacion
- Inicializa los casos base: `M[0] = 0` y `M[1] = W[1]`
- Recorre de `i=2` hasta `n` y para cada posicion calcula:
  - Opcion 1: Incluir nodo i → `W[i] + M[i-2]`
  - Opcion 2: Excluir nodo i → `M[i-1]`
  - Guarda el maximo: `M[i] = max(opcion1, opcion2)`
- Retorna la tabla completa `M` y el peso maximo `M[n]`

**Ejemplo**:
```python
pesos = [1, 4, 5, 4]
M, peso_total = peso_maximo_independiente(pesos)
# M = [0, 1, 4, 6, 8]
# peso_total = 8
```

#### 2. `reconstruir_solucion(M: List[int], pesos: List[int], i: int, nodos_seleccionados: List[int])`

**Archivo**: algoritmos.py

**Que hace**: Reconstruye recursivamente los nodos que pertenecen a la solucion optima usando la tabla de memorizacion.

**Como funciona**:
- **Caso base 1** (i=0): No hay mas nodos, termina la recursion
- **Caso base 2** (i=1): Selecciona el nodo 1 y termina
- **Caso recursivo**: Verifica si el nodo `i` fue incluido en la solucion optima:
  - Si `W[i] + M[i-2] > M[i-1]`: El nodo `i` fue incluido → lo agrega a la lista y continua con `i-2`
  - Si no: El nodo `i` no fue incluido → continua con `i-1`

**Ejemplo**:
```python
pesos = [1, 4, 5, 4]
M = [0, 1, 4, 6, 8]
nodos_seleccionados = []
reconstruir_solucion(M, pesos, 4, nodos_seleccionados)
# nodos_seleccionados = [4, 2] (se agregan en orden inverso)
```

#### 3. `obtener_solucion_optima(pesos: List[int])`

**Archivo**: algoritmos.py

**Que hace**: Funcion de alto nivel que combina las dos funciones anteriores para obtener la solucion completa.

**Como funciona**:
1. Llama a `peso_maximo_independiente()` para obtener la tabla `M` y el peso total
2. Llama a `reconstruir_solucion()` para obtener los nodos seleccionados
3. Ordena los nodos en orden ascendente
4. Retorna los nodos seleccionados y el peso total

**Ejemplo**:
```python
pesos = [1, 4, 5, 4]
nodos, peso_total = obtener_solucion_optima(pesos)
# nodos = [2, 4]
# peso_total = 8
```

### Modulo: visualizacion.py

Este modulo maneja toda la representacion grafica del problema.

#### 4. `visualizar_camino(pesos: List[int], nodos_seleccionados: List[int])`

**Archivo**: visualizacion.py

**Que hace**: Crea una representacion grafica del camino usando matplotlib y networkx.

**Como funciona**:
- Crea un grafo de tipo camino con `n` nodos
- Posiciona los nodos en una linea horizontal
- Colorea los nodos:
  - Verde claro: Nodos seleccionados en la solucion
  - Azul claro: Nodos no seleccionados
- Muestra las etiquetas con el numero de nodo y su peso
- Dibuja las aristas que conectan nodos adyacentes

**Ejemplo de uso**:
```python
pesos = [1, 4, 5, 4]
nodos_seleccionados = [2, 4]
visualizar_camino(pesos, nodos_seleccionados)
# Muestra el grafo con los nodos 2 y 4 en verde
```### Modulo: entrada_datos.py

Este modulo gestiona la interaccion con el usuario.

#### 5. `ingresar_pesos_rapido()`

**Archivo**: entrada_datos.py

**Que hace**: Permite al usuario ingresar los pesos de los nodos en una sola linea separados por espacios.

**Ejemplo de uso**:
```
Ingrese los pesos de los nodos separados por espacios: 1 4 5 4
```

## Ejecucion del Programa

### Requisitos

- Python 3.x
- Bibliotecas: `matplotlib`, `networkx`

### Instalacion de Dependencias

```bash
pip install matplotlib networkx
```

### Ejecutar el Programa

```bash
python independent_set.py
```

### Ejemplo de Ejecucion

```
============================================================
  CONJUNTO INDEPENDIENTE MAXIMO EN UN CAMINO
============================================================
1. Ingresar pesos de nodos (todos en una linea)
2. Usar ejemplo predefinido
3. Salir
============================================================
Seleccione una opcion: 1

Ingrese los pesos de los nodos separados por espacios: 1 4 5 4

--- GRAFO DE ENTRADA ---
Pesos de los nodos: [1, 4, 5, 4]
[Se muestra el grafico del camino]

--- SOLUCION OPTIMA ---
Nodos seleccionados: [2, 4]
Peso total maximo: 8
[Se muestra el grafico con la solucion]

Desea resolver otro problema? (s/n): n

Gracias por usar el programa
```

---

## Casos de Uso

### Caso 1: Problema Pequeno

```
Entrada: [1, 4, 5, 4]
Solucion: Nodos [2, 4], Peso total = 8
Explicacion: Seleccionar nodos 2 y 4 da 4+4=8, que es mejor que cualquier otra combinacion
```

### Caso 2: Pesos Alternados

```
Entrada: [5, 1, 5, 1, 5]
Solucion: Nodos [1, 3, 5], Peso total = 15
Explicacion: Se seleccionan todos los nodos con peso 5, saltando los de peso 1
```

### Caso 3: Un Peso Dominante

```
Entrada: [1, 1, 100, 1, 1]
Solucion: Nodos [1, 3, 5], Peso total = 102
Explicacion: Se incluye el nodo con peso 100 mas los nodos extremos
```

---

## Notas Tecnicas

### Por que funciona la Programacion Dinamica?

La clave es que cada decision (incluir o no un nodo) solo afecta a los nodos anteriores, no a los futuros. Esto permite construir la solucion optima global a partir de soluciones optimas locales.

### Ventajas del Enfoque

1. **Eficiencia**: Resuelve el problema en tiempo lineal O(n)
2. **Claridad**: El codigo sigue directamente el pseudocodigo matematico
3. **Correcto**: Garantiza encontrar la solucion optima

### Limitaciones

- Solo funciona para grafos tipo camino (no ciclos, no arboles generales)
- Requiere almacenar toda la tabla de memorizacion

---

## Autor

Proyecto academico para el curso de Diseno y Analisis de Algoritmos
