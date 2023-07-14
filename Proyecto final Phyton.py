import random

def generar_matriz(n):
    """
    Genera una matriz cuadrada de tamaño n x n con números aleatorios entre 0 y 9.
    """
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def calcular_sumas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna de la matriz.
    Retorna dos listas, una con las sumas de las filas y otra con las sumas de las columnas.
    """
    n = len(matriz)
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(matriz[i][j] for i in range(n)) for j in range(n)]
    return sumas_filas, sumas_columnas

def imprimir_matriz(matriz):
    """
    Imprime la matriz en pantalla.
    """
    for fila in matriz:
        print(fila)

def imprimir_sumas(sumas_filas, sumas_columnas):
    """
    Imprime las sumas de cada fila y columna en pantalla.
    """
    print("Sumas de filas:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i + 1}: {suma}")
    
    print("\nSumas de columnas:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i + 1}: {suma}")

try:
    # Solicitar al usuario el tamaño de la matriz
    N = int(input("Ingresa el tamaño de la matriz (N): "))

    # Generar la matriz
    matriz = generar_matriz(N)

    # Imprimir la matriz generada
    print("Matriz generada:")
    imprimir_matriz(matriz)

    # Calcular las sumas de filas y columnas
    sumas_filas, sumas_columnas = calcular_sumas(matriz)

    # Imprimir las sumas de filas y columnas
    imprimir_sumas(sumas_filas, sumas_columnas)

except ValueError:
    print("Error: El tamaño de la matriz debe ser un número entero.")

