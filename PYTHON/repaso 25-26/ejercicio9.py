lista = []
ent = int(input("ingrese un numero entero: "))
while ent != -0:
    lista.append(ent)
    ent = int(input("ingrese un numero entero: "))
print("la media de esta lista es",sum(lista)/len(lista))