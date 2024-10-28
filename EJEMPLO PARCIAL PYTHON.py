"""
1. Listas y Condicionales
Dada una lista de numeros enteros, escribe una funci´on llamada 
filtrar y modificar que:
• Elimine los numeros impares.
• Devuelva una lista donde los numeros restantes se dividan entre 2 si son
mayores a 10, o se multipliquen por 2 si son menores o iguales a 10.
Ejemplo de entrada: [3, 14, 6, 12, 7, 18]
Ejemplo de salida: [7, 3, 6]


def filtrar_y_modificar (lista):
    resultado = []

    for num in lista:
        if num % 2 == 0: #pares
            if num > 10:
                resultado.append(num // 2)
            else:
                resultado.append(num * 2)
    
    return resultado

entrada = [3, 14, 6, 12, 7, 18]
salida = filtrar_y_modificar(entrada)
print(salida)

2. Ciclos anidados y Diccionarios
Escribe una funcion llamada generar matriz que:
• Reciba dos numeros enteros n y m (numero de filas y columnas).
• Devuelva un diccionario donde las claves sean las coordenadas (i, j) 
y los valores sean numeros enteros consecutivos, comenzando en 1.
Ejemplo de entrada: n = 3, m = 2
Ejemplo de salida: {(0,0): 1, (0,1): 2, (1,0): 3, (1,1): 4, (2,0):
5, (2,1): 6}

def generar_matriz (n, m):
    matriz = {}
    contador = 1

    for i in range(n):
        for j in range(m):
            matriz[(i, j)] = contador
            contador += 1

    return matriz

n = 3
m = 2
resultado = generar_matriz(n, m)
print(resultado)

3. Conjuntos
Crea una funcion llamada comparar sets que reciba dos listas de numeros 
enteros. Convierte ambas listas en conjuntos y realiza lo siguiente:
• Devuelve el conjunto que contiene los elementos comunes entre las dos
listas.
• Luego, devuelve el conjunto resultante de la diferencia simetrica 
entre los dos conjuntos.
• Ambos resultados deben ser devueltos como una tupla de conjuntos
Ejemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
Ejemplo de salida: ({3, 4}, {1, 2, 5, 6})


def comprar_sets (lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    interseccion = conjunto1 & conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    return interseccion, diferencia_simetrica

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
resultado = comprar_sets(lista1, lista2)
print(resultado)

4. Decoradores con multiples funciones
Escribe un decorador llamado multiplicar resultado que reciba un numero
como parametro. Este decorador debe aplicarse a dos funciones:
• Una funcion suma(a, b) que sume dos numeros.
• Una funcion resta(a, b) que reste dos numeros.
El decorador debe multiplicar el resultado de ambas funciones por el 
valor proporcionado al decorador. Implementa el decorador y aplica las 
dos funciones.
Ejemplo de uso:
@multiplicar_resultado(3)
def suma(a, b):
return a + b
@multiplicar_resultado(2)
def resta(a, b):
return a - b
Si se llama a suma(2, 3), el resultado deberia ser 15, ya que el 
decorador multiplica el resultado original 5 por 3.

def multiplicar_resultado(multiplicador):
    def decorador(func):
        def envoltura(a, b):
            return func(a, b) * multiplicador
        return envoltura
    return decorador

@multiplicar_resultado(3)
def suma (a, b):
    return a + b

@multiplicar_resultado(2)
def resta (a, b):
    return a - b    

resultado_suma = suma(2, 3)
resultado_resta = resta(5, 3)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)

5. Clases y POO
Disena una clase llamada Rectangulo que tenga los siguientes atributos y
metodos:
• Atributos: base, altura.
• Metodos:
area(): Calcula y devuelve el area del rectangulo.
perimetro(): Calcula y devuelve el perimetro del rectangulo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return self.base * 2 + self.altura * 2

Rectangulo = Rectangulo(4, 6)
print("Area del rectangulo:", Rectangulo.area())
print("Perimetro del rectangulo:", Rectangulo.perimetro())

6. Pilares de la Programacion Orientada a Objetos
En base al siguiente codigo:
from abc import ABC, abstractmethod
class Animal(ABC):
@abstractmethod
def sonido(self):
pass
class Perro(Animal):
def sonido(self):
return "Guau"
class Gato(Animal):
def sonido(self):
return "Miau"

Explica:
¿Como se implementa la abstraccion en el codigo?
La abstracción se implementa a través de la clase Animal, 
que es una clase abstracta.

¿Que ventaja ofrece este enfoque?
La abstracción en este caso asegura que todas las subclases de Animal 
(como Perro y Gato) tengan el método sonido. Esto permite que cualquier 
objeto de tipo Animal tenga una estructura común, lo que facilita 
trabajar con ellos de forma uniforme en el código sin importar el 
tipo de animal específico.

¿Que ventaja tiene el polimorfismo en este caso?
El polimorfismo permite que cada tipo de animal (como Perro y Gato) 
responda de forma diferente al mismo método sonido

Explica como se podria aplicar la herencia en este ejemplo para extender
la funcionalidad a otros animales.
La herencia permite crear nuevas clases de animales que hereden de Animal.
Solo necesitamos definir su propio sonido.

"""