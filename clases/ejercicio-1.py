class Coche:

    def __init__(self, motor: int, color: str):
        self.motor = motor
        self.color = color

    def arrancar(self):
        print("El auto está arrancando")

    def frenar(self):
        print("El auto está frenando")

auto = Coche(1500, "negro")
auto.arrancar()
auto.frenar()
