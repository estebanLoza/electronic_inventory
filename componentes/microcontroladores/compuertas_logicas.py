class CompuertaLogica:
    def __init__(self, tipo_compuerta, nomenclatura):
        self.tipo_compuerta = tipo_compuerta
        self.cantidad = None


class CompuertaAnd(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaOr(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaNot(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaNand(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaNor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaXor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None


class CompuertaXnor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta, nomenclatura)
        self.cantidad = None
