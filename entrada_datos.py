from typing import List


def ingresar_pesos_manual() -> List[int]:
    while True:
        try:
            n = int(input("Ingrese el numero de nodos: "))
            if n <= 0:
                print("El numero de nodos debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Por favor ingrese un numero valido")
    
    pesos = []
    print(f"\nIngrese el peso de cada nodo:")
    for i in range(n):
        while True:
            try:
                peso = int(input(f"  Peso del nodo {i+1}: "))
                pesos.append(peso)
                break
            except ValueError:
                print("Por favor ingrese un numero valido")
    
    return pesos


def ingresar_pesos_rapido() -> List[int]:
    while True:
        try:
            entrada = input("Ingrese los pesos de los nodos separados por espacios: ")
            pesos = [int(x) for x in entrada.split()]
            if len(pesos) == 0:
                print("Debe ingresar al menos un nodo")
                continue
            return pesos
        except ValueError:
            print("Por favor ingrese numeros validos separados por espacios")


def mostrar_menu() -> int:
    """
    Muestra el menu principal y retorna la opcion seleccionada por el usuario.
    """
    print("\n" + "="*60)
    print("  CONJUNTO INDEPENDIENTE MAXIMO EN UN CAMINO")
    print("="*60)
    print("1. Ingresar pesos de nodos (todos en una linea)")
    print("2. Usar ejemplo predefinido")
    print("3. Salir")
    print("="*60)
    
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opcion invalida. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un numero valido")
