# Las variable globales en python se declaran fuera de cualquier función o bloque de código
# y pueden ser accedidas o modificadas desde cualquier parte del programa, a diferencia de
# las variables locales que solo pueden ser accedidas desde la funcion que son creadas 

global x
x = 10

def mi_funcion():
    print("El valor de x es:", x)

mi_funcion()