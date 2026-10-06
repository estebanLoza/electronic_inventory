class Fusible:
    def __init__(self, tipo_fusible, volt_max, amperaje, medida, cantidad=None):
        self.tipo_fusible = tipo_fusible
        self.volt_max = volt_max
        self.amperaje = amperaje
        self.medida = medida
        self.cantidad = cantidad

    def __str__(self):
        return f"""
            ----- Fusible {self.tipo_fusible.upper()} 🔰 CANTIDAD: {self.cantidad} ----- 
            🔶 Voltaje Max: {self.volt_max}
            🔶 Amperaje: {self.amperaje} A
            🔶 Medida: {self.medida} mm
            
        """
