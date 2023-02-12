from agregar import *
from actualizar import *
from eliminar import *
from leer import *

acumulador={}
while True:
    print("-"*50)
    print(
    """
    Seleccione una acción.
    1. registrar usuario.
    2. actualizar usuario.
    3. eliminar usuario.
    4. visualizar usuarios
    (x) salir
    """
    )
    seleccion = input("selección: ")

    if seleccion == "1":
        registro_usuario(acumulador)

    if seleccion =="2":
        actualizar_usuario(acumulador)
    
    if seleccion == "3":
        eliminar_usuario(acumulador)
    
    if seleccion == "4":
        leer_usuario(acumulador)

    if seleccion == "x":
        break
    print("-"*50)