# Componentes activos, como Transitores, Diodos, Amplificadores operaciones, compuertas lógicas

## Esto ahora se convierte la parte "administrativo" de los componentes activos.

from componentes.componentes_Activos.diodo import Diodo, Led, DiodoZener
from componentes.componentes_Activos.transitor import (
    Transitor,
    TransitorBJT,
    TransitorMosfet,
)


class CatalogoActivos:
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        """
        Si el modelo ya existe, suma la cantidad: si no existe lo añade
        """
        existente = self.buscar_por_modelo(getattr(componente, "nomenclatura", None))
        if existente:
            existente.cantidad += componente.cantidad
        else:
            self.componentes.append(componente)

    def quitar(self, nomenclatura, cantidad):
        """
        Resta unidades. Devuelve True si pudo, False si no.
        """
        componente = self.buscar_por_modelo(nomenclatura)
        if componente is None or componente.cantidad < cantidad:
            return False
        componente.cantidad -= cantidad
        return True

    def buscar_por_modelo(self, nomenclatura):
        if nomenclatura is None:
            return None
        for c in self.componentes:
            if getattr(c, "nomenclatura", None) == nomenclatura:
                return c
        return None

    def cantidad_total(self):
        return sum(c.cantidad for c in self.componentes)

    def cantidad_por_tipo(self):
        """
        Devuelve como dict {"Led ": 50, "DiodoZener": 20}
        """
        resumen = {}
        for c in self.componentes:
            nombre = type(c).__name__  ## Led, DiodoZener, TransitorBJT
            resumen[nombre] = resumen.get(nombre, 0) + c.cantidad
        return resumen

    def cantidad_por_modelo(self):
        return {
            c.nomenclatura: c.cantidad
            for c in self.componentes
            if hasattr(c, "nomenclatura")
        }
