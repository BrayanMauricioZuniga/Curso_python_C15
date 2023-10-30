# Listas Vs Tuplas
# Las listas son estructuras de datos que pueden almacenar cualquier tipo de dato, 
# además la cantidad de elementos de una lista se puede MODIFICAR removiendo o añadiendo elementos.
# Para definir una lista se utilizan los corchetes, dentro de estos se colocan todos 
# los elementos separados por comas. Una tupla es similar a una lista la diferencia principal es que las tuplas 
# no pueden ser modificadas directamente. Para definir una tupla, los elementos se separan con comas 
# y se encierran entre paréntesis.


#Lista

calificaciones = [10,9,8,7.5,9]
nombres = ["Ana","Juan","Sofía","Pablo","Tania"]
mezcla = [True, 10.5, "abc", [0,1,1]]

print(nombres[-2])
print(nombres)
# Se puede añadir o quitar elementos
nombres.append("Pedro")
nombres.append("Mauricio")
print(nombres)
nombres.remove("Tania")
print(nombres)


#Tupla

colores = ("Amarillo","Azul","Rojo")
