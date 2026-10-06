# Aquí aplicaré solo una clase para los esp32.


# Creación del objeto en GENERAL del esp32.
class Esp32:
    def __init__(
        self, chip, modelo, sd_card=False, wifi=False, bluetooth=False, antena=False
    ):
        self.chip = chip
        self.modelo = modelo
        self.sd_card = sd_card
        self.wifi = wifi
        self.bluetooth = bluetooth
        self.antena = antena


class Esp32V2(Esp32):
    def __init__(
        self,
        chip,
        modelo,
        puerto,
        memoria_rom=448,
        memoria_sram=520,
        sd_card=False,
        wifi=True,
        bluetooth=True,
        antena=True,
        cantidad=None,
    ):
        super().__init__(chip, modelo, sd_card, wifi, bluetooth, antena)
        self.puerto = puerto
        self.memoria_rom = memoria_rom
        self.memoria_sram = memoria_sram


# Aquí agrego la segudna clase de esp32-cam, pero este es lo mismo por lo tanto heredo lo mismo


class Esp32Cam(Esp32V2):
    def __init__(
        self,
        chip,
        modelo,
        puerto,
        memoria_rom=448,
        memoria_sram=520,
        sd_card=True,
        wifi=True,
        bluetooth=True,
        antena=True,
        cantidad=None,
        module_cam=True,
    ):
        super().__init__(
            chip,
            modelo,
            puerto,
            memoria_rom,
            memoria_sram,
            sd_card,
            wifi,
            bluetooth,
            antena,
        )
        self.module_cam = module_cam
