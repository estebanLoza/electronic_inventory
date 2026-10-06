# Componentes activos, como Transitores, Diodos, Amplificadores operaciones, compuertas lógicas

## Esto ahora se convierte la parte "administrativo" de los componentes activos.

from componentes.componentes_Activos import *


class CataloActivos:
    def __init__(self, op, cantidad=None):
        self.op = op
        self.cantidad = cantidad
