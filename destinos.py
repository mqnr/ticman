TIC = "TIC"
LUN = "LUN"
EUR = "EUR"
TAN = "TAN"


def codigo_a_largo(codigo):
    if codigo == TIC:
        return "Sin destino"
    if codigo == LUN:
        return "Luna"
    if codigo == EUR:
        return "Europa"
    if codigo == TAN:
        return "Titán"
    return ""


def largo_a_codigo(largo):
    if largo == "Sin destino":
        return TIC
    if largo == "Luna":
        return LUN
    if largo == "Europa":
        return EUR
    if largo == "Titán":
        return TAN
    return ""
