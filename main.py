from sections.catalogo_Activos import CatalogoActivos
from sections.catalogo_Pasivos import CatalogoPasivos


from componentes.componentes_Activos.diodo import Led, DiodoZener
from componentes.componentes_Activos.transitor import TransitorBJT, TransitorMosfet
from componentes.componentes_Pasivos.capacitor import Capacitor
from componentes.componentes_Pasivos.fusible import Fusible
from componentes.componentes_Pasivos.resistencia import Resistencia, Potenciometro
from componentes.componentes_Pasivos.transformador import Transformador


activos = CatalogoActivos()
pasivos = CatalogoPasivos()


# Cada tipo: (nombre, clase, valores fijos, [(atributo, pregunta, tipo)])
TIPOS_ACTIVOS = {
    "1": (
        "Diodo zener",
        DiodoZener,
        {},
        [
            ("nomenclatura", "Nomenclatura", str),
            ("voltaje_nominal", "Voltaje nominal (V)", float),
            ("potencia", "Potencia (W)", float),
            ("tolerancia", "Tolerancia (%)", float),
        ],
    ),
    "2": (
        "LED",
        Led,
        {"tipo_diodo": "led"},
        [
            ("pines", "Pines", int),
            ("dimension", "Tamaño (mm)", float),
            ("color", "Color", str),
            ("unidad_amp", "Unidad de corriente (mA/A)", str),
        ],
    ),
    "3": (
        "Transistor BJT",
        TransitorBJT,
        {"tipo_transitor": "BJT"},
        [
            ("nomenclatura", "Nomenclatura", str),
            ("tipo_senial", "Tipo de señal (NPN/PNP)", str),
            ("ganancia", "Ganancia (hFE)", float),
            ("volt_saturacion", "Voltaje de saturación", float),
            ("corriente_max", "Corriente máxima", float),
        ],
    ),
    "4": (
        "Transistor MOSFET",
        TransitorMosfet,
        {"tipo_transitor": "MOSFET"},
        [
            ("nomenclatura", "Nomenclatura", str),
            ("resistencia_encendido", "Resistencia de encendido", float),
            ("volt_umbral", "Voltaje umbral", float),
            ("gate_charge", "Gate charge", float),
        ],
    ),
}


TIPOS_PASIVOS = {
    "1": (
        "Resistencia",
        Resistencia,
        {},
        [
            ("ohmios", "Valor", float),
            ("unidad", "Unidad (ohm/kOhm/MOhm)", str),
            ("potencia", "Potencia (W)", float),
            ("tolerancia", "Tolerancia (%)", float),
        ],
    ),
    "2": (
        "Potenciómetro",
        Potenciometro,
        {},
        [
            ("ohmios", "Valor", float),
            ("unidad", "Unidad (ohm/kOhm/MOhm)", str),
            ("potencia", "Potencia (W)", float),
            ("tolerancia", "Tolerancia (%)", float),
            ("pines", "Pines", int),
        ],
    ),
    "3": (
        "Capacitor",
        Capacitor,
        {},
        [
            ("tipo_capacitor", "Tipo (electrolitico/ceramico)", str),
            ("volt_max", "Voltaje máximo (V)", float),
            ("capacitancia", "Capacitancia", float),
            ("unidad", "Unidad (uf/nf/pf)", str),
        ],
    ),
    "4": (
        "Fusible",
        Fusible,
        {},
        [
            ("tipo_fusible", "Tipo", str),
            ("volt_max", "Voltaje máximo (V)", float),
            ("amperaje", "Amperaje (A)", float),
            ("medida", "Medida (mm)", str),
        ],
    ),
    "5": (
        "Transformador",
        Transformador,
        {},
        [
            ("voltaje_entrada", "Voltaje de entrada (V)", float),
            ("voltaje_salida", "Voltaje de salida (V)", float),
            ("amperaje", "Amperaje (A)", float),
        ],
    ),
}

SECCIONES = {
    "1": ("Componentes ACTIVOS", activos, TIPOS_ACTIVOS),
    "2": ("Componentes PASIVOS", pasivos, TIPOS_PASIVOS),
}


# ---------- Utilidades ----------


def pedir(texto, tipo=str):
    while True:
        valor = input(f"{texto}: ").strip()
        if tipo is str:
            if valor:
                return valor
            print("⚠️  No puede estar vacío.")
            continue
        try:
            return tipo(valor)
        except ValueError:
            print("⚠️  Valor inválido, intenta de nuevo.")


def mostrar_logo(titulo="INVENTARIO ELECTRÓNICO"):
    print("=" * 44)
    print(f"⚡ {titulo} ⚡".center(44))
    print("=" * 44)


def elegir_tipo(tipos):
    for clave, (nombre, *_) in tipos.items():
        print(f"  {clave}) {nombre}")
    print("  0) Cancelar")
    return input("Tipo: ").strip()


def descripcion(c):
    return f"{type(c).__name__} {c.clave()[1:]}"


# ---------- Acciones de una sección ----------


def agregar(catalogo, tipos):
    opcion = elegir_tipo(tipos)
    if opcion not in tipos:
        return
    nombre, clase, fijos, campos = tipos[opcion]

    datos = dict(fijos)
    for atributo, pregunta, tipo in campos:
        datos[atributo] = pedir(pregunta, tipo)
    datos["cantidad"] = pedir("Cantidad", int)
    datos["ubicacion"] = input("Ubicación (opcional): ").strip()

    catalogo.agregar(clase(**datos))
    print(f"✅ {nombre} agregado.")


def quitar(catalogo, _tipos):
    items = catalogo.listar()
    if not items:
        print("No hay componentes en esta sección.")
        return

    for i, c in enumerate(items, 1):
        print(f"  {i}) {descripcion(c)}  x{c.cantidad}")
    numero = pedir("Número a quitar (0 cancela)", int)
    if numero == 0 or numero > len(items):
        return

    cantidad = pedir("Cantidad a quitar", int)
    if catalogo.quitar(items[numero - 1].clave(), cantidad):
        print("✅ Listo.")
    else:
        print("❌ No hay suficientes unidades.")


def ver(catalogo, _tipos):
    print("\n--- Por tipo ---")
    for nombre, cant in catalogo.cantidad_por_tipo().items():
        print(f"  {nombre}: {cant}")
    print(f"  TOTAL: {catalogo.cantidad_total()}")

    print("\n--- Detalle ---")
    for c in catalogo.listar():
        print(f"  {descripcion(c)}  x{c.cantidad}  📍{c.ubicacion or '-'}")


# ---------- Menús ----------

ACCIONES = {
    "1": ("Agregar componente", agregar),
    "2": ("Quitar componente", quitar),
    "3": ("Ver cantidades", ver),
}


def menu_seccion(titulo, catalogo, tipos):
    while True:
        print()
        mostrar_logo(titulo)
        for clave, (texto, _) in ACCIONES.items():
            print(f"  {clave}) {texto}")
        print("  0) Volver")

        opcion = input("\nOpción: ").strip()
        if opcion == "0":
            return
        if opcion in ACCIONES:
            ACCIONES[opcion][1](catalogo, tipos)
            input("\nEnter para continuar...")
        else:
            print("⚠️  Opción inválida.")


def menu_principal():
    while True:
        print()
        mostrar_logo()
        for clave, (titulo, _, _) in SECCIONES.items():
            print(f"  {clave}) {titulo}")
        print("  0) Salir")

        opcion = input("\nOpción: ").strip()
        if opcion == "0":
            print("Hasta luego 👋")
            break
        if opcion in SECCIONES:
            titulo, catalogo, tipos = SECCIONES[opcion]
            menu_seccion(titulo, catalogo, tipos)
        else:
            print("⚠️  Opción inválida.")


if __name__ == "__main__":
    menu_principal()
