# El bucle for se utiliza para hacer sentencia repetitivas.
# El ingreso de datos desde el usuario a python se realiza mediante input
# La impresión de texto se realiza mediante print

cont = 0
numero = int(input(f"Digite un número: "))

for i in range (1,(numero+1)):
    res = numero%i
    if res == 0:
        cont=cont+1
if cont == 2:
    print(str(numero)+(" es un número primo"))