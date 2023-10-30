# Ejercicio. Numero par

activo = True


while (activo):
    try:
        numero = int(input(f"Digite un número: "))
        if numero != 100:
            if  numero%2 == 0:
                print(f"El número ingresado es par")
            else:
                print(f"El número ingresado es impar")
        else:
            print("Saliendo del ejercicio...")
            activo = False
    except ValueError:
        print("¡Debes ingresar un número entero!")