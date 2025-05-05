n = 10

tablero = []
tablero_visible = []

import random

def graficar(tablero):
    for fila in tablero:
        for c in fila:
            print(c, end=" ")
        print()

for _ in range(n):
    fila = ["🌊"] * n
    tablero.append(fila)

for _ in range(n):
    fila = ["🌊"] * n
    tablero_visible.append(fila)

graficar(tablero_visible)

for i in range(3):
    fila_random = (123456789 * (2 + i)) % n
    columna_random = (987654321 * (6 + i)) % n
    tablero[fila_random][columna_random] = "🚢"

while True:
    inputFila = int(input("Ingrese fila (0-9): "))
    inputColumna = int(input("Ingrese columna (0-9): "))

    if tablero[inputFila][inputColumna] == "🚢":
        print("¡Le diste a un barco!")
        tablero[inputFila][inputColumna] = "🔥"
        tablero_visible[inputFila][inputColumna] = "🔥"
        graficar(tablero_visible)
    else:
        print("¡Agua! Intenta de nuevo.")
        tablero_visible[inputFila][inputColumna] = "❌"
        graficar(tablero_visible)
