ent = str(input("Ingrese una cadena de texto y le diré cuantas vocales tiene: "))
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
contador = 0
for caracter in ent:
    if caracter in vocales:
        contador += 1
print("La cadena tiene ",contador," vocales.")