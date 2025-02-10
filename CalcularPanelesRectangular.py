def calcularPaneles(ancho_techo, largo_techo, ancho_panel, largo_panel):

    # Cálculo de número de paneles en cada orientación
    paneles_horizontales = (ancho_techo // ancho_panel) * \
        (largo_techo // largo_panel)
    paneles_verticales = (ancho_techo // largo_panel) * \
        (largo_techo // ancho_panel)

    # Verificando si queda espacio para poner paneles en la orientación opuesta
    sobrante_ancho_horiz = ancho_techo % ancho_panel

    # Espacio libre al colocar paneles verticalmente
    sobrante_ancho_vert = ancho_techo % largo_panel

    extra_paneles_horiz = (sobrante_ancho_horiz //
                           largo_panel) * (largo_techo // ancho_panel)
    extra_paneles_vert = (sobrante_ancho_vert //
                          ancho_panel) * (largo_techo // largo_panel)

    # Adicionar paneles si es que se puede
    total_horiz = paneles_horizontales + extra_paneles_horiz
    total_vert = paneles_verticales + extra_paneles_vert

    return max(total_horiz, total_vert)


# Inputs de usuario
ancho_techo = int(input("Ingrese el ancho del techo: "))
largo_techo = int(input("Ingrese el largo del techo: "))
ancho_panel = int(input("Ingrese el ancho del panel: "))
largo_panel = int(input("Ingrese el largo del panel: "))

# Calcular y mostrar el resultado
total_paneles = calcularPaneles(
    ancho_techo, largo_techo, ancho_panel, largo_panel)

print(f"La cantidad máxima de paneles es: {total_paneles}")
