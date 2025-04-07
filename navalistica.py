n = 10
turno = 1

tablero = []
tablero_visible = []
tablero_visible2 = []

# Generar tablero general

for _ in range(n):
    fila = [" "] * n
    tablero.append(fila)

# Generar tablero visible 1

for _ in range(n):
    fila = [" "] * n
    tablero_visible.append(fila)

for fila in tablero_visible:
    print(fila)

# Generar tablero visible 2

for _ in range(n):
    fila = ["🌊"] * n
    tablero_visible2.append(fila)

for fila in tablero_visible2:
    print(fila)

for i in range(3):
    ubicarFilaBarcos: int = int(input("Ingrese fila del barco: "))
    ubicarColumnaBarcos: int = int(input("Ingrese fila del barco: "))
    tablero[ubicarFilaBarcos][ubicarColumnaBarcos] = "🚢"

while True:
    inputFila: int = int(input("Ingrese fila: "))
    inputColumna: int = int(input("Ingrese columna: "))

    if tablero[inputFila][inputColumna] == "🚢":
        print("Le diste a " + tablero[inputFila][inputColumna])
        tablero[inputFila][inputColumna] = "🔥"
        tablero_visible[inputFila][inputColumna] = "🔥"
        for fila in tablero_visible:
            print(fila)
    else:
        print("Volver a intentar")
        for fila in tablero_visible:
            tablero_visible[inputFila][inputColumna] = "🤣"
            print(fila)


for fila in tablero:
    print(fila)

