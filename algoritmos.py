from typing import List, Tuple

"""
Diseñe un algoritmo bottom-up que devuelva el peso del conjunto independiente óptimo.
"""
def peso_maximo_independiente(pesos: List[int]) -> Tuple[List[int], int]:
    n = len(pesos)
    
    # Caso borde: grafo vacio
    if n == 0:
        return [0], 0
    
    # Crear arreglo de memorizacion
    M = [0] * (n + 1)
    
    # Caso base: un solo nodo
    M[1] = pesos[0]
    
    # Llenar la tabla con programacion dinamica
    for i in range(2, n + 1):
        # Incluir o excluir el nodo i
        incluir_nodo = pesos[i - 1] + M[i - 2]
        excluir_nodo = M[i - 1]
        M[i] = max(incluir_nodo, excluir_nodo)
    
    return M, M[n]

"""
Utilice la información guardada en el arreglo de memorización para recuperar 
la identidad de los nodos que pertenecen a la solución óptima.
"""
def reconstruir_solucion(M: List[int], pesos: List[int], i: int, nodos_seleccionados: List[int]) -> None:
    # Caso base: no hay nodos que seleccionar
    if i == 0:
        return
    
    # Caso base: se elige el unico nodo
    if i == 1:
        nodos_seleccionados.append(1)
        return
    
    # Se incluye el nodo i
    if pesos[i - 1] + M[i - 2] > M[i - 1]:
        nodos_seleccionados.append(i)
        reconstruir_solucion(M, pesos, i - 2, nodos_seleccionados)
    # No se incluye el nodo i
    else:
        reconstruir_solucion(M, pesos, i - 1, nodos_seleccionados)

"""
Encuentra el conjunto independiente de peso maximo y retorna los nodos seleccionados.
Retorna una tupla con la lista de nodos seleccionados y el peso total.
"""
def obtener_solucion_optima(pesos: List[int]) -> Tuple[List[int], int]:
    if len(pesos) == 0:
        return [], 0
    
    # Calcular peso maximo
    M, peso_total = peso_maximo_independiente(pesos)
    
    # Reconstruir solucion
    nodos_seleccionados = []
    reconstruir_solucion(M, pesos, len(pesos), nodos_seleccionados)
    
    # Ordenar los nodos en orden ascendente
    nodos_seleccionados.sort()
    
    return nodos_seleccionados, peso_total
