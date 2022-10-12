class Vehiculo:
    patente = ""
    color=""
    chassis =""
    puertas=0
    __velocidad=0
    latitud=0.0
    longitud=0.0
    distancia=0
    def acelerar(self):
        self.__velocidad += 10 #velodcidad = velocidad + 10
    def frenar(self):
        self.__velocidad -= 10 #velodcidad = velocidad + 10
    def setVelocidad(self,cuanto) -> None:
        self.__velocidad = cuanto
    def getVelocidad(self) -> int:
        return self.__velocidad
    def __init__(self, velocidad=0, marca="",latitud=0, longitud=0) -> None:
        self.__velocidad = velocidad
        self.latitud = latitud
        self.longitud = longitud
        self.marca = marca
        pass

objeto = Vehiculo(100,"Mazda")
#objeto.__velocidad = 1000
#objeto.setVelocidad(123)
print(objeto.getVelocidad())







############################### EXPLICACION DE GLOBAL ###########################
'''
velocidad = 0
def acelerar(cuanto):
    global velocidad
    velocidad +=cuanto
    return velocidad

print(acelerar())
'''