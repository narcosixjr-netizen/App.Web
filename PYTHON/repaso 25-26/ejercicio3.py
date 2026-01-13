contador = 0
num = int(input("Ingrese un número entero y le diré si es primo: "))
for i in range(2, num):
    if (num%i==0):
        contador = contador +1
if (contador>0):
        print("el numero no es primo")
else:
        print("el numero es primo")
