class coche():
    def __init__(self,matricula,marca,kilometraje,gasolina):
        self.matricula= matricula
        self.marca=marca
        self.kilometraje=kilometraje
        self.gasolina=gasolina
        
    def avanzar(self,km):
        self.gasolina= self.gasolina - km
        self.kilometraje=self.kilometraje + km
        
omar = coche("JUT654","chevrolet joi",45,20)
omar.avanzar(25)
print(omar.gasolina)
print(omar.kilometraje)

if omar.gasolina < omar.kilometraje:
    print("Su numero esta por debajo de 0")
else:
    print("")        