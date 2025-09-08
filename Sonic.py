def esSolucion(casilla, casilla_fin, numeroUnos, contadorUnos):
    return casilla == casilla_fin and numeroUnos == contadorUnos


def esMejor(mejorSol, contador):
    return mejorSol > contador


def esFactible(n, datos, newF, newC):
    if newF < 0 or newF >= n or newC < 0 or newC >= n:
        return False
    elif datos[newF][newC] == 0 or datos[newF][newC] == 2 or datos[newF][newC] == 1:
        return True
    else:
        return False


def SonicSito(n, datos, casilla, casilla_fin, mejorSol, contador, visitados, numeroUnos, contadorUnos):
    if contador >= mejorSol:
        return mejorSol

    if esSolucion(casilla, casilla_fin, numeroUnos, contadorUnos):
        if esMejor(mejorSol, contador):
            mejorSol = contador
            return mejorSol
        else:
            return mejorSol

    f, c = casilla
    if visitados[f][c]:
        return mejorSol


    desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for d in desplazamientos:
        newF, newC = f + d[0], c + d[1]
        if esFactible(n, datos, newF, newC) and not visitados[newF][newC]:
            contadorAux = contador
            auxUnos = contadorUnos
            while esFactible(n, datos, newF, newC) and not visitados[newF][newC]:
                if datos[newF][newC] == 1:
                    auxUnos += 1
                contadorAux += 1
                newF += d[0]
                newC += d[1]
            visitados[f][c] = True
            mejorSol = SonicSito(n, datos, (newF - d[0], newC - d[1]), casilla_fin, mejorSol, contadorAux, visitados, numeroUnos, auxUnos)
            visitados[f][c] = False
    return mejorSol



n = int(input())
datos = []
numero_de_unos = 0
for _ in range(n):
    a = list(map(int, input().strip().split()))
    numero_de_unos += a.count(1)
    datos.append(a)
x1, y1, x2, y2 = map(int, input().strip().split())
casilla_ini = (x1, y1)
casilla_fin = (x2, y2)
visitados = [[False for _ in range(n)] for _ in range(n)]
numUnos = 0
if datos[x1][y1] == 1:
    numUnos = 1
mejorSol = SonicSito(n, datos, casilla_ini, casilla_fin, float('inf'), 1, visitados, numero_de_unos, numUnos)
print(mejorSol)