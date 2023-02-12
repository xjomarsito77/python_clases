from acumulador import acumulador
def actualizar_usuario(dato1:list,
                     dato2:list,
)->list:
    """ACTUALIZAR DATO DEL DICCIONARIO

    Args:
        dato1 (list): nombre del usuario
        dato2 (list): nombre del libro

    Returns:
        list: _description_
    """
    print(acumulador)
    nom=input("ingrese nombre del usuario antiguo: ")
    tomo=input("ingrese nombre del libro antiguo : ")
    nomn=input("ingrese el nuevo usuario: ")
    tomon=input("ingrese el nuevo libro: ")
    dato1.remove(nom)
    dato2.remove(tomo)
    dato1.append(nomn)
    dato2.append(tomon)
    return
        