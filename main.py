# Importación dde las secciones

from sections.catalogo_Activos import CatalogoActivos
# from sections.catalogo_Pasivos import CatalogoPasivos

# Creando la clase de los catalogos
catalogo = CatalogoActivos()


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
