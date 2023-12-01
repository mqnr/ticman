import destinos
import mapa
from asientos import (
    OCUPADO,
    asiento_actualizar,
    asiento_desocupar,
    asiento_esta_ocupado,
    imprimir_asientos,
    imprimir_asientos_con_encabezado,
    imprimir_pasajero_por_asiento,
    imprimir_pasajero_por_datos,
)
from util import (
    es_alfabetico,
    esperar_continuar,
    imprimir_encabezado,
    imprimir_error_esperar,
    imprimir_esperar,
    limpiar_pantalla,
    pedir_asiento,
    pedir_respuesta,
    tic_entrada,
    tic_entrada_ciclo,
    tic_entrada_numero_ciclo_inmediato,
    tic_imprimir,
)


def comando_registro_de_reservaciones(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Registro de Reservaciones")
    imprimir_asientos_con_encabezado(asientos)

    elegido = pedir_asiento(
        "Elige el asiento a reservar (0 para volver al menú principal): "
    )

    if elegido == 0:
        return

    asiento = mapa.obtener(asientos, elegido)

    if asiento_esta_ocupado(asiento):
        imprimir_error_esperar("Número del asiento está ocupado.")

        if pedir_respuesta(
            "¿Se desea continuar con el Registro de Reservaciones, (S/N)? "
        ):
            return comando_registro_de_reservaciones(asientos)
        return

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

    if pedir_respuesta("¿Se confirma el registro de la reservación, (S/N)? "):
        asiento_actualizar(
            asiento,
            estado=OCUPADO,
            destino_codigo=destino,
            pasajero=mapa.nuevo(("nombre", nombre), ("id", identificacion)),
        )

    if pedir_respuesta("¿Se desea continuar con el Registro de Reservaciones, (S/N)? "):
        return comando_registro_de_reservaciones(asientos)


def comando_eliminacion_de_reservaciones(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Eliminación de Reservaciones")
    imprimir_asientos(asientos)

    elegido = pedir_asiento("Elige el asiento para el cual eliminar la reservación: ")
    if elegido == 0:
        return

    asiento = mapa.obtener(asientos, elegido)
    if not asiento_esta_ocupado(asiento):
        imprimir_esperar("Número del asiento no está ocupado.")

        if pedir_respuesta(
            "¿Se desea continuar con la Eliminación de Reservaciones, (S/N)? "
        ):
            return comando_eliminacion_de_reservaciones(asientos)
        return

    imprimir_pasajero_por_asiento(asiento)

    if pedir_respuesta("¿Se confirma la eliminación de la reservación, (S/N)? "):
        asiento_desocupar(asiento)

    if pedir_respuesta(
        "¿Se desea continuar con la Eliminación de Reservaciones, (S/N)? "
    ):
        return comando_eliminacion_de_reservaciones(asiento)


def comando_modificacion_de_reservaciones(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Modificación de Reservaciones")
    imprimir_asientos(asientos)

    elegido = pedir_asiento(
        "Elige el asiento a modificar (0 para volver al menú principal): "
    )
    if elegido == 0:
        return

    asiento = mapa.obtener(asientos, elegido)
    if not asiento_esta_ocupado(asiento):
        imprimir_error_esperar("Número del asiento no está ocupado.")

        if pedir_respuesta(
            "¿Se desea continuar con la Modificación de Reservaciones, (S/N)? "
        ):
            return comando_eliminacion_de_reservaciones(asientos)
        return

    imprimir_pasajero_por_asiento(asiento)

    if not pedir_respuesta("¿Se confirma el ingreso de los datos a modificar, (S/N)? "):
        if pedir_respuesta(
            "¿Se desea continuar con la Modificación de Reservaciones, (S/N)? "
        ):
            return comando_modificacion_de_reservaciones(asientos)
        return

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

    if pedir_respuesta("¿Se confirma la modificación de la reservación, (S/N)? "):
        asiento_actualizar(
            asiento,
            estado=OCUPADO,
            destino_codigo=destino,
            pasajero=mapa.nuevo(("nombre", nombre), ("id", identificacion)),
        )

    if pedir_respuesta(
        "¿Se desea continuar con la Modificación de Reservaciones, (S/N)? "
    ):
        return comando_modificacion_de_reservaciones(asientos)


def comando_mapa_de_ocupacion(asientos):
    limpiar_pantalla()
    imprimir_encabezado("Mapa de Ocupación")
    imprimir_asientos(asientos)
    esperar_continuar()
