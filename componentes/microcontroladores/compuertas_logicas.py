class CompuertaLogica:
    def __init__(self, tipo_compuerta):
        self.tipo_compuerta = tipo_compuerta
        self.cantidad = None


class CompuertaAnd(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None

    def __str__(self):
        return f"""
            Compuerta Lógica: {self.tipo_compuerta} 
            Nomenclatura: {self.nomenclatura}
        """


class CompuertaOr(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None

    def __str__(self):
        return f"""
            Compuerta Lógica: {self.tipo_compuerta} 
            Nomenclatura: {self.nomenclatura}
        """


class CompuertaNot(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None


class CompuertaNand(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None


class CompuertaNor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None


class CompuertaXor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None


class CompuertaXnor(CompuertaLogica):
    def __init__(self, tipo_compuerta, nomenclatura):
        super().__init__(tipo_compuerta)
        self.nomenclatura = nomenclatura
        self.cantidad = None
