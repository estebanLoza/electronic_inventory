# Lista de Componentes Pasivos

class Resistencia:
    def __init__(self, ohmios, unidad, potencia):
        self.ohmios = ohmios
        self.unidad = unidad
        self.potencia = potencia
        self.tolerancia = 5

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
    def __init__(self, ohmios, potencia, unidad, pines):
        super().__init__(ohmios, potencia, unidad)
        self.pines = pines

    def __str__(self):
        return f"Potenciometro {self.ohmios} {self.unidad}, {self.potencia} W, Pines: {self.pines}"

# *** Capacitor


class Capacitor:
    def __init__(self, tipo_capacitor, volt_max, capacitancia, unidad):
        self.tipo_capacitor = tipo_capacitor
        self.volt_max = volt_max
        self.capacitancia = capacitancia
        self.unidad = unidad

    def __str__(self):
        if self.tipo_capacitor.lower() == "electrolitico":
            return self.capacitor_electrolitico()
        elif self.tipo_capacitor.lower() == "ceramico" and self.unidad == "nf":
            return self.capacitor_ceramico_nf()
        elif self.tipo_capacitor.lower() == "ceramico" and self.unidad == "pf":
            return self.capacitor_ceramico_pf()

    def capacitor_electrolitico(self):
        return f"Capacitor {self.capacitancia} mF, Voltaje Max: {self.volt_max}\n"

    def capacitor_ceramico_nf(self):
        return f"Capacitor Ceramico: {self.capacitancia} {self.unidad} (nano faradio), Voltaje Max: {self.volt_max}\n"

    def capacitor_ceramico_pf(self):
        return f"Capacitor Ceramico: {self.capacitancia} {self.unidad} (pico faradio), Voltaje Max: {self.volt_max}\n"


class Transformador:
    def __init__(self, voltaje_entrada, voltaje_salida, amperaje):
        self.voltaje_entrada = voltaje_entrada
        self.voltaje_salida = voltaje_salida
        self.amperaje = amperaje
        self.tap_central = True

    def __str__(self):
        return f"""
            \n*******Transformador\n🔸Voltaje Entrada: {self.voltaje_entrada} V\n🔸Voltaje Salida: {self.voltaje_salida}V\n🔸Amperaje: {self.amperaje}A        """


# if __name__ == "__main__":
#
#     capacitor = Capacitor("ceramico", 25, 100, "nf")
#     capacitorDos = Capacitor("ceramico", 30, 101, "pf")
#
#     potenciometro = Potenciometro(120, "kOhm", 32, 3)
#
#     resistencia = Resistencia(32, "ohm", 32)
#
#     transformador = Transformador(123, 24, 5)
#
#     print(capacitor)
#     print(capacitorDos)
#
#     print(potenciometro)
#     print(resistencia)
#     print(transformador)
