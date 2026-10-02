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


class Diodo:
    def __init__(self, tipo_diodo):
        self.tipo_diodo = tipo_diodo

    def __str__(self):
        return f"{self.tipo_diodo}"


class Led(Diodo):
    def __init__(
        self,
        tipo_diodo,
        pines,
        dimension,
        color,
        # consumo_voltaje,
        # consumo_amp = 0.2,
        unidad_amp,
    ):
        super().__init__(tipo_diodo)
        self.pines = pines
        self.dimension = dimension
        self.color = color
        # self.consumo_voltaje = consumo_voltaje
        self.consumo_amp = 0.2
        self.unidad_amp = unidad_amp

    def __str__(self):

        # Aquí agrega una condicional sobre los colores, etc.

        return (
            f"🔵 Diodo {self.tipo_diodo.upper()}\n"
            f"🔶 Pines: {self.pines}\n"
            f"💡 Tamaño: {self.dimension} mm\n"
            f"🎨 Color: {self.color}\n"
            f"⚡ Voltaje típico: {self.voltaje_tipico} V\n"
            f"🔋 Consumo: {self.consumo_amp} {self.unidad_amp}\n"
        )

    @property
    def voltaje_tipico(self):
        match self.color:
            case "rojo":
                return "1.6-2.0"
            case "naranja":
                return "1.7-2.2"
            case "amarillo":
                return "2.1-2.4"
            case "verde":
                return "2.0-3.5"
            case "azul":
                return "3.0 - 3.8"
            case "blanco":
                return " 3.2 - 3.6"
            case "morado":
                return "3.4-4.0"
            case _:
                return "Color DESCONOCIDO"


class DiodoZener(Diodo):
    def __init__(self, nomenclatura, voltaje_tipico, potencia, tolerancia):
        self.nomenclatura = nomenclatura
        self.voltaje_nominal = voltaje_tipico
        self.potencia = potencia
        self.tolerancia = tolerancia
        self.cantidad = 0
        self.ubicacion = ""


if __name__ == "__main__":
    led = Led("Led", 3, 5, "rojo", "mA")

    print(led)
