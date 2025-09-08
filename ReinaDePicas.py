def esSolucion(casilla, casillaFin, numeroDeR, contadorR):
    return casilla == casillaFin and numeroDeR == contadorR


def recompensasTramapa(n, m, datos):
    contador = 0
    for i in range(n):
        for j in range(m):
            if datos[i][j] == 'r':
                if not hayTorreta(datos, n, m, i, j):
                    contador += 1
    return contador


def hayTorreta(datos, n, m, newF, newC):
    desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for d in desplazamientos:
        auxF, auxC = newF + d[0], newC + d[1]
        if 0 <= auxF < n and 0 <= auxC < m and datos[auxF][auxC] == 't':
            return True
    return False


def esFactible(n, m, datos, newF, newC):
    if newF < 0 or newF >= n or newC < 0 or newC >= m:
        return False
    elif hayTorreta(datos, n, m, newF, newC):
        return False
    elif datos[newF][newC] in ['f', 'r', 'e']:
        return True
    else:
        return False

def Laberintico(n, m, datos, casilla, casillaFin, mejorSol, contador, visitados, numeroDeR, contadorR):
    if contador >= mejorSol:
        return mejorSol

    if esSolucion(casilla, casillaFin, numeroDeR, contadorR):
        return min(contador, mejorSol)

    fila, col = casilla
    desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for desp in desplazamientos:
        newF, newC = fila + desp[0], col + desp[1]
        if esFactible(n, m, datos, newF, newC) and not visitados[newF][newC]:
            if datos[newF][newC] == 'r':
                contadorR += 1
                recogioRecompensa = True
            else:
                recogioRecompensa = False
            aux = datos[newF][newC]
            datos[newF][newC] = 'w'
            mejorSol = Laberintico(n, m, datos, (newF, newC), casillaFin, mejorSol, contador+1, visitados, numeroDeR, contadorR)
            if recogioRecompensa:
                contadorR -= 1
            datos[newF][newC] = aux

    return mejorSol


n, m = map(int, input().strip().split())
datos = []
casillaIni = (0, 0)
casillaFin = (0, 0)
for i in range(n):
    a = list(input().strip().split())
    datos.append(a)
    if 's' in a:
        casillaIni = (i, a.index('s'))
    if 'e' in a:
        casillaFin = (i, a.index('e'))

numero_de_r = recompensasTramapa(n, m, datos)
visitados = [[False for _ in range(m)] for _ in range(n)]
visitados[casillaIni[0]][casillaIni[1]] = True
mejorSol = Laberintico(n, m, datos, casillaIni, casillaFin, float('inf'), 1, visitados, numero_de_r, 0)
print(mejorSol)


