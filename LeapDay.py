def esSolucion(casilla, casilla_fin):
    return casilla == casilla_fin


def esMejor(mejorSol, contador):
    return mejorSol > contador


def esFactible(n, m, lista, casillaSig, d):
    if casillaSig[0] < 0 or casillaSig[0] >= n or casillaSig[1] < 0 or casillaSig[1] >= m:
        return False
    elif lista[casillaSig[0]][casillaSig[1]] == 0 or lista[casillaSig[0]][casillaSig[1]] == 4:
        return True
    elif lista[casillaSig[0]][casillaSig[1]] == 1:
        return False
    elif lista[casillaSig[0]][casillaSig[1]] == 2 and -2 < d[0] < 2 and -2 < d[1] < 2:
        return True
    else:
        return False


def nivelPasar(n, m, lista, visitados, casilla, casilla_ini, casilla_fin, mejorSol, contador, esSaltoDoble):
    if contador >= mejorSol:
        return mejorSol
    if esSolucion(casilla, casilla_fin):
        if esMejor(mejorSol, contador):
            mejorSol = contador
    else:
        desplazamientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if not esSaltoDoble:
            desplazamientos += [[0, 2], [2, 0], [0, -2], [-2, 0]]
        for d in desplazamientos:
            newF = casilla[0] + d[0]
            newC = casilla[1] + d[1]
            casillaSig = (newF, newC)
            if esFactible(n, m, lista, casillaSig, d) and not visitados[newF][newC]:
                visitados[newF][newC] = True
                salto_incremento = 2 if abs(d[0]) == 2 or abs(d[1]) == 2 else 1
                mejorSol = nivelPasar(n, m, lista, visitados, casillaSig, casilla_ini, casilla_fin, mejorSol, contador + salto_incremento, abs(d[0]) == 2 or abs(d[1]) == 2)
                visitados[newF][newC] = False
    return mejorSol


n, m = map(int, input().strip().split())
lista = []
casilla_ini = (0, 0)
casilla_fin = (0, 0)
encontrado = False
encontrado2 = False
for i in range(n):
    a = list(map(int, input().strip().split()))
    lista.append(a)
    if 3 in a and not encontrado:
        casilla_ini = (i, a.index(3))
        encontrado = True
    if 4 in a and not encontrado2:
        casilla_fin = (i, a.index(4))
        encontrado2 = True
visitados = [[False for _ in range(m)] for _ in range(n)]
mejorSol = nivelPasar(n, m, lista, visitados, casilla_ini, casilla_ini, casilla_fin,  float('inf'), 1, True)
if mejorSol % 2 == 0:
    mejorSol -= 2
print(mejorSol)
