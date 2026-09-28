

class Resistencia:
    def __init__(self, ohmios, potencia):
        self.ohmios = ohmios
        self.potencia = potencia
        self.tolerancia = 5


class Potenciometro(Resistencia):
    def __init__(self, ohmios, potencia, pines):
        super().__init__(ohmios, potencia)
        self.pines = pines

    def __str__(self):
        return f"Potenciometro {self.ohmios} Ohm, {self.potencia} W, Pines: {self.pines}"


class Capacitor:
    def __init__(self, tipo_capacitor, volt_max, capacitancia):
        self.tipo_capacitor = tipo_capacitor
        self.volt_max = volt_max
        self.capacitancia = capacitancia

    def clasificacion(self):

        if self.tipo_capacitor.lower() == "electrolitico":
            return self.capacitor_electrolitico()
        elif self.tipo_capacitor.lower() == "ceramico nf":
            return self.capacitor_ceramico_nf()
        elif self.tipo_capacitor.lower() == "ceramico pf":
            return self.capacitor_ceramico_pf()

    def capacitor_electrolitico(self):
        return f"Capacitor {self.capacitancia} mF, Voltaje Max: {self.volt_max}\n"

    def capacitor_ceramico_nf(self):
        return f"Capacitor Ceramico: {self.capacitancia} nF(nano faradio), Voltaje Max: {self.volt_max}\n"

    def capacitor_ceramico_pf(self):
        return f"Capacitor Ceramico: {self.capacitancia} pF (pico faradio), Voltaje Max: {self.volt_max}\n"


if __name__ == "__main__":

    capacitor = Capacitor("ceramico nf", 25, 100)
    capacitorDos = Capacitor("ceramico pf", 30, 101)

    potenciometro = Potenciometro(120, 32, 3)

    print(capacitor.clasificacion())
    print(capacitorDos.clasificacion())
    print(potenciometro)
