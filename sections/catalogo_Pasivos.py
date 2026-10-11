# Este código solo es la cración de los Objetos/Componentes.

# En componentes Activos son las Resistencias, Capacitores, Transformadores e Inductores
# **** Capacitores


class CatalogoPasivos:
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        """
        Si ya existe el mismo modelo, suma la cantidad; si no, lo añade.
        """

        existe = self.buscar(componente.clave())
        if existe:
            existe.cantidad += componente.cantidad
        else:
            self.componentes.append(componente)

    def quitar(self, clave, cantidad):
        """
        Resta unidades. Devuelve True si pudo, False si no.
        """

        componente = self.buscar(clave)
        if componente is None or componente.cantidad < cantidad:
            return False
        componente.cantidad -= cantidad

        return True

    def buscar(self, clave):
        for c in self.componentes:
            if c.clave() == clave:
                return c
        return None

    def cantidad_total(self):
        return sum(c.cantidad for c in self.componentes)

    def cantidad_por_tipo(self):
        """
        Devuelve {"capacitor": 40, "Resistencia": 300,...}

        """

        resumen = {}
        for c in self.componentes:
            nombre = type(c).__name__
            resumen[nombre] = resumen.get(nombre, 0) + c.cantidad
        return resumen
