# Generador de Contraseñas

import random
from GC_Caracteres import Caracteres

print(f"**************************")
print(f" Generador de Contraseñas ")
print(f"**************************")

minusculas = Caracteres.minusculas
mayusculas = Caracteres.mayusculas
numericos = Caracteres.numericos
especiales = Caracteres.especiales

activo = True

def seguir():
    continuar = str(input(f"¿Desea continuar? (s/n): "))
    if continuar == 'n':
        activo = False
        print("Saliendo...")
    else:
        if continuar == 's':
            activo = True
            print(f"continuar")
        else:
            print(f"-¡Error! Debes ingresar una opcón válida")
            seguir()
            activo = True
    return activo


while(activo):
    try:
        minu= int(input(f"Ingrese el número de minúsculas: "))
        mayu= int(input(f"Ingrese el numero de mayusculas: "))
        nume = int(input(f"Ingrese el número de caracteres numéricos: "))
        longitud = int(input(f"Ingrese la longitud de la contraseña: "))
        
        resto = longitud -(minu+mayu+nume)
        
        contrasena = []
        if resto >= 0: 
            for i in range (1,(minu+1)):
                a = random.choice(minusculas)
                contrasena.append(a)

            for i in range (1,(mayu+1)):
                a = random.choice(mayusculas)
                contrasena.append(a)

            for i in range (1,(nume+1)):
                a = random.choice(numericos)
                contrasena.append(a)

            for i in range (1,(resto+1)):
                a = random.choice(especiales)
                contrasena.append(a)
    
            random.shuffle(contrasena)
            print(f"N° de caracteres de su contraseña: " + str(len(contrasena)))
            print(f"Su contraseña es: ")
            print(*contrasena)     
        
            activo = seguir()
            
        else: 
            print("La longitud de la contraseña debe ser mayor o igual al número de caracteres ingresados")
        
    except ValueError:
        print(f"¡Debes ingresar un número entero!")