# Importación dde las secciones

from sections.catalogo_Activos import CatalogoActivos
from componentes.componentes_Pasivos.resistencia import Resistencia

# Creando la clase de los catalogos
catalogo = CatalogoActivos()

catalogo.agregar(Resistencia(220, "ohm", 0.25, 5, cantidad=100))
catalogo.agregar(Resistencia(220, "ohm", 0.25, 5, cantidad=50))  # Se suma: 150


r = Resistencia(220, "ohm", 0.25, 5)
if catalogo.quitar(r.clave(), 30):
    print("Listo")
else:
    print("No existe o no hay suficientes unidades. ")


def opcion_agregar_zener():
    nomenclatura = input("Nomenclatura: ")
    voltaje = float(input("Voltaje nominal: "))
    potencia = float(input("Potencia(W): "))
    tolerancia = float(input("Tolerancia (%): "))
    cantidad = int(input("Cantidad: "))

    zener = DiodoZener(nomenclatura, voltaje, potencia, tolerancia, cantidad)
    catalogo.agregar(zener)
    print("Agregado")


def opcion_quitar():
    modelo = input("Modelo a quitar: ")
    cantidad = int(input("Cantidad: "))

    if catalogo.quitar(modelo, cantidad):
        print("Listo.")
    else:
        print("No existe ese modelo o no hay suficientes unidades.")


def menu():
    print("*" * 150)
    print(
        " " * 50
        + """

        ██████████  ██          ██████████    ██████    ██████████  ████████      ██████    ██      ██  ██████    ██████    
        █ ████████  ██          █ ████████    ██████    ████  ████  █ ██████      ██████    ██      ██  ██  ██    ██████    
        ██          ██          ██          ██              ██      ██      ██  ██      ██  █ ██    ██    ██    ██          
        ██          ██          ██          ██              ██      ██      ██  ██      ██  █ ██    ██    ██    ██          
        █ ██████    ██          █ ██████    ██              ██      █ ██████    ██      ██  ██  ██  ██    ██    ██          
        █ ██████    ██          █ ██████    ██              ██      █ ████ █    ██      ██  ██  ██  ██    ██    ██          
        ██          ██          ██          ██              ██      ██    ██    ██      ██  ██    ██ █    ██    ██          
        ██          ██          ██          ██              ██      ██    ██    ██      ██  ██    ██ █    ██    ██          
        █ ████████  █ ████████  █ ████████    ██████        ██      ██      ██    ██████    ██      ██  ██  ██    ██████    
        ██████████  ██████████  ██████████    ██████        ██      ██      ██    ██████    ██      ██  ██████    ██████            
    """
    )
    print("*" * 150)

    opcion_agregar_zener()
    opcion_quitar()


menu()
