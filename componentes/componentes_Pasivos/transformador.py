class Transformador:
    def __init__(self, voltaje_entrada, voltaje_salida, amperaje, cantidad=None):
        self.voltaje_entrada = voltaje_entrada
        self.voltaje_salida = voltaje_salida
        self.amperaje = amperaje
        self.cantidad = cantidad

    def __str__(self):
        return f"""
            \n*******Transformador (--CANTIDAD: {self.cantidad})\n🔸Voltaje Entrada: {self.voltaje_entrada} V\n🔸Voltaje Salida: {self.voltaje_salida}V\n🔸Amperaje: {self.amperaje}A        """


if __name__ == "__main__":
    transform = Transformador(127, 12, 0.2, 321)
    print(transform)
