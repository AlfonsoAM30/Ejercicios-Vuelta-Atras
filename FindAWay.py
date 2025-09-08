def isFactible(cel, mat):
    return 0 <= cel[0] < len(mat) and 0 <= cel[1] < len(mat) and mat[cel[0]][cel[1]] == 0


def bt(mat, cel, celdasparavisitar, celdasvisitadas):
    esSolucion = False
    if celdasvisitadas == celdasparavisitar and cel[0] == len(mat)-1 and cel[1] == len(mat)-1:
        esSolucion = True
    else:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dirs:
            nextX = cel[0]+d[0]
            nextY = cel[1]+d[1]
            if isFactible((nextX, nextY), mat):
                mat[nextX][nextY] = celdasvisitadas
                esSolucion = bt(mat, (nextX, nextY), celdasparavisitar, celdasvisitadas+1)
                if esSolucion:
                    return True
                mat[nextX][nextY] = 0
    return esSolucion


n = int(input().strip())
mat = []
celdasparavisitar = 0
for _ in range(n):
    row = list(map(int, input().strip().split()))
    celdasparavisitar += (n + sum(row))
    mat.append(row)
ini_cel = (0, 0)
end_cel = (n-1, n-1)
if bt(mat, ini_cel, celdasparavisitar, 1):
    print("SI")
else:
    print("NO")