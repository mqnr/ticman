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
    tic_imprimir(f"• Identificación del pasajero: {op('identificacion')}")
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
