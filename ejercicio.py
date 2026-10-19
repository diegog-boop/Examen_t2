def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c, visitados):
    if f >= len(lab) or f < 0:
        return False
    if c >= len(lab[0]) or c < 0:
        return False
    if visitados[f][c]:
        return False
    if lab[f][c] == 0:
        return False
    return True

def obtener_valor(lab, f, c):
    valor = lab[f][c]
    if valor == 'I' or valor == 'F':
        return 1
    return int(valor)

def laberB(lab, res, visitados, f, c, puntos_acumulados):
    if not valido(lab, res, f, c, visitados):
        return False
    if lab[f][c] == 'F':
        puntos_totales = puntos_acumulados + obtener_valor(lab, f, c)
        if puntos_totales >= 23:
            res[f][c] = 1
            imprime(res)
            return True
        return False
    visitados[f][c] = True
    res[f][c] = 1
    puntos_actuales = puntos_acumulados + obtener_valor(lab, f, c)
    imprime(res)

    if laberB(lab, res, visitados, f - 1, c, puntos_actuales):
        return True
    elif laberB(lab, res, visitados, f, c + 1, puntos_actuales):
        return True
    elif laberB(lab, res, visitados, f + 1, c, puntos_actuales):
        return True
    elif laberB(lab, res, visitados, f, c - 1, puntos_actuales):
        return True
    else:
        res[f][c] = 0
        visitados[f][c] = False
        return False

lab = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]
visitados = [[False for _ in range(9)] for _ in range(9)]

print("Laberinto Original:")
imprime(lab)

if laberB(lab, res, visitados, 8, 0, 0):
    print("final del laberinto")
    imprime(res)
else:
    print("se queda atrapado")