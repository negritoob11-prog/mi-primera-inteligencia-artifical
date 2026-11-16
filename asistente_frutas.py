
def identificar_fruta(peso, color):
    if color == "amarillo" and peso >= 100:
        return "Podría ser un banano"

    elif color == "rojo":
        return "Podría ser una manzana"

    elif color == "naranja":
        return "Podría ser una naranja"

    else:
        return "No conozco esa fruta"


# Primera prueba del asistente
print("ASISTENTE DE IDENTIFICACION DE FRUTAS")

resultado = identificar_fruta(150, "rojo")

print("Resultado:", resultado)

print(resultado)

