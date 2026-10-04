class Capacitor:
    """
    Conceptos generales de los componentes capacitor
    """

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
