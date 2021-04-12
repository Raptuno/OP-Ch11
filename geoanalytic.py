import math

"""
Fórmula distancia entre dos puntos: d=sqrt((x_2-x_1)^2+(y_2-y_1)^2))
"""


def distancia(x1, y1, x2, y2):
    return math.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))


"""
Fórmula pendiente: y=mx+b
Fórmula general pendiente: m=(y2-y1)/(x2-x1)
"""


def pendiente(x1, y1, x2, y2):
    try:
        return (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return "Error: División entre cero"
