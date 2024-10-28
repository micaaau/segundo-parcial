"""5. Clases y POO
Disena una clase llamada Rectangulo que tenga los siguientes atributos y
metodos:
• Atributos: base, altura.
• Metodos:
area(): Calcula y devuelve el area del rectangulo.
perimetro(): Calcula y devuelve el perimetro del rectangulo."""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return self.base * 2 + self.altura * 2

base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))


rectangulo = Rectangulo(base, altura)
print("Area del rectangulo:", rectangulo.area())
print("Perimetro del rectangulo:", rectangulo.perimetro())