from cargar import cargar_archivos
import color
import comandos
import mapa
import sys
from asientos import asiento_vacio
from util import imprimir_error_esperar, tic_entrada, limpiar_pantalla


def menu_principal():
    primero = True

    asientos_cargados, errores_archivos, errores_asientos = cargar_archivos(
        sys.argv[1:]
    )

    asientos = mapa.nuevo()
    cargados = 0
    for i in range(1, 29):
        cargado = mapa.obtener(asientos_cargados, i)
        if cargado is None:
            mapa.actualizar(asientos, (i, asiento_vacio(i)))
        else:
            mapa.actualizar(asientos, (i, cargado))
            cargados += 1

    while True:
        limpiar_pantalla()
        if primero:
            if "--cargar" in sys.argv:
                if len(errores_archivos) > 0:
                    print(
                        f"{color.ERROR}ERROR: No se pudieron cargar los siguientes archivos (¿existen?){color.FIN}"
                    )
                    for archivo in errores_archivos:
                        print(f"    - {color.NEGRITAS}{archivo}{color.FIN}")
                if len(errores_asientos) > 0:
                    print(
                        f"{color.ERROR}ERROR: Los siguientes archivos tuvieron entradas mal formadas [nombre del archivo seguido por los índices de entradas]:{color.FIN}"
                    )
                    for nombre, entradas_fallidas in errores_asientos:
                        print(
                            f"    - {color.NEGRITAS}{nombre}{color.FIN}: {', '.join(str(n) for n in entradas_fallidas)}"
                        )
            plural = "s" if cargados != 1 else ""
            if cargados > 0:
                print(
                    f"{color.OKVERDE}✓ Cargado{plural} {color.NEGRITAS}{cargados}{color.FIN}{color.OKVERDE} asiento{plural} de archivos{color.FIN}"
                )
            primero = False

        print(f"({color.CABECERA}1{color.FIN}) Registro de Reservaciones")
        print(f"({color.CABECERA}2{color.FIN}) Eliminación de Reservaciones")
        print(f"({color.CABECERA}3{color.FIN}) Modificación de Reservaciones")
        print(f"({color.CABECERA}4{color.FIN}) Submenú Consulta de Reservaciones")
        print(f"({color.CABECERA}5{color.FIN}) Mapa de Ocupación")
        print(f"({color.CABECERA}6{color.FIN}) Reporte de Reservaciones")
        print(f"({color.CABECERA}7{color.FIN}) Terminar")

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
