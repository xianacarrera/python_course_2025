class Vehiculo():
    def __init__(self, vel_max, precio, color):
        self.vel_max = vel_max
        self.precio = precio
        self.color = color
    
    def __str__(self):
        return f"Vehículo con velocidad máxima {self.vel_max}, precio {self.precio} y color {self.color}"
    
    def moverse(self):
        print("Me estoy moviendo")
            
class Coche(Vehiculo):
    def __init__(self, vel_max, precio, color, mi_marca, mis_puertas):
        super().__init__(vel_max, precio, color)
        self.marca = mi_marca
        self.numero_de_puertas = mis_puertas
    
    def moverse(self):
        super().moverse()
        print("Me estoy moviendo brum brum....")

class Avion(Vehiculo):
    def __init__(self, vel_max, precio, color, mi_marca, mis_puertas):
        super().__init__(vel_max, precio, color)
        self.marca = mi_marca
        self.numero_de_puertas = mis_puertas
    
    def volar(self):
        print("estoy volando")

class Bicicleta(Vehiculo):
    pass
     
c = Coche(200, "100.000€", "red", "Porsche", 4)
     
     
c.moverse()


# c.volar() 

avion = Avion(2000, "100.000.000€", "white", "Boeing", 4)
avion.volar()
avion.moverse()