class Vehículo:
    Color = None
    Ruedas = None
    Puertas = None

    def __init__(self, color, ruedas, puertas):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas


class Coche(Vehículo):
    Velocidad = None
    Cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.Velocidad = velocidad
        self.Cilindrada = cilindrada

    def mostrarAtributos(self):
        print("Color:", self.Color)
        print("Ruedas:", self.Ruedas)
        print("Puertas:", self.Puertas)
        print("Velocidad:", self.Velocidad)
        print("Cilindrada:", self.Cilindrada)

Dacia = Coche("negro", 4, 5, 150, 300)
Dacia.mostrarAtributos()
