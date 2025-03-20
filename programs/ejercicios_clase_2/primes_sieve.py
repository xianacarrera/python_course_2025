# Todos los números desde 0 hasta 10001
lista_original = [i for i in range(0, 10002)]

# Sieve of Eratosthenes, ponemos un 0 en los números no primos
lista_original[1] = 0
for i in range(2, 102):
    if lista_original[i] != 0:
        # Se puede empezar a descartar en i*i, ya que los factores más pequeños que i ya están quitados
        # De todas formas, el código se puede entender mejor si empiezas en 2*i
        for j in range(i * i, 10002, i):
            lista_original[j] = 0

# Sacamos todos los números de la lista que no son 0
primos = [num for num in lista_original if num != 0]
print(primos)
    