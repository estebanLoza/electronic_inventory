from sections.catalogo_Activos import CatalogoActivos
from sections.catalogo_Pasivos import CatalogoPasivos
from componentes.componentes_Activos.diodo import DiodoZener
from componentes.componentes_Pasivos.resistencia import Resistencia


activos = CatalogoActivos()
pasivos = CatalogoPasivos()

# Entrada


def pedir_numero(texto, tipo=float):
    """
    Repite la pregunta hasta que el usuario escriba un número válido.
    """

    while True:
        try:
            return tipo(input(texto))
        except ValueError:
            print("⚠️ Valor inválido, intenta de nuevo. ")


# Logo


def mostrar_logo():
    print("=" * 44)
    print("    ⚡ INVENTARIO ELECTRÓNICO ⚡".center(44))
    print("=" * 44)


## Opciones: Componentes Activos


def agregar_zener():
    nomenclatura = input("Nomenclatura: ").strip()
    voltaje = pedir_numero("Voltaje nominal (V): ")
    potencia = pedir_numero("Potencia (W): ")
    tolerancia = pedir_numero("Tolerancia(%): ")
    cantidad = pedir_numero("Cantidad: ", int)

    activos.agregar(DiodoZener(nomenclatura, voltaje, potencia, tolerancia, cantidad))
    print("✅ Zener Agregado.")


def quitar_activo():
    modelo = input("Nomenclatura a quitar: ").strip()
    cantidad = pedir_numero("Cantidad: ", int)

    if activos.quitar(modelo, cantidad):
        print("✅  Listo.")
    else:
        print("❌ No existe ese modelo o no hay suficientes unidades.")


## OPciones pasivos


def agregar_resistencia():
    ohmios = pedir_numero("Valor: ")
    unidad = input("Unidad (ohm/kOhm/MOhm): ").strip()
    potencia = pedir_numero("Potencia (W): ")
    tolerancia = pedir_numero("Tolerancia (%): ")
    cantidad = pedir_numero("Cantida: ", int)

    pasivos.agregar(Resistencia(ohmios, unidad, potencia, tolerancia, cantidad))

    print("✅ Resistencia agregada")


def quitar_resistencia():
    ohmios = pedir_numero("Valor: ")
    unidad = input("Unidad (ohm/ kOhm/ MOhm): ").strip()
    potencia = pedir_numero("Potencia (W): ")
    tolerancia = pedir_numero("Tolerancia: (%): ")
    cantidad = pedir_numero("Cantidad a quitar: ", int)

    molde = Resistencia(ohmios, unidad, potencia, tolerancia)
    if pasivos.quitar(molde.clave(), cantidad):
        print("✅ Listo.")
    else:
        print("❌ No existe ese modelo o no hay suficientes unidades.")


# ---- Resumenes


def ver_resumen():
    print("\n ---- Activos ----")
    for nombre, cant in activos.cantidad_por_tipo().items():
        print(f" {nombre}: {cant}")
    print(f"    Total: {activos.cantidad_total()}")

    print("\n --- Pasivos ---")
    for nombre, cant in pasivos.cantidad_por_tipo().items():
        print(f" {nombre}: {cant}")
    print(f" Total: {pasivos.cantidad_total()}")


OPCIONES = {
    "1": ("Agregar diodo zener", agregar_zener),
    "2": ("Quitar componente", quitar_activo),
    "3": ("Agregar resistencia", agregar_resistencia),
    "4": ("Quitar resistencia", agregar_resistencia),
    "5": ("Ver resumen de inventario", ver_resumen),
}


def menu():
    while True:
        print()
        mostrar_logo()
        for clave, (texto, _) in OPCIONES.items():
            print(f"  {clave})  {texto}")
        print("  0) Salir")

        opcion = input("\n Opción: ").strip()

        if opcion == "0":
            print("Hasta Luego 👋")
            break
        elif opcion in OPCIONES:
            OPCIONES[opcion][1]()
            input("\nEnter para continuar...")
        else:
            print("⚠️  Opción inválida.")


if __name__ == "__main__":
    menu()
