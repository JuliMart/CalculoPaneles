def calcular_paneles_triangulo(base, altura, ancho_panel, largo_panel):
    def calcular_paneles(ancho_panel, largo_panel):
        paneles_validos = []
        y = 0
        while y + largo_panel <= altura:
            ancho_disponible = base * (1 - (y / altura))
            inicio_x = (base - ancho_disponible) / 2
            paneles_en_fila = int(ancho_disponible // ancho_panel)
            for i in range(paneles_en_fila):
                x = inicio_x + i * ancho_panel
                if x + ancho_panel <= inicio_x + ancho_disponible:
                    paneles_validos.append((x, y, ancho_panel, largo_panel))
            y += largo_panel
        return paneles_validos

    # Calcular para orientación horizontal
    paneles_horizontales = calcular_paneles(ancho_panel, largo_panel)

    # Calcular para orientación vertical
    paneles_verticales = calcular_paneles(largo_panel, ancho_panel)

    # Elegir opción más conveniente
    if len(paneles_horizontales) > len(paneles_verticales):
        return paneles_horizontales
    else:
        return paneles_verticales


base = int(input("Ingresa la base del triángulo: "))
altura = int(input("Ingresa la altura del triángulo: "))
ancho_panel = int(input("Ingresa el ancho del panel: "))
largo_panel = int(input("Ingresa el largo del panel: "))

paneles_validos = calcular_paneles_triangulo(
    base, altura, ancho_panel, largo_panel)
print(f"Se muestran {len(paneles_validos)} paneles dentro del triángulo.")
