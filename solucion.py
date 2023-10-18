def getTablero(n):
    torre1 = list(range(n, 0, -1))
    torre2 = []
    torre3 = []
    return (torre1, torre2, torre3)

def imprimirTablero(tablero):
    for i, torre in enumerate(tablero, start=1):
        print(f"Torre {i}: {torre}")

def solve(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        disco = origen.pop()
        destino.append(disco)
        movimientos.append(f"Mover disco {disco} de Torre {origen} a Torre {destino}")
    else:
        solve(n - 1, origen, auxiliar, destino, movimientos)
        disco = origen.pop()
        destino.append(disco)
        movimientos.append(f"Mover disco {disco} de Torre {origen} a Torre {destino}")
        solve(n - 1, auxiliar, destino, origen, movimientos)

if __name__ == "__main__":
    n = 5
    tablero = getTablero(n)

    print("Estado inicial del tablero:")
    imprimirTablero(tablero)

    movimientos = []
    solve(n, tablero[0], tablero[2], tablero[1], movimientos)

    print("\nLista de movimientos:")
    for movimiento in movimientos:
        print(movimiento)

    print("\nEstado final del tablero:")
    imprimirTablero(tablero)
