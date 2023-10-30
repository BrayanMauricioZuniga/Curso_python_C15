# Las excepciones son estructuras que nos permiten manejar los errores en el código

while True:
    try:
        edad = int(input(f"Digite su edad en años: "))
        #break
    except ValueError:
        print(f"Error : ¡Debes ingresar un número!")
    if edad >= 18:
        print(f"Eres adulto")
    else:
        print(f"Aún no eres adulto")
