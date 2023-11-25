import destinos
import mapa
from asientos import (
    OCUPADO,
    asiento_actualizar,
    asiento_esta_ocupado,
    imprimir_asientos,
    imprimir_asientos_con_encabezado,
    imprimir_pasajero_por_datos,
)
from util import (
    es_respuesta,
    es_si,
    esperar_continuar,
    imprimir_encabezado,
    imprimir_error_esperar,
    limpiar_pantalla,
    tic_entrada,
    tic_entrada_ciclo,
    tic_entrada_numero_ciclo,
    tic_entrada_numero_ciclo_inmediato,
    tic_imprimir,
)


def comando_registro_de_reservaciones(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Registro de Reservaciones")
    imprimir_asientos_con_encabezado(asientos)

    elegido = tic_entrada_numero_ciclo(
        entrada_texto="Elige el asiento a reservar (0 para volver al menú principal): ",
        validador=lambda x: x in range(29),
        en_invalido="Número del asiento inválido.",
    )

    if elegido == 0:
        return

    asiento = mapa.obtener(asientos, elegido)

    if asiento_esta_ocupado(asiento):
        imprimir_error_esperar("Número del asiento está ocupado.")

        respuesta = tic_entrada_ciclo(
            entrada_texto=(
                "¿Se desea continuar con el Registro de Reservaciones, (S/N)? "
            ),
            validador=lambda x: es_respuesta(x),
            en_invalido="Respuesta inválida.",
        )

        if es_si(respuesta):
            return comando_registro_de_reservaciones(asientos)
        return

    def es_alfabetico(s: str):
        for car in s:
            if car.isalpha():
                return True
        return False

    nombre = tic_entrada_ciclo(
        entrada_texto="Ingresar el nombre de la persona para esta reservación: ",
        validador=es_alfabetico,
        en_invalido="Destino del pasajero inválido.",
    )

    identificacion = tic_entrada(
        "Ingresa la identificación del pasajero: ", inmediato=False
    )

    tic_imprimir("Posibles destinos:")
    tic_imprimir("(1) Luna (LUN)")
    tic_imprimir("(2) Europa (EUR)")
    tic_imprimir("(3) Titán (TAN)")

    opcion = tic_entrada_numero_ciclo_inmediato(
        entrada_texto="--- Presiona uno de los números entre paréntesis --- ",
        validador=lambda x: x in range(1, 4),
        en_invalido="Destino del pasajero inválido.",
    )

    if opcion == 1:
        destino = destinos.LUN
    elif opcion == 2:
        destino = destinos.EUR
    else:
        destino = destinos.TAN

    imprimir_pasajero_por_datos(
        asiento,
        nombre_pasajero=nombre,
        identificacion_pasajero=identificacion,
        destino_codigo=destino,
    )

    # TODO: transformador que sanitiza el input
    confirmar = tic_entrada_ciclo(
        entrada_texto="¿Se confirma el registro de la reservación, (S/N)? ",
        validador=lambda x: es_respuesta(x),
        en_invalido="Respuesta inválida.",
    )

    if es_si(confirmar):
        asiento_actualizar(
            asiento,
            estado=OCUPADO,
            destino_codigo=destino,
            pasajero=mapa.nuevo(("nombre", nombre), ("id", identificacion)),
        )

    continuar = tic_entrada_ciclo(
        entrada_texto="¿Se desea continuar con el Registro de Reservaciones, (S/N)? ",
        validador=lambda x: es_respuesta(x),
        en_invalido="Respuesta inválida.",
    )

    if es_si(continuar):
        return comando_registro_de_reservaciones(asientos)


def comando_eliminacion_de_reservaciones(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Eliminación de Reservaciones")
    imprimir_asientos(asientos)
    esperar_continuar()


def comando_mapa_de_ocupacion(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Mapa de Ocupación")
    imprimir_asientos(asientos)
    esperar_continuar()
