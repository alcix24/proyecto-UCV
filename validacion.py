def valInt(*args):
    """esta funcion si se introduce un argumentose verifica si es entero y en el caso de dos varifica si el primer argumento
    se encuentra en el rango establecido en el segundo argumento"""
    if len(args) == 0 or len(args) > 2:
        raise ValueError("la funcion valInt espera minimo 1 argumento y maximo 2")
    elif len(args) == 1 and type(args[0]) == type(1):
        return True
    elif len(args) == 1 and type(args[0]) != type(1):
        return False
    elif len(args) == 2 and type(args[0]) != type(1):
        return False
    elif len(args) == 2 and type(args[0]) == type(1):
        if type(args[1]) != type(()):
            if type(args[1]) != type([]):
                raise TypeError("la funcion valInt espera como segundo argumento una tupla o una lista")
        lista_aux = []
        a,b = min(args[1]),max(args[1])
        for j in range(a,b+1):
            if j in args[1]:
                lista_aux.append(j)
        if tuple(lista_aux) != args[1] and lista_aux != args[1]:
            raise ValueError("La tupla no esta ordenada de forma creciente")
        elif type(args[1]) == type([]):
            if args[0] in range(a,b+1):
                return True
            else:
                return False
        elif type(args[1]) == type(()):
                if args[0] in range(a,b+1) and args[0] != a and args[0] != b:
                    return True
                else:
                    return False
def valFloat(*args):
    """Esta funcion si se introduce un argumentose verifica si es flotante y en el caso de dos varifica si el primer argumento
    se encuentra en el rango establecido en el segundo argumento"""
    if len(args) == 0 or len(args) > 2:
        raise ValueError("la funcion valFloat espera minimo 1 argumento y maximo 2")
    elif len(args) == 1 and type(args[0]) == type(1.1):
        return True
    elif len(args) == 1 and type(args[0]) != type(1.1):
        return False
    elif len(args) == 2:
        if type(args[0]) != type(1.1):
            if type(args[1]) != type(()):
                if type(args[1]) != type([]):
                    raise TypeError("la funcion valFloat espera como segundo argumento una tupla o lista")
            elif type(args[1]) == type(()) or type(args[1]) == type([]):
                return False
        elif type(args[0]) == type(1.1):
            lista_aux = []
            lista_aux_2 = [int(args[1][0]),int(args[1][1])]
            k,l = int(min(args[1])),int(max(args[1]))
            for j in range(k,l+1):
                if j in lista_aux_2:
                    lista_aux.append(j)
            if tuple(lista_aux) != tuple(lista_aux_2) and lista_aux != lista_aux_2:
                raise ValueError("La tupla no esta ordenada de forma creciente")
            elif type(args[1]) == type([]):
                if int(args[0]) in range(k,l+1):
                    return True
                else:
                    return False
            elif type(args[1]) == type(()):
                    if int(args[0]) in range(k,l+1) and args[0] != min(args[1]) and args[0] != max(args[1]):
                        return True
                    else:
                        return False
def valComplex(*args):
    """Esta funcion introduce un argumentose verifica si es entero y en el caso de dos varifica si el primer argumento
    se encuentra en el rango establecido en el segundo argumento"""
    if len(args) == 0 or len(args) > 2:
        raise ValueError("la funcion valComplex espera minimo 1 argumento y maximo 2")
    elif len(args) == 1 and type(args[0]) == type(1 + 2j):
        return True
    elif len(args) == 1 and type(args[0]) != type(1 + 2j):
        return False
    elif len(args) == 2 and type(args[0]) != type(1 + 2j):
        return False
    elif len(args) == 2 and type(args[0]) == type(1 + 2j):
        if type(args[1]) != type(()):
            if type(args[1]) != type([]):
                raise TypeError("la funcion valComplex espera como segundo argumento una tupla o una lista")
        lista_aux = []
        a,b = min(args[1]),max(args[1])
        for j in range(a,b+1):
            if j in args[1]:
                lista_aux.append(j)
        if tuple(lista_aux) != args[1] and lista_aux != args[1]:
            raise ValueError("La tupla no esta ordenada de forma creciente")
        elif type(args[1]) == type([]):
            if abs(args[0]) in range(a,b+1):
                return True
            else:
                return False
        elif type(args[1]) == type(()):
            if int(abs(args[0])) in range(a,b+1) and int(abs(args[0])) != a and int(abs(args[0])) != b:
                return True
            else:
                return False
def valString(*args):
    """Esta funcion si se introduce un argumento verifica si es string, si se introduce 2 argumentos verifica que estos dos sean string e iguales"""
    if len(args) == 0 or len(args) > 2:
        raise TypeError("valString recibe un argumento o maximo 2")
    elif len(args) == 1:
        if type(args[0]) == type("a"):
            isString = True
        else:
            isString = False
    else:
        bool_1 = (type(args[0]) != type("a"))
        bool_2 = (type(args[1]) != type("a"))
        if bool_1 or bool_2:
            isString = False
        elif args[0] != args[1]:
            isString = False
        else:
            isString = True
    return isString
def valList(*args):
    """Esta funcion si se introduce 1 argumento verifica que sea una lista, si se introduce 3 argumentos y el tercer argumento es value y el segundo es una lista este verifica si son iguales,
    si el tercer argumento es len y el segundo un entero este verifica si la longitud del primer argumento corresponde al segundo argumento"""
    if len(args) == 2 or len(args) > 3:
        raise TypeError("la funcion valList espera 1 o 3 argumentos")
    elif len(args) == 1 and type(args[0]) == type([1]):
        return True
    elif len(args) == 1 and type(args[0]) != type([1]):
        return False
    elif len(args) == 3:
        if type(args[1]) != type(1):
            a = args[2].lower()
            if type(args[2]) != type("a"):
                raise TypeError("argumentos no validos")
        elif type(args[1]) != type([]):
            if type(args[2]) != type("a"):
                raise TypeError("argumentos no validos")
        elif valString(a,"value") == False and valString(a,"len") == False:
            raise ValueError("el tercer argumento solo puede ser value o len")
        elif valString(a,"value") and type(args[0]) == type([]) and type(args[1]) == type([]) and args[0] == args[1]:
            return True
        elif valString(a,"value") and type(args[0]) != type([]):
            return False
        elif valString(a,"value") and type(args[1]) != type([]):
            return False
        elif valString(a,"value") and args[0] != args[1]:
            return False
        elif valString(a,"len") and type(args[0]) == type([]) and type(args[1]) == type(1) and len(args[0]) == args[1]:
            return True
        elif valString(a,"len") and type(args[0]) != type([]):
            return False
        elif valString(a,"len") and len(args[0]) != args[1]:
            return False
print(valList([1],[1],"len"))
