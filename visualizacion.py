import matplotlib.pyplot as plt
import networkx as nx
from typing import List


def visualizar_camino(pesos: List[int], nodos_seleccionados: List[int] = None) -> None:
    """
    Crea una visualizacion grafica del camino y la solucion optima.
    Muestra los nodos con sus pesos y resalta los nodos seleccionados.
    """
    n = len(pesos)
    if n == 0:
        print("No hay nodos para visualizar")
        return
    
    # Crear grafo de camino
    G = nx.path_graph(n)
    
    # Posiciones de los nodos en linea horizontal
    pos = {i: (i, 0) for i in range(n)}
    
    # Colores de los nodos
    colores_nodos = []
    for i in range(n):
        if nodos_seleccionados and (i + 1) in nodos_seleccionados:
            colores_nodos.append('lightgreen')
        else:
            colores_nodos.append('lightblue')
    
    # Etiquetas de los nodos con sus pesos
    etiquetas = {i: f"Nodo {i+1}\nPeso: {pesos[i]}" for i in range(n)}
    
    # Crear figura
    plt.figure(figsize=(max(12, n * 2), 4))
    
    # Dibujar grafo
    nx.draw(G, pos, 
            node_color=colores_nodos, 
            node_size=2000, 
            with_labels=False,
            edge_color='gray',
            width=2)
    
    # Dibujar etiquetas
    nx.draw_networkx_labels(G, pos, etiquetas, font_size=10)
    
    # Titulo
    if nodos_seleccionados:
        plt.title(f"Conjunto Independiente Maximo\nNodos seleccionados: {nodos_seleccionados}", 
                 fontsize=14, fontweight='bold')
    else:
        plt.title("Grafo de Entrada - Camino", fontsize=14, fontweight='bold')
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()
