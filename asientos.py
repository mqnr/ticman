import mapa
import destinos
from util import tic_imprimir

OCUPADO = "ocupado"
DESOCUPADO = "desocupado"

EJECUTIVO = "Ejecutiva"
ECONOMICO = "Económica"

TARIFAS = mapa.nuevo(
    (
        EJECUTIVO,
        mapa.nuevo(
            (destinos.LUN, 3_000.00),
            (destinos.EUR, 5_250.00),
            (destinos.TAN, 10_500.00),
        ),
    ),
    (
        ECONOMICO,
        mapa.nuevo(
            (destinos.LUN, 2_000.00), (destinos.EUR, 3_500.00), (destinos.TAN, 7_000.00)
        ),
    ),
)

VENTANA = "Ventana"
CENTRO = "Centro"
PASILLO = "Pasillo"


def asiento_vacio(n):
    ubicacion = ""
    if n in range(1, 5):
        clase = EJECUTIVO
        m = n % 4
        if m in (1, 0):
            ubicacion = VENTANA
        else:
            ubicacion = PASILLO
    else:
        clase = ECONOMICO
        m = (n - 4) % 6
        if m in (1, 0):
            ubicacion = VENTANA
        elif m in (2, 5):
            ubicacion = CENTRO
        else:
            ubicacion = PASILLO

    return mapa.nuevo(
        ("numero", n),
        ("ubicacion", ubicacion),
        ("clase", clase),
        ("estado", "desocupado"),
        ("destino_codigo", destinos.TIC),
        ("destino_largo", destinos.codigo_a_largo(destinos.TIC)),
        ("costo", -1),
        ("pasajero", None),
    )


def asiento_esta_ocupado(asiento):
    return mapa.obtener(asiento, "estado") == OCUPADO


def calcular_tarifa(clase, destino):
    costos = mapa.obtener(TARIFAS, clase)
    return mapa.obtener(costos, destino)


def asiento_actualizar(asiento, estado=None, destino_codigo=None, pasajero=object()):
    _sin_valor = object()

    destino_cambiado = False
    if estado in (OCUPADO, DESOCUPADO):
        mapa.actualizar(asiento, ("estado", estado))
    if destino_codigo in (destinos.TIC, destinos.LUN, destinos.EUR, destinos.TAN):
        destino_cambiado = True
        mapa.actualizar(asiento, ("destino_codigo", destino_codigo))
        mapa.actualizar(
            asiento, ("destino_largo", destinos.codigo_a_largo(destino_codigo))
        )
    if pasajero is not _sin_valor:
        mapa.actualizar(asiento, ("pasajero", pasajero))

    if destino_cambiado:
        if destino_codigo == destinos.TIC:
            mapa.actualizar(asiento, ("costo", -1))
            return

        clase = mapa.obtener(asiento, "clase")
        mapa.actualizar(asiento, ("costo", calcular_tarifa(clase, destino_codigo)))


def asiento_desocupar(asiento):
    asiento_actualizar(
        asiento, estado=DESOCUPADO, destino_codigo=destinos.TIC, pasajero=None
    )


def imprimir_pasajero_por_datos(
    asiento, nombre_pasajero, identificacion_pasajero, destino_codigo
):
    tic_imprimir(f"• Nombre del pasajero: {nombre_pasajero}")
    tic_imprimir(f"• Identificación del pasajero: {identificacion_pasajero}")
    tic_imprimir(f"• Destino del pasajero: {destinos.codigo_a_largo(destino_codigo)}")
    tic_imprimir(f"• Clase del asiento: {mapa.obtener(asiento, 'clase')}")
    tic_imprimir(f"• Ubicación del asiento: {mapa.obtener(asiento, 'ubicacion')}")
    tic_imprimir(f"• Número del asiento: {mapa.obtener(asiento, 'numero')}")
    costo = calcular_tarifa(mapa.obtener(asiento, "clase"), destino_codigo)
    tic_imprimir(f"• Costo del boleto del pasajero: ${costo:,.2f}")


def imprimir_pasajero_por_asiento(asiento):
    pasajero = mapa.obtener(asiento, "pasajero")

    def op(s):
        return mapa.obtener(pasajero, s)

    def oa(s):
        return mapa.obtener(asiento, s)

    tic_imprimir(f"• Nombre del pasajero: {op('nombre')}")
    tic_imprimir(f"• Identificación del pasajero: {op('id')}")
    tic_imprimir(f"• Destino del pasajero: {oa('destino_largo')}")
    tic_imprimir(f"• Clase del asiento: {oa('clase')}")
    tic_imprimir(f"• Ubicación del asiento: {oa('ubicacion')}")
    tic_imprimir(f"• Número del asiento: {oa('numero')}")
    tic_imprimir(f"• Costo del boleto del pasajero: ${oa('costo'):,.2f}")


def imprimir_asientos(asientos):
    def f(asiento):
        return (
            f" {str(mapa.obtener(asiento, 'numero')).rjust(2)}"
            f" {mapa.obtener(asiento, 'destino_codigo')} "
        )

    def o(n):
        return mapa.obtener(asientos, n)

    def fo(n):
        return f(o(n))

    tic_imprimir("[9]┌────────┬────────┐[3]┌────────┬────────┐")
    tic_imprimir(f"[9]│{fo(1)}│{fo(2)}│[3]│{fo(3)}│{fo(4)}│")
    tic_imprimir("[9]└────────┴────────┘[3]└────────┴────────┘")
    tic_imprimir("┌────────┬────────┬────────┐[3]┌────────┬────────┬────────┐")
    tic_imprimir(f"│{fo(5)}│{fo(6)}│{fo(7)}│[3]│{fo(8)}│{fo(9)}│{fo(10)}│")
    tic_imprimir("├────────┼────────┼────────┤[3]├────────┼────────┼────────┤")
    tic_imprimir(f"│{fo(11)}│{fo(12)}│{fo(13)}│[3]│{fo(14)}│{fo(15)}│{fo(16)}│")
    tic_imprimir("├────────┼────────┼────────┤[3]├────────┼────────┼────────┤")
    tic_imprimir(f"│{fo(17)}│{fo(18)}│{fo(19)}│[3]│{fo(20)}│{fo(21)}│{fo(22)}│")
    tic_imprimir("├────────┼────────┼────────┤[3]├────────┼────────┼────────┤")
    tic_imprimir(f"│{fo(23)}│{fo(24)}│{fo(25)}│[3]│{fo(26)}│{fo(27)}│{fo(28)}│")
    tic_imprimir("└────────┴────────┴────────┘[3]└────────┴────────┴────────┘")


def imprimir_asientos_con_encabezado(asientos):
    tic_imprimir("Mapa de Ocupación:")
    imprimir_asientos(asientos)


def imprimir_asientos_lista(asientos):
    nombre_predeterminado = "*** Disponible ***"
    max_nombre = nombre_predeterminado

    max_identificacion = "Identificación"

    max_destino = "Destino"

    lgt_ubicacion = 11  # longitud de la cadena "del Asiento"

    lgt_clase = 9  # longitud de la cadena "Clase del"

    max_costo = "del Boleto"

    for _, asiento in asientos:
        pasajero = mapa.obtener(asiento, "pasajero")
        if pasajero is None:
            continue

        nombre = mapa.obtener(pasajero, "nombre")
        if nombre is not None:
            if len(nombre) > len(max_nombre):
                max_nombre = nombre

        identificacion = mapa.obtener(pasajero, "id")
        if identificacion is not None:
            if len(identificacion) > len(max_identificacion):
                max_identificacion = identificacion

        destino = mapa.obtener(asiento, "destino_largo")
        if destino is not None:
            if len(destino) > len(max_destino):
                max_destino = destino

        costo = mapa.obtener(asiento, "costo")
        if costo is not None and costo != -1:
            costo_cad = f"{costo:,.2f}"
            if len(costo_cad) > len(max_costo):
                max_costo = costo_cad

    # tic_imprimir("Transportes Intergalácticos de Cajeme, S.A.\n")
    # tic_imprimir("Reporte de reservaciones")
    # tic_imprimir(
    #     "────────────────────────────────────────────────────────────────────────────────"
    # )
    # tic_imprimir(
    #     "No. del[10]Nombre[10]Identificación[10]Destino[10]Clase del[10]Ubicación[10]Costo"
    # )
    nodel = len("No. del")
    lgt_mn = len(max_nombre)
    lgt_mi = len(max_identificacion)
    lgt_d = len(max_destino)
    lgt_c = len(max_costo)
    encabezado = f"{'No. del':^{nodel}} {'':^{lgt_mn}} {'':^{lgt_mi}} {'':^{lgt_d}} {'Clase del':^{lgt_clase}} {'Ubicación':^{lgt_ubicacion}} {'Costo':^{lgt_c}}"
    lgt_encabezado = len(encabezado)

    tic_imprimir(f"{'Transportes Intergalácticos de Cajeme, S.A.':^{lgt_encabezado}}\n")
    tic_imprimir(f"{'Reporte de Reservaciones':^{lgt_encabezado}}")
    tic_imprimir("─" * len(encabezado))
    tic_imprimir(encabezado)
    tic_imprimir(
        f"{'Asiento':^{nodel}} {'Nombre':^{lgt_mn}} {'Identificación':^{lgt_mi}} {'Destino':^{lgt_d}} {'Asiento':^{lgt_clase}} {'del Asiento':^{lgt_ubicacion}} {'del Boleto':^{lgt_c}}"
    )
    tic_imprimir("─" * len(encabezado))
    for n, asiento in asientos:
        pasajero = mapa.obtener(asiento, "pasajero")

        def op(s):
            if pasajero is None:
                if s == "nombre":
                    return "*** Disponible ***"
                return ""

            dev = mapa.obtener(pasajero, s)
            if dev is None:
                return ""
            return dev

        def oa(s):
            return mapa.obtener(asiento, s)

        def i(s):
            print(s, end=" ")

        i(f"{n:^{nodel}}")
        i(f"{op('nombre'):<{lgt_mn}}")
        i(f"{op('id'):<{lgt_mi}}")
        destino = oa("destino_largo")
        d = destino if oa("destino_codigo") != destinos.TIC else ""
        i(f"{d:^{lgt_d}}")
        i(f"{oa('clase'):^{lgt_clase}}")
        i(f"{oa('ubicacion'):^{lgt_ubicacion}}")
        costo = mapa.obtener(asiento, "costo")
        cc = f"{costo:,.2f}" if costo is not None and costo != -1 else ""
        i(f"{cc:>{lgt_c}}")

        print()
