def esSolucion(e, numeroVictimas):
    return e == numeroVictimas


def esMejor(mejorSol, contador):
    return mejorSol > contador


def esFactible(n, m, datos, newF, newC):
    if newF < 0 or newF >= n or newC < 0 or newC >= m:
        return False
    elif datos[newF][newC] == 1 or datos[newF][newC] == 0:
        return True
    else:
        return False


def moonknight(n, m, e, datos, param, d, mejorSol, contador, numeroVictimas, visitados):
    if contador >= mejorSol:
        return mejorSol
    elif esSolucion(e, numeroVictimas):
        if esMejor(mejorSol, contador):
            mejorSol = contador
    else:
        desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for dist in desplazamientos:
            newF = param[0] + dist[0]
            newC = param[1] + dist[1]
            if esFactible(n, m, datos, newF, newC) and not visitados[newF][newC]:
                numeroVictimasAux = numeroVictimas
                if datos[newF][newC] == 1:
                    numeroVictimasAux += 1
                visitados[newF][newC] = True
                mejorSol = moonknight(n, m, e, datos, (newF, newC), d, mejorSol, contador+1, numeroVictimasAux, visitados)
                visitados[newF][newC] = False
    return mejorSol


n, m, e = map(int, input().strip().split())
datos = []
for _ in range(n):
    a = list(map(int, input().strip().split()))
    datos.append(a)
x, y, d = map(int, input().strip().split())
if(datos[x][y] == 1):
    numeroVictimas = 1
else:
    numeroVictimas = 0
visitados = [[False for _ in range(m)] for _ in range(n)]
visitados[x][y] = True
mejorSol = moonknight(n, m, e, datos, (x, y), d, float('inf'), 0, numeroVictimas, visitados)
if mejorSol <= d:
    print("ATACA")
else:
    print("CORRE")