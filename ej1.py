def filtrar_y_modificar (lista): #EJERCICIO 1
    nueva_lista = []

    for num in lista:
        if num % 5 != 0:
            if num < 3:
                nueva_lista.append(num + 5)
            else:
                nueva_lista.append(num - 2)
    return nueva_lista

lista = [5, 10, 3, 15, 20, 24, 35]
resultado = filtrar_y_modificar(lista)
print(resultado)

def generar_matriz_invertida (n, m): ·EJERCICIO 2
    matriz = {}
    contador = n * m

    for i in range(n):
        for j in range(m):
            matriz[(i, j)] = contador
            contador -= 1

    return matriz

n = 2
m = 3
print(generar_matriz_invertida(n, m))

def operaciones_conjuntos (lista1, lista2): #EJERCICIO 3
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    diferencia = conjunto1 - conjunto2
    union = conjunto1 | conjunto2
    dif_simetrica = conjunto1 ^ conjunto2

    return diferencia, union, dif_simetrica

lista1 = [1, 4, 6, 3, 8]
lista2 = [1, 7, 5, 8, 3]
print(operaciones_conjuntos(lista1, lista2))

class circulo: #EJERCICIO 5
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return float(3.1415 * (self.radio ** 2))
    
    def circunferencia(self):
        return float(2 * 3.1415 * self.radio)
    
circ = circulo(5)
print(circ.area())
print(circ.circunferencia())

def operar_resultado(num1, num2):
    def decorador (func):
        def wrapper (*args, **kwargs):
            resultado = func (*args, **kwargs)
            return resultado + num1 + num2
        return wrapper
    return decorador

@operar_resultado(3, 2)
def multiplicar(a, b):
    return a * b

@operar_resultado(5, 1)
def dividir(a, b):
    return a / b

print(multiplicar(2, 3))
print(dividir(8, 4))