def inicializarTablero(n):
    sol = [-1] * n
    return sol


def inicializarTablero2(n):
    tablero = []
    for i in range(n):
        tablero.append([0]*n)
    return tablero

def imprimir(sol):
    N = len(sol)
    tablero = inicializarTablero2(N)
    for f in range(N):
        tablero[f][sol[f]] = 1
        print(tablero[f])


def damaEnColumna(sol, fila, col):
    # return col in sol
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] == col
        f += 1
    return encontrada

def damaEnDiagonal45(sol, fila, col):
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] + f == col + fila
        f += 1
    return encontrada

def damaEnDiagonal135(sol, fila, col):
    encontrada = False
    f = 0
    while not encontrada and f < fila:
        encontrada = sol[f] - f == col - fila
        f += 1
    return encontrada

def esFactible(sol, fila, col):
        return not (damaEnColumna(sol, fila, col) or damaEnDiagonal45(sol, fila, col) or damaEnDiagonal135(sol, fila, col))


def n_reinas_va(sol, fila):
    N = len(sol)
    if fila == N: #¿es solucion?
        esSol = True
    else:
        esSol = False
        col = 0
        while not esSol and col < N:
            if esFactible(sol, fila, col):
                sol[fila] = col
                sol, esSol = n_reinas_va(sol, fila+1)
            col = col + 1
        if not esSol:
            sol[fila] = -1
    return sol, esSol


n = int(input())
sol = inicializarTablero(n)
fila = 0
sol, esSol = n_reinas_va(sol, fila)
if esSol:
    print(f"{sol}\n")
    imprimir(sol)
else:
    print("no se ha encontrado solucion.")