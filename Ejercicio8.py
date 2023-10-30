# Clases en python
# Una clase en Python es una estructura de programación que permite definir 
# un conjunto de métodos y atributos que describen un objeto o entidad. 
# Las clases son un concepto fundamental en la programación orientada a objetos, 
# que se utilizan para modelar entidades del mundo real o abstracto en un programa de computadora.

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)