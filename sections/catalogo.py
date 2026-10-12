## Esta parte será para agregar o quitar componentes.


class Catalogo:
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        existente = self.buscar(componente.clave())
        if existente:
            existente.cantidad += componente.cantidad
        else:
            self.componentes.append(componente)

    def quitar(self, clave, cantidad):
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

    def listar(self):
        return list(self.componentes)

    def cantidad_total(self):
        return sum(c.cantidad for c in self.componentes)

    def cantidad_por_tipo(self):
        resumen = {}
        for c in self.componentes:
            nombre = type(c).__name__
            resumen[nombre] = resumen.get(nombre, 0) + c.cantidad
        return resumen
