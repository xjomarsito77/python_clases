listas= [1,2,3,4]


def funciones(parametros):
    print(parametros)
    listas.append(parametros)
    variable = parametros*2
    print(variable)
    listas.append(variable)
    
funciones("felipe")
#print(variable)    