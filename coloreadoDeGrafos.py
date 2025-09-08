def inicializarGrafo():
    g = [[1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1]]
    return g


def inicializarSolucion(longitud):
    return [0] * longitud


def esSol(sol, vertice):
    return vertice == len(sol)


def Esfactible(grafo, sol, vertice, color):
    solu = True
    fila = grafo[vertice]
    for i, elem in enumerate(fila):
        if elem == 1 and i != vertice:
            if sol[i] == color:
                return False
    return solu


def colores(sol, grafo, m, vertice):
    if esSol(sol, vertice):
        print(sol)
    else:
        color = 1
        while color <= m:
            if Esfactible(grafo, sol, vertice, color):
                sol[vertice] = color
                colores(sol, grafo, m, vertice+1)
                sol[vertice] = 0
            color += 1


grafo = inicializarGrafo()
m = 3
sol = inicializarSolucion(4)
colores(sol, grafo, m, 0)