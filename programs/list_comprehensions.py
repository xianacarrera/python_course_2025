impares1 = []
for n in range(1, 10, 2):
    impares1.append(n)
print(impares1)

impares2 = [n for n in range(1, 10, 2)]
print(impares2)

impares3 = [n for n in range(1, 10) if n % 2 == 1]
print(impares3)

uni = "compostela"

letras = []
for letra in uni:
    if letra != "c":
        letras.append(letra)
print(letras)

letras2 = [letra for letra in uni if letra != "c"]
print(letras2)