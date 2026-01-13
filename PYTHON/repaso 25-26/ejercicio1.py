num = int(input("dame un numero entero y te diré su factorial: "))
val = 1
for i in range(1, num + 1):
    val *= i
print(val)