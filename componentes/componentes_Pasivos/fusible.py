class Fusible:
    def __init__(
        self, tipo_fusible, volt_max, amperaje, medida, cantidad=0, ubicacion=""
    ):
        self.tipo_fusible = tipo_fusible
        self.volt_max = volt_max
        self.amperaje = amperaje
        self.medida = medida
        self.cantidad = cantidad
        self.ubicacion = ubicacion

    def __str__(self):
        return f"""
            ----- Fusible {self.tipo_fusible.upper()} 🔰 CANTIDAD: {self.cantidad} ----- 
            🔶 Voltaje Max: {self.volt_max}
            🔶 Amperaje: {self.amperaje} A
            🔶 Medida: {self.medida} mm  
            🔶 Ubicación: {self.ubicacion} mm
            
        """

    def clave(self):
        return (
            "fusible",
            self.tipo_fusible.lower(),
            self.volt_max,
            self.amperaje,
            self.medida,
        )
