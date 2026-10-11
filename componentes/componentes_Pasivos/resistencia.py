class Resistencia:
    def __init__(self, ohmios, unidad, potencia, tolerancia, cantidad=0, ubicacion=""):
        self.ohmios = ohmios
        self.unidad = unidad
        self.potencia = potencia
        self.tolerancia = tolerancia
        self.cantidad = cantidad
        self.ubicacion = ubicacion

    def __str__(self):
        return (
            f"Resistencia {self.ohmios} {self.unidad}, "
            f"Potencia {self.potencia} W, Tolerancia: {self.tolerancia} %\n"
        )

    def clave(self):
        return ("resistencia", self.ohmios, self.unidad, self.potencia, self.tolerancia)


class Potenciometro(Resistencia):
    def __init__(
        self, ohmios, unidad, potencia, tolerancia, pines, cantidad=0, ubicacion=""
    ):
        super().__init__(ohmios, unidad, potencia, tolerancia, cantidad, ubicacion)
        self.pines = pines

    def clave(self):
        return (
            "potenciometro",
            self.ohmios,
            self.unidad,
            self.potencia,
            self.tolerancia,
            self.pines,
        )

    def __str__(self):
        return f"Potenciometro {self.ohmios} {self.unidad}, {self.potencia} W, Pines: {self.pines}"
