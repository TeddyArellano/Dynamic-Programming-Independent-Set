# Conjunto Independiente Máximo en un Grafo de Camino

**Implementación del Algoritmo de Programación Dinámica para el Problema del Conjunto Independiente de Peso Máximo**

---

## Descripción del Problema

Un **conjunto independiente** en un grafo es un subconjunto de vértices donde ningún par de vértices es adyacente (no están conectados por una arista). Este proyecto implementa una solución eficiente para encontrar el conjunto independiente de **peso máximo** en un grafo tipo camino.

### Definición Formal

Dado un camino con _n_ nodos, donde cada nodo _i_ tiene un peso _W[i]_, el objetivo es encontrar un subconjunto de nodos tal que:

1. Ningún par de nodos en el subconjunto sea adyacente
2. La suma de los pesos de los nodos seleccionados sea máxima

### Ejemplo Ilustrativo

Para el camino con pesos `[1, 4, 5, 4]`:
```
Nodo:  1 --- 2 --- 3 --- 4
Peso:  1     4     5     4
```
La solución óptima selecciona los nodos `[2, 4]` con un peso total de `8` (4 + 4).


---

## Requisitos del Sistema

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Dependencias

Las bibliotecas necesarias para ejecutar el proyecto son:
- `matplotlib >= 3.5.0` - Para visualización gráfica
- `networkx >= 2.6.0` - Para manipulación de grafos

### Instalación

Para instalar las dependencias, ejecute uno de los siguientes comandos:

```bash
pip install matplotlib networkx
```

O bien, utilizando el archivo de requisitos:

```bash
pip install -r requirements.txt
```

### Ejecución del Programa

Para ejecutar el programa principal:

```bash
python independent_set.py
```

---

## Estructura del Proyecto

```
Trabajo Remedial - Independent Set/
│
├── algoritmos.py          # Implementación del algoritmo de programación dinámica
├── entrada_datos.py       # Módulo de gestión de entrada y menú interactivo
├── independent_set.py     # Archivo principal de ejecución
├── visualizacion.py       # Módulo de visualización gráfica
├── requirements.txt       # Archivo de dependencias del proyecto
└── README.md             # Documentación del proyecto
```

---

## Uso del Programa

Al ejecutar el programa, se presenta un menú interactivo con las siguientes opciones:

```
============================================================
  CONJUNTO INDEPENDIENTE MAXIMO EN UN CAMINO
============================================================
1. Ingresar pesos de nodos (todos en una linea)
2. Usar ejemplo predefinido
3. Salir
============================================================
```

**Ejemplo de sesión:**

```
Seleccione una opcion: 1
Ingrese los pesos de los nodos separados por espacios: 1 4 5 4

--- GRAFO DE ENTRADA ---
Pesos de los nodos: [1, 4, 5, 4]

--- SOLUCION OPTIMA ---
Nodos seleccionados: [2, 4]
Peso total maximo: 8
```

El programa genera visualizaciones gráficas que muestran:
- El grafo de entrada con todos los nodos
- La solución óptima con los nodos seleccionados resaltados en verde


---

## Fundamento Teórico: Programación Dinámica

### Subestructura Óptima

El problema exhibe una subestructura óptima que permite aplicar programación dinámica. Para un camino con _n_ nodos, la solución óptima en el nodo _i_ depende de dos casos mutuamente excluyentes:

1. **Incluir el nodo _i_**: Si se incluye el nodo _i_, no se puede incluir el nodo _i-1_ (son adyacentes). Por lo tanto, el peso total es _W[i]_ más la solución óptima de los primeros _i-2_ nodos.

2. **Excluir el nodo _i_**: Si no se incluye el nodo _i_, la solución es idéntica a la solución óptima de los primeros _i-1_ nodos.

### Relación de Recurrencia

La fórmula de recurrencia que caracteriza el problema es:

```
M[i] = max(W[i] + M[i-2], M[i-1])
```

**Donde:**
- `M[i]` = Peso máximo del conjunto independiente usando los primeros _i_ nodos
- `W[i]` = Peso del nodo _i_
- `M[i-2]` = Solución óptima sin considerar el nodo _i-1_ (adyacente)
- `M[i-1]` = Solución óptima excluyendo el nodo _i_

**Casos base:**
- `M[0] = 0` (grafo vacío)
- `M[1] = W[1]` (un solo nodo)

### Análisis de Complejidad

- **Complejidad Temporal:** O(n) - Se procesa cada nodo exactamente una vez
- **Complejidad Espacial:** O(n) - Se requiere una tabla de memoización de tamaño _n+1_

### Ejemplo de Traza del Algoritmo

Para el camino con pesos `[1, 4, 5, 4]`:

```
M[0] = 0                          (caso base)
M[1] = 1                          (caso base)
M[2] = max(4+0, 1) = 4           (se incluye nodo 2)
M[3] = max(5+1, 4) = 6           (se incluye nodo 3)
M[4] = max(4+4, 6) = 8           (se incluye nodo 4) ← Peso total óptimo
```

Reconstrucción de la solución desde _M[4]_:
- En _i=4_: `W[4] + M[2] = 8 > M[3] = 6` → Se incluye nodo 4
- En _i=2_: `W[2] + M[0] = 4 > M[1] = 1` → Se incluye nodo 2
- Solución: `[2, 4]` con peso total `8`



---

## Arquitectura del Software

El proyecto está organizado en módulos independientes que implementan las diferentes funcionalidades del sistema.

### Módulo: `algoritmos.py`

Contiene la implementación del algoritmo de programación dinámica.

**Funciones principales:**

- **`peso_maximo_independiente(pesos: List[int])`**  
  Implementa el algoritmo de programación dinámica para calcular el peso máximo del conjunto independiente. Retorna la tabla de memoización _M_ y el peso total óptimo.

- **`reconstruir_solucion(M: List[int], pesos: List[int], i: int, nodos_seleccionados: List[int])`**  
  Reconstruye recursivamente los índices de los nodos que conforman la solución óptima utilizando la tabla de memoización.

- **`obtener_solucion_optima(pesos: List[int])`**  
  Función de alto nivel que orquesta el cálculo del peso máximo y la reconstrucción de la solución. Retorna los nodos seleccionados (ordenados) y el peso total.

### Módulo: `visualizacion.py`

Proporciona funcionalidades para la representación gráfica del problema y su solución.

**Funciones principales:**

- **`visualizar_camino(pesos: List[int], nodos_seleccionados: List[int] = None)`**  
  Genera una visualización gráfica del grafo de camino utilizando las bibliotecas matplotlib y networkx. Los nodos seleccionados se resaltan en verde, mientras que los no seleccionados se muestran en azul.

### Módulo: `entrada_datos.py`

Gestiona la interacción con el usuario y la captura de datos de entrada.

**Funciones principales:**

- **`ingresar_pesos_rapido()`**  
  Permite al usuario ingresar los pesos de todos los nodos en una sola línea, separados por espacios.

- **`mostrar_menu()`**  
  Presenta el menú principal y captura la selección del usuario.

### Módulo: `independent_set.py`

Archivo principal que integra todos los módulos y controla el flujo de ejecución del programa.

**Funciones principales:**

- **`ejecutar_programa()`**  
  Función principal que implementa el ciclo de ejecución: presentación del menú, captura de datos, cálculo de la solución óptima, visualización de resultados y opción de continuar.



---

## Casos de Prueba

La siguiente tabla presenta diversos casos de prueba que demuestran el comportamiento del algoritmo:

| Entrada | Nodos Seleccionados | Peso Total | Observación |
|---------|---------------------|------------|-------------|
| `[1, 4, 5, 4]` | `[2, 4]` | `8` | Selección de nodos alternos de peso 4 |
| `[5, 1, 5, 1, 5]` | `[1, 3, 5]` | `15` | Selección de todos los nodos con peso máximo |
| `[1, 1, 100, 1, 1]` | `[3]` | `100` | Nodo dominante excluye adyacentes |
| `[3, 2, 5, 10, 7, 2]` | `[1, 4, 6]` | `15` | Optimización sobre múltiples opciones |
| `[2, 4, 6, 8, 10]` | `[2, 4]` o `[1, 3, 5]` | `18` | Múltiples soluciones óptimas equivalentes |

---

## Propiedades del Algoritmo

**Ventajas:**
- **Optimalidad garantizada:** El algoritmo siempre encuentra la solución de peso máximo
- **Eficiencia lineal:** Complejidad temporal O(n), óptima para este problema
- **Claridad conceptual:** La implementación refleja directamente la formulación matemática
- **Visualización integrada:** Facilita la comprensión del problema y su solución

**Limitaciones:**
- Aplicable únicamente a grafos de tipo camino (estructura lineal)
- No extensible directamente a grafos con ciclos o estructuras arbóreas generales
- Requiere almacenamiento de la tabla de memoización completa en memoria

---

## Información del Proyecto

**Institución:** Instituto Politécnico Nacional  
**Curso:** Diseño y Análisis de Algoritmos  
**Alumno:** Arellano Juárez José Juan
**Tipo:** Trabajo Remedial  
**Año:** 2026
