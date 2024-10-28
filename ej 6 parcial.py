"""6. Pilares de la Programacion Orientada a Objetos
En base al siguiente codigo:"""

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
    
"""Explica:
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
Solo necesitamos definir su propio sonido."""