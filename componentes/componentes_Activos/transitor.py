## Molde solo para los Transitores, que sabiendo esto , ten encuenta que los principales tipos son
#


class Transitor:
    def __init__(self, tipo_transitor):
        self.tipo_transitor = tipo_transitor


class TransitorBJT(Transitor):
    def __init__(
        self,
        tipo_transitor,
        nomenclatura,
        tipo_senial,
        ganancia,
        volt_saturacion,
        corriente_max,
    ):
        super().__init__(tipo_transitor)
        self.nomenclatura = nomenclatura
        self.tipo_senial = tipo_senial
        self.ganancia = ganancia
        self.volt_stauracion = volt_saturacion
        self.corriente_max = corriente_max


class TransitorMosfet(Transitor):
    def __init__(self, tipo_transitor, resistencia_encendido, volt_umbral, gate_charge):
        super().__init__(tipo_transitor)
        self.resistencia_encendido = resistencia_encendido
        self.volt_umbral = volt_umbral
        self.gate_charge = gate_charge
