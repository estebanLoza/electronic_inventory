class Resistencia:
    def __init__(self, ohmios, unidad, potencia, tolerancia):
        self.ohmios = ohmios
        self.unidad = unidad
        self.potencia = potencia
        self.tolerancia = tolerancia

    def __str__(self):
        if self.unidad == "ohm":
            return f"Resistencia {self.ohmios} Ohm, Potencia {self.potencia} W, Tolerancia: {self.tolerancia} %\n"
        elif self.unidad == "kOhm":
            return f"Resistencia {self.ohmios} kOhm, Potencia {self.potencia} W, Tolerancia: {self.tolerancia} %\n"
        elif self.unidad == "MOhm":
            return f"Resistencia {self.ohmios} kOhm, Potencia {self.potencia} W, Tolerancia: {self.tolerancia} %\n"
        else:
            return "Esa clasificación no existe (Al menos no por el momento)"


class Potenciometro(Resistencia):
    def __init__(self, ohmios, potencia, unidad, pines, cantidad=0, ubicacion=""):
        super().__init__(ohmios, potencia, unidad)
        self.pines = pines

    def __str__(self):
        return f"Potenciometro {self.ohmios} {self.unidad}, {self.potencia} W, Pines: {self.pines}"
