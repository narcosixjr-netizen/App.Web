suma = 0
ent = 1
while ent != 0:
    ent =int(input("Ingrese un número entero positivo: "))
    if ent % 2 == 0:
        suma = suma + ent
print("la suma total de los pares es ",suma)