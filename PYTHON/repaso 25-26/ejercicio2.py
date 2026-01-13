def contar_positivos(lista):
    contador = 0
    for i in lista:
        if i > 0:
            contador += 1
    return contador

lista = [10, -5, 3, 0, -2, 8, -1]

print("Cantidad de números positivos en la lista:", contar_positivos(lista))


