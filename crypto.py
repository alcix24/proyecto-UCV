def encryp(*args):
    """Esta funcion se encarga de codificar una oracion introducida"""
    q = args[0].lower()
    palabras = list(q)
    lista_aux = []
    while True:
        for i in palabras:
            w = letras.index(i)
            if i in letras:
                lista_aux.append(simbolos[w])
        if len(lista_aux) == len(palabras):
            break
    oracion = "".join(lista_aux)
    return oracion
def desCryp(*args):
    """Esta funcion se encargar de decodificar una oracion"""
    q = args[0].lower()
    palabras = list(q)
    lista_aux = []
    while True:
        for i in palabras:
            w = simbolos.index(i)
            if i in simbolos:
                lista_aux.append(letras[w])
        if len(lista_aux) == len(palabras):
            break
    oracion = "".join(lista_aux)
    return oracion
