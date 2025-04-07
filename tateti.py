numeroTurno: int = 1

tablero: list[list[str]] = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turno: str = "X"

while True:
    print("Turno de", turno)
    fila: int = int(input("Ingrese la fila: "))
    columna: int = int(input("Ingrese la columna: "))
    
    # Verifica si la casilla está ocupada
    if tablero[fila][columna] != " ":
        print("Esa casilla ya está ocupada. Intenta de nuevo.")
        continue
    
    tablero[fila][columna] = turno
    
    # Imprimir el tablero
    for fila in tablero:
        print(fila)
    
    # Alternar el turno
    turno = "O" if turno == "X" else "X"