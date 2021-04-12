import geoanalytic

x1 = int(input("Ingrese el valor x del primer punto (x1): "))
y1 = int(input("Ingrese el valor y del primer punto (y1): "))
x2 = int(input("\nIngrese el valor x del segundo punto (x2): "))
y2 = int(input("Ingrese el valor y del segundo punto (y2): "))

dst = geoanalytic.distancia(x1, y1, x2, y2)
pnd = geoanalytic.pendiente(x1, y1, x2, y2)

pntA = [x1, y1]
pntB = [x2, y2]

print(f"\nPuntos: A = {pntA}, B = {pntB}")

print(f"Distancia: {dst}")
print(f"Pendiente: {pnd}")
