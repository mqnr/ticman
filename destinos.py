TIC = "TIC"
LUN = "LUN"
EUR = "EUR"
TAN = "TAN"


def codigo_a_largo(codigo):
    if codigo == "TIC":
        return "Sin destino"
    if codigo == "LUN":
        return "Luna"
    if codigo == "EUR":
        return "Europa"
    if codigo == "TAN":
        return "Titán"
    return ""


def largo_a_codigo(codigo):
    if codigo == "Sin destino":
        return "TIC"
    if codigo == "Luna":
        return "LUN"
    if codigo == "Europa":
        return "EUR"
    if codigo == "Titán":
        return "TAN"
    return ""
