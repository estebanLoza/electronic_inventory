# Componentes activos, como Transitores, Diodos, Amplificadores operaciones, compuertas lógicas


class Transitor:
    def __init__(self, nomenclatura, tipo_transitor):
        self.nomenclatura = nomenclatura
        self.tipo_transitor = tipo_transitor

    def __str__(self):
        return f"""
                ****************************************************************

                        NOTA --- TIENES SOLO LOS PINES DE 3 LOS MÁS COMUNES

                ****************************************************************


                \n Transitor({self.tipo_transitor})
                \n Nomenclatura: {self.nomenclatura}

        """
