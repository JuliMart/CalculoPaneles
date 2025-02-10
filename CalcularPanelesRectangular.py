def calcularPaneles(ancho_techo, largo_techo, ancho_panel, largo_panel):

    # Cálculo de número de paneles en cada orientación
    paneles_horizontales = (ancho_techo // ancho_panel) * \
        (largo_techo // largo_panel)
    paneles_verticales = (ancho_techo // largo_panel) * \
        (largo_techo // ancho_panel)

    return max(paneles_horizontales, paneles_verticales)


# Inputs de usuario
ancho_techo = int(input("Ingrese el ancho del techo: "))
largo_techo = int(input("Ingrese el largo del techo: "))
ancho_panel = int(input("Ingrese el ancho del panel: "))
largo_panel = int(input("Ingrese el largo del panel: "))

# Calcular y mostrar el resultado
total_paneles = calcularPaneles(
    ancho_techo, largo_techo, ancho_panel, largo_panel)

print(f"La cantidad máxima de paneles es: {total_paneles}")
