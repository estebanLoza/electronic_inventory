class Transformador:
    def __init__(self, voltaje_entrada, voltaje_salida, amperaje):
        self.voltaje_entrada = voltaje_entrada
        self.voltaje_salida = voltaje_salida
        self.amperaje = amperaje

    def __str__(self):
        return f"""
            \n*******Transformador\n🔸Voltaje Entrada: {self.voltaje_entrada} V\n🔸Voltaje Salida: {self.voltaje_salida}V\n🔸Amperaje: {self.amperaje}A        """
