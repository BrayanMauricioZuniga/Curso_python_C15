# Ejercicio. Numero par

ejercicioActivo = True


while (ejercicioActivo):
    numero = int(input(f"Digite un número: "))
    try:    
        if numero != 100:
            if  numero%2 == 0:
                print(f"El número ingresado es par")
            else:
                print(f"El número ingresado es impar")
        else:
            print("Saliendo del ejercicio...")
            ejercicioActivo = False
    except ValueError:
        print("`numero` Debes ser un número entero")