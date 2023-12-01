import comandos
import mapa
from asientos import asiento_vacio
from util import imprimir_error_esperar, tic_entrada, limpiar_pantalla


def menu_principal():
    asientos = mapa.nuevo()
    for i in range(1, 29):
        mapa.actualizar(asientos, (i, asiento_vacio(i)))

    while True:
        limpiar_pantalla()
        print("Elegir una de las siguientes opciones:")
        print("(1) Registro de Reservaciones")
        print("(2) Eliminación de Reservaciones")
        print("(3) Modificación de Reservaciones")
        print("(4) Submenú Consulta de Reservaciones")
        print("(5) Mapa de Ocupación")
        print("(6) Reporte de Reservaciones")
        print("(7) Terminar")

        opcion = tic_entrada("--- Presionar una de las teclas entre paréntesis --- ")

        if opcion == "1":
            comandos.comando_registro_de_reservaciones(asientos)
            pass
        elif opcion == "2":
            comandos.comando_eliminacion_de_reservaciones(asientos)
            pass
        elif opcion == "3":
            comandos.comando_modificacion_de_reservaciones(asientos)
            pass
        elif opcion == "4":
            comandos.comando_submenu_consulta_de_reservaciones(asientos)
        elif opcion == "5":
            comandos.comando_mapa_de_ocupacion(asientos)
        elif opcion == "6":
            comandos.comando_reporte_de_reservaciones(asientos)
        elif opcion == "7":
            break
        else:
            imprimir_error_esperar("Opción invalida.")


menu_principal()
