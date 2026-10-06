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
        cantidad=None,
        ubicacion="",
    ):
        super().__init__(tipo_transitor)
        self.nomenclatura = nomenclatura
        self.tipo_senial = tipo_senial
        self.ganancia = ganancia
        self.volt_saturacion = volt_saturacion
        self.corriente_max = corriente_max
        self.cantidad = cantidad
        self.ubicacion = ubicacion

    def __str__(self):
        return f"""
            Transistor '{self.tipo_transitor}'
                Nomeclatura: {self.nomenclatura}
                Tipo señal: {self.tipo_senial}
                Volt Saturación: {self.volt_saturacion}
                Corriente Max: {self.corriente_max}
               """


class TransitorMosfet(Transitor):
    def __init__(
        self,
        tipo_transitor,
        nomenclatura,
        resistencia_encendido,
        volt_umbral,
        gate_charge,
        cantidad=None,
        ubicacion="",
    ):
        super().__init__(tipo_transitor)
        self.nomenclatura = nomenclatura
        self.resistencia_encendido = resistencia_encendido
        self.volt_umbral = volt_umbral
        self.gate_charge = gate_charge
        self.cantidad = cantidad
        self.ubicacion = ubicacion

    def __str__(self):
        return f"""
            Transistor '{self.tipo_transitor}'
                Nomenclatura: {self.nomenclatura}
                Resistencia Encendido: {self.resistencia_encendido}
                Volt Umbral: {self.volt_umbral}
                Gate Charge: {self.gate_charge}
        """
