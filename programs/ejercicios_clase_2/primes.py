n = 53239
primo = True
for i in range(2, int(n ** 0.5)+1):
    if not n % i:
        # Divisible entre i
        print(f"¡{n} no es primo! es divisible entre {i}")
        primo = False
        break
if primo:
    print(f"¡{n} es un número primo!")
