res = 1
base = int(input("dame un numero entero: "))
exponente = int(input("dame un numero entero al que exponer el anterior: "))
for i in range(1, exponente+1):
    res = res * base
print(res)