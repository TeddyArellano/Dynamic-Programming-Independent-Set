# Conjunto Independiente Máximo en un Camino

Solución eficiente del problema del conjunto independiente de peso máximo en grafos tipo camino usando programación dinámica.

## 📋 Descripción

Un **conjunto independiente** es un subconjunto de vértices donde ningún par está conectado por una arista. Este programa encuentra el conjunto independiente de **peso máximo** en un grafo tipo camino.

**Ejemplo:** Para el camino `[1, 4, 5, 4]`
```
Nodo:  1 --- 2 --- 3 --- 4
Peso:  1     4     5     4
```
**Solución óptima:** Nodos `[2, 4]` con peso total `8` (4 + 4)


## 🚀 Instalación y Ejecución

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install matplotlib networkx
```

O usa el archivo de requirements:
```bash
pip install -r requirements.txt
```

### Ejecutar el Programa

```bash
python independent_set.py
```

## 📂 Estructura del Proyecto

```
Trabajo Remedial - Independent Set/
│
├── algoritmos.py          # Algoritmo de programación dinámica
├── entrada_datos.py       # Gestión de entrada y menú
├── independent_set.py     # Archivo principal
├── visualizacion.py       # Visualización gráfica
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Documentación
```

## 🎯 Uso del Programa

Al ejecutar el programa, verás un menú con 3 opciones:

```
============================================================
  CONJUNTO INDEPENDIENTE MAXIMO EN UN CAMINO
============================================================
1. Ingresar pesos de nodos (todos en una linea)
2. Usar ejemplo predefinido
3. Salir
============================================================
```

**Ejemplo de ejecución:**
```bash
Seleccione una opcion: 1
Ingrese los pesos de los nodos separados por espacios: 1 4 5 4

--- GRAFO DE ENTRADA ---
Pesos de los nodos: [1, 4, 5, 4]

--- SOLUCION OPTIMA ---
Nodos seleccionados: [2, 4]
Peso total maximo: 8
```
## 🧮 Algoritmo de Programación Dinámica

### Fórmula de Recurrencia

Para cada nodo `i`, decidimos incluirlo o excluirlo:
```
M[i] = max(W[i] + M[i-2], M[i-1])
```

**Donde:**
- `M[i]` = Peso máximo usando los primeros `i` nodos
- `W[i]` = Peso del nodo `i`
- `M[i-2]` = Solución sin considerar el nodo adyacente
- `M[i-1]` = Solución sin incluir el nodo actual

### Complejidad
- **Tiempo:** O(n) - Un solo recorrido del arreglo
- **Espacio:** O(n) - Tabla de memoización

### Ejemplo de Ejecución del Algoritmo

Para `[1, 4, 5, 4]`:
```
M[0] = 0
M[1] = 1
M[2] = max(4+0, 1) = 4
M[3] = max(5+1, 4) = 6
M[4] = max(4+4, 6) = 8  ← Peso total óptimo
```

## 📊 Módulos del Proyecto

### `algoritmos.py`
- `peso_maximo_independiente()` - Calcula el peso máximo usando programación dinámica
- `reconstruir_solucion()` - Recupera los nodos de la solución óptima
- `obtener_solucion_optima()` - Función principal que combina ambas

### `visualizacion.py`
- `visualizar_camino()` - Genera visualización gráfica del grafo con matplotlib/networkx
- Nodos seleccionados en verde, no seleccionados en azul

### `entrada_datos.py`
- `ingresar_pesos_rapido()` - Captura pesos en una línea
- `mostrar_menu()` - Muestra el menú principal

### `independent_set.py`
- `ejecutar_programa()` - Flujo principal: entrada → cálculo → visualización

## 📝 Ejemplos de Casos

| Entrada | Solución | Peso Total | Explicación |
|---------|----------|------------|-------------|
| `[1, 4, 5, 4]` | `[2, 4]` | `8` | Nodos alternos de peso 4 |
| `[5, 1, 5, 1, 5]` | `[1, 3, 5]` | `15` | Todos los nodos con peso 5 |
| `[1, 1, 100, 1, 1]` | `[3]` | `100` | El nodo dominante |
## 📌 Características

✅ **Solución Óptima Garantizada** - Encuentra el peso máximo siempre  
✅ **Eficiencia Lineal** - Complejidad O(n) en tiempo  
✅ **Visualización Interactiva** - Gráficos claros del problema y solución  
✅ **Fácil de Usar** - Interfaz simple por consola  

## 🔧 Limitaciones

- Solo funciona para grafos tipo **camino** (no ciclos ni árboles generales)
- Requiere almacenar tabla de memoización completa en memoria

## 👨‍💻 Autor

Proyecto académico para el curso de **Diseño y Análisis de Algoritmos**

---

*Instituto Politécnico Nacional - 2026*
