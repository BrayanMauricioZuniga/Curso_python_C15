# Generador de Contraseñas

import random

print(f"**************************")
print(f" Generador de Contraseñas ")
print(f"**************************")

#minusculas = list()
#mayusculas = list()
#numericos =  list()


minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numericos = [0,1,2,3,4,5,6,7,8,9]
especiales = ['#','$','%','&','¿','?','!','¡','*','+','-','/','~','^']


try:
    minu= int(input(f"Ingrese el número de minúsculas: "))
    mayu= int(input(f"Ingrese el numero de mayusculas: "))
    nume = int(input(f"Ingrese el número de caracteres numéricos: "))
    espe = int(input(f"Ingrese el número de caracteres especiales: "))

    contrasena = []

    for i in range (1,(minu+1)):
        a = random.choice(minusculas)
        contrasena.append(a)

    for i in range (1,(mayu+1)):
        a = random.choice(mayusculas)
        contrasena.append(a)

    for i in range (1,(nume+1)):
        a = random.choice(numericos)
        contrasena.append(a)

    for i in range (1,(espe+1)):
        a = random.choice(especiales)
        contrasena.append(a)
    
    random.shuffle(contrasena)
    print("N° de caracteres de su contraseña: " + str(len(contrasena)))
    print("Su contraseña es: ")
    print(*contrasena)
except ValueError:
    print(f"Debes ingresar un numero entero")