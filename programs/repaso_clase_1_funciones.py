# Como repaso de los conceptos vistos en la primera clase, vamos a hacer un programa de Python 
# sencillito para encontrar números perfectos!

# Un número perfecto satisface que la suma de sus divisores menores que él (i.e. estrictos) es el mismo número:
# e.g. 6 tiene divisores estricftos 1,2,3 y 1+2+3=6

# En primer lugar, vamos a definir un límite de hasta dónde buscar
limit = 10000

# Para almacenar los números, usaremos un diccionario que lleve cada número (key) a una lista de divisores (value) 
numeros_perfectos = {}

# Esta función comprueba si numero es perfecto. Si lo es devuelve True y una lista de divisores. Si no lo es, devuelve False
# y una lista vacía
def check_perfect(numero):
    divisores = []
    suma_divisores = 0
    for divisor in range(1, numero):
        # Comprobamos si es divisor
        if numero % divisor == 0:
            divisores.append(divisor)
            suma_divisores += divisor
    if suma_divisores == numero:
        return True, divisores
    else:
        return False, []

# El programa principal se desarrollará a lo largo de un bucle
for numero in range(2, limit + 1):
    # En primer lugar, queremos una lista con todos los divisores estrictos del número
    es_perfecto, lista_divisores = check_perfect(numero)
    if es_perfecto:
        numeros_perfectos[numero] = lista_divisores
    
    # Opcional: imprimir cuántos llevamos (pero cada vez va más lento el programa debido a que hay más divisores que comprobar)
    # if numero % (limit / 100) == 0:
    #    print("Progreso: ", (100*numero/limit), "%")

# Y ahora imprimimos los resultados
print(f"Hay {len(numeros_perfectos)} números perfectos desde 2 hasta {limit}:")
for numero_perfecto, divisores in numeros_perfectos.items():
    divisores_string = " + ".join(str(d) for d in divisores)
    print(f"{numero_perfecto} = {divisores_string}")

# Algunos facts:
# No se sabe si hay infinitos números perfectos
# Solo se han encontrado 51 de momento, crecen muy rápido!
# Los 10 primeros: https://oeis.org/A000396/list
# Los números 2^(p-1)*(2^p-1) son perfectos, dónde p es un primo tal que 2^p-1 también es primo (i.e. primos de Mersenne, que tampoco
# se sabe si hay infinitos o no), no hay más numeros perfectos pares y se cree que no hay números perfectos impares