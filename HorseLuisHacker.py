def esSolucion(elementosRecogidos, p):
    return elementosRecogidos == p

def esFactible(lista, fila, col, n, m, visitado, siguienteElemento):
    if fila < 0 or fila >= n or col < 0 or col >= m or visitado[fila][col]:
        return False
    return lista[fila][col] == 0 or lista[fila][col] == siguienteElemento

def JoseLuis(lista, mejorSol, contador, fila, col, p, n, m, elementosRecogidos, siguienteElemento, visitado):
    if esSolucion(elementosRecogidos, p):
        return min(contador, mejorSol)

    visitado[fila][col] = True
    mejorLocal = float('inf')
    desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for des in desplazamientos:
        newF, newC = fila + des[0], col + des[1]
        if esFactible(lista, newF, newC, n, m, visitado, siguienteElemento):
            recogioElemento = lista[newF][newC] == siguienteElemento
            mejorLocal = min(mejorLocal, JoseLuis(lista, mejorSol, contador + 1, newF, newC, p, n, m, elementosRecogidos + recogioElemento, siguienteElemento + recogioElemento, visitado))

    visitado[fila][col] = False
    return min(mejorLocal, mejorSol)

n, m, p = map(int, input().strip().split())
lista = [list(map(int, input().strip().split())) for _ in range(n)]
visitado = [[False for _ in range(m)] for _ in range(n)]
sol = JoseLuis(lista, float('inf'), 1, 0, 0, p, n, m, 0, 1, visitado)
print(sol if sol != float('inf') else -1)

'''
def esSolucion(obj, tot):
    return obj-1 == tot

def esfactible(n, m, maze, newF, newC, sig):
    if 0 > newF or n <= newF or 0 > newC or m <= newC:
        return False
    if maze[newF][newC] == sig or maze[newF][newC] == 0:
        return True
    else:
        return False


def caballito(n, m, maze, mejorSol, contador, casilla, siguienteObj, numeroObj, visitados):
    if esSolucion(siguienteObj, numeroObj):
        mejorSol = min(contador, mejorSol)
        return mejorSol
    else:
        distancias = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for dist in distancias:
            newF = casilla[0] + dist[0]
            newC = casilla[1] + dist[1]
            if esfactible(n, m, maze, newF, newC, siguienteObj) and not visitados[newF][newC]:
                siguienteObjAux = siguienteObj
                if maze[newF][newC] == siguienteObjAux:
                    siguienteObjAux += 1
                visitados[newF][newC] = True
                mejorSol = caballito(n, m, maze, mejorSol, contador+1, (newF, newC), siguienteObjAux, numeroObj, visitados)
                visitados[newF][newC] = False
        return mejorSol


n, m, p = map(int, input().strip().split())
maze = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    maze.append(row)
visitados = [[False for _ in range(m)]for _ in range(n)]
mejorSol = caballito(n, m, maze, float('inf'), 1, (0, 0), 1, p, visitados)
print(mejorSol)
'''
