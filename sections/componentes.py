# Clasificación de componentes
from componentesPasivos import Resistencia, Potenciometro


class Componentes:
    def __init__(self, tipo_componente, cantidad):
        self.tipo_componente = tipo_componente
        self.cantidad = 0

    def agregar_stock(self, n):
        self.cantidad += n

    def quitar_stock(self, n):
        if n > self.cantidad:
            raise ValueError(f"No hay suficientes componentes {
                             self.tipo_componente}")
        self.cantidad -= n


if __name__ == "__main__":
