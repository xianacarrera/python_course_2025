def dividir(a, b):
    try:
        res = a / b
        print(res)
    except:
        print("Error. b no puede ser 0")

dividir(3, 0)

dividir(3, 1)