from algoritmos import obtener_solucion_optima
from visualizacion import visualizar_camino
from entrada_datos import ingresar_pesos_manual, ingresar_pesos_rapido, mostrar_menu


def ejecutar_programa():
    while True:
        opcion = mostrar_menu()
        
        if opcion == 3:
            print("\nGracias por usar el programa")
            break
        
        # Obtener pesos segun la opcion elegida
        if opcion == 1:
            pesos = ingresar_pesos_rapido()
        elif opcion == 2:
            pesos = [1, 4, 5, 4]
            print(f"\nUsando ejemplo predefinido: {pesos}")
        
        # Mostrar grafo de entrada
        print("\n--- GRAFO DE ENTRADA ---")
        print(f"Pesos de los nodos: {pesos}")
        visualizar_camino(pesos)
        
        # Calcular solucion optima
        nodos_seleccionados, peso_total = obtener_solucion_optima(pesos)
        
        # Mostrar resultados
        print("\n--- SOLUCION OPTIMA ---")
        print(f"Nodos seleccionados: {nodos_seleccionados}")
        print(f"Peso total maximo: {peso_total}")
        
        # Mostrar visualizacion de la solucion
        visualizar_camino(pesos, nodos_seleccionados)
        
        # Preguntar si desea continuar
        continuar = input("\nDesea resolver otro problema? (s/n): ")
        if continuar.lower() != 's':
            print("\nGracias por usar el programa")
            break


if __name__ == "__main__":
    ejecutar_programa()
