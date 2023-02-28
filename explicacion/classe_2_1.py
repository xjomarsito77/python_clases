class robot():
    #variable de clase
    x=0
    y=0
    
    def name(self,nombre) -> None:
        nombre=input("ingresa su nombre: ")
        self.nombre=nombre
        
    def arriba(self) -> None:
        l= int(input("cuantos pasos quieres accender [en numeros enteros]: "))
        self.y= self.y + l
   
    def abajo(self) -> None:
        l=int(input("cuantos pasos quieres descender [en numeros enteros]: "))
        self.y=self.y - l
    
    def derecha(self) -> None:
        l=int(input("cuantos pasos quieres para avanzar [en numeros enteros]:  "))
        self.x= self.x + l
    
    def izquierda(self) -> None:
        l=int(input("cuantos pasos quieres retroceder [en numeros enteros]: "))
        self.x=  self.x - l
    
    def posicion(self) -> None:
        print(f'las coordenadas son: {self.x},{self.y}')
    
   
    
robotcito = robot()
robotcito.name(nombre=str)
robotcito.arriba()
robotcito.abajo()
robotcito.derecha()
robotcito.izquierda()
robotcito.posicion()
