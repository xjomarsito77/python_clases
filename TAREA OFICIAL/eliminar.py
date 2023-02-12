from acumulador import *
def eliminar_usuario(nombre_usuario):
    if nombre_usuario in acumulador:
        del acumulador[nombre_usuario]