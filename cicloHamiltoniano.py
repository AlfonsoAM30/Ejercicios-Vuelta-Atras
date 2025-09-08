
def esSol(sol, grafo):
    estanTodos = len(sol) == len(grafo)
    formanCiclo = grafo[sol[0]][sol[-1]] == 1
    return estanTodos and formanCiclo


def ciclo(sol, grafo, i):
    if esSol(sol, grafo):
        print(sol)
    else:
        vertice = 1
        while vertice < len(sol):
            sol.append(vertice)
            ciclo(sol, grafo, i+1)
            del sol[-1]
        vertice += 1

grafo = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1]
]

origen = 0
sol = [origen]
ciclo(sol, grafo, 1)