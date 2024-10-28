"""1. Listas y Condicionales
Dada una lista de numeros enteros, escribe una funci´on llamada 
filtrar y modificar que:
• Elimine los numeros impares.
• Devuelva una lista donde los numeros restantes se dividan entre 2 si son
mayores a 10, o se multipliquen por 2 si son menores o iguales a 10.
Ejemplo de entrada: [3, 14, 6, 12, 7, 18]
Ejemplo de salida: [7, 3, 6]"""

def filtrar_y_modificar (lista):
    resultado = []

    for num in lista:
        if num % 2 == 0: #pares
            if num > 10:
                resultado.append(int(num / 2))
            else:
                resultado.append(int(num * 2))
    
    return resultado
"""entrada = input("Ingresa una lista de numeros: ")

lista_numeros = [] 
for num in entrada.split():
    lista_numeros.append(int(num))

salida = filtrar_y_modificar(lista_numeros)
print(salida)"""
listaEntrada = [3, 14, 6, 12, 7, 18]
print(listaEntrada)
listaSalida = filtrar_y_modificar(listaEntrada)
print(listaSalida) 