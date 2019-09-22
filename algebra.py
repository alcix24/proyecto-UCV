def proVec(*args):
    """Esta funcion se encarga de realizar el producto vectorial entre 2 vectores"""
    resultado = []
    i,j,k = (args[0][1] * args[1][2]) - (args[0][2] * args[1][1]) , ((args[0][0] * args[1][2]) - (args[0][2] * args[1][0])) * (-1) , (args[0][0] * args[1][1]) - (args[0][1] * args[1][0])
    resultado.append(i)
    resultado.append(j)
    resultado.append(k)
    return resultado
def traspo(*args):
    """esta funcion se encarga de trasponer una matriz"""
    filas,columnas = len(args),len(args[0])
    matriz_r = []
    for i in range(0,filas):
        lista_aux = []
        for j in range(0,columnas):
            lista_aux.append(args[j][i])
        matriz_r.append(lista_aux)
    return matriz_r
def multiM(*args):
    """esta funcion se encarga de ralizar la multuplicacion entre 2 matrices"""
    filas_1,filas_2 = len(args[0]),len(args[1])
    columnas_1,columnas_2 = len(args[0][0]),len(args[1][0])
    matriz_r = []
    for k in range(filas_1):
        matriz_r.append([0]*columnas_2)
        for i in range(columnas_2):
            matriz_r[k][i] = 0
    for i in range(filas_1):
        for j in range(columnas_1):
            for k in range(columnas_2):
                matriz_r[i][k] = matriz_r[i][k] + args[0][i][j] * args[1][j][k]
    return matriz_r
