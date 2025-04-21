n = 10

tablero = []
tablero_visible = []


def graficar(tablero):
for fila in tablero:
for c in fila:
print(c, end="")
print()


for in range(n):
fila = ["🌊"] n
tablero.append(fila)

for in range(n):
fila = ["🌊"] n
tablero_visible.append(fila)

graficar(tablero_visible)
for i in range(3):
fila_random = (123456789 (2 + i)) % n
columna_random = (987654321 (6 + i)) % n
tablero[fila_random][columna_random] = "🚢"

while True:
inputFila: int = int(input("Ingrese fila: "))
inputColumna: int = int(input("Ingrese columna: "))

if tablero[inputFila][inputColumna] == "🚢":
print("Le diste a " + tablero[inputFila][inputColumna])
tablero[inputFila][inputColumna] = "🔥"
tablero_visible[inputFila][inputColumna] = "🔥"
graficar(tablero_visible)
else:
print("Volver a intentar")
for fila in tablero_visible:
tablero_visible[inputFila][inputColumna] = "❌"
graficar(tablero_visible)