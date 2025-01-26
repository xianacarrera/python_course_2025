menu = "Introduce una opción:\n"
menu += "\t a. Buscar en la base de datos.\n"
menu += "\t b. Añadir entrada a la base de datos.\n"
menu += "\t c. Salir.\n"

msg = ""
while (msg != "c"):
    msg = input(menu).lower()

    if msg == "a": buscar()
    elif msg == "b": añadir()
    elif msg == "c": print("¡Adiós!")
    else: print("Opción incorrecta.")