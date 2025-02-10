def calcular_paneles(base, altura, ancho, largo):
    paneles = []
    y = 0
    while y + largo <= altura:
        ancho_disponible = base * (1 - (y / altura))
        inicio_x = (base - ancho_disponible) / 2
        for i in range(int(ancho_disponible // ancho)):
            x = inicio_x + i * ancho
            paneles.append((x, y, ancho, largo))
        y += largo
    return paneles


def calcular_paneles_triangulo(base, altura, ancho_panel, largo_panel):
    return max(
        [calcular_paneles(base, altura, ancho_panel, largo_panel),
         calcular_paneles(base, altura, largo_panel, ancho_panel)],
        key=len
    )


# Entrada del usuario
base = int(input("Ingresa la base del triángulo: "))
altura = int(input("Ingresa la altura del triángulo: "))
ancho_panel = int(input("Ingresa el ancho del panel: "))
largo_panel = int(input("Ingresa el largo del panel: "))

# Cálculo y salida
paneles_validos = calcular_paneles_triangulo(
    base, altura, ancho_panel, largo_panel)
print(f"Se muestran {len(paneles_validos)} paneles dentro del triángulo.")
