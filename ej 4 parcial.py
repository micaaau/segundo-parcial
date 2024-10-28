"""4. Decoradores con multiples funciones
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
decorador multiplica el resultado original 5 por 3."""

def multiplicar_resultado(num):
    def decorador(func):
        def envoltura(a, b):
            return func(a, b) * num
        return envoltura
    return decorador

@multiplicar_resultado(3)
def suma (a, b):
    return a + b

@multiplicar_resultado(2)
def resta (a, b):
    return a - b    

a = float(input("Ingrese el primer numero para la suma: "))
b = float(input("Ingrese el segundo numero para la suma: "))
resultado_suma = suma(a, b)

a = float(input("Ingrese el primer numero para la resta: "))
b = float(input("Ingrese el segundo numero para la resta: "))
resultado_resta = resta(a, b)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)