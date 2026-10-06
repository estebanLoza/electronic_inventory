class Arduino:
    def __init__(self, tipo_arduino, chip):
        self.tipo_arduino = tipo_arduino
        self.chip = chip


class ArduinoUno(Arduino):
    def __init__(self, tipo_arduino, chip, pines_analog=6, pines_digital=6):
        super().__init__(tipo_arduino, chip)
        self.pines_analog = pines_analog
        self.pines_digital = pines_digital
        self.voltaje_minimo_in = 5
        self.voltaje_maximo_in = 12
        self.cantidad = None

    def __str__(self):
        return f"""
        ---    ARDUINO {self.tipo_arduino} &&& Cantidad {self.cantidad} ------ 
            Chip {self.chip}
            Pines Analogicos: {self.pines_analog}
            Pines Digitales: {self.pines_digital} 
            Voltaje Entrada Min - Max: {self.voltaje_minimo_in} V - {self.voltaje_maximo_in}
                   """


class ArduinoMega(Arduino):
    def __init__(self, tipo_arduino, chip, pines_analog=16, pines_digital=54):
        super().__init__(tipo_arduino, chip)
        self.pines_analog = pines_analog
        self.pines_digital = pines_digital
        self.voltaje_minimo_in = 5
        self.voltaje_maximo_in = 12
        self.cantidad = None

    def __str__(self):
        return f"""
        ----- ARDUINO {self.tipo_arduino} &&& Cantidad {self.cantidad} ------ 
            Chip {self.chip}
            Pines Analogicos: {self.pines_analog}
            Pines Digitales: {self.pines_digital} 
            Voltaje Entrada Min - Max: {self.voltaje_minimo_in} V - {self.voltaje_maximo_in}
                   """


### Pruebas


#
# if __name__ == "__main__":
#     arduino_uno = ArduinoUno("UNO", "Atmega328P")
#     print(arduino_uno)
#     arduino_mega = ArduinoMega("Mega", "Atmega2560")
#     print(arduino_mega)
