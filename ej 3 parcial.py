"""3. Conjuntos
Crea una funcion llamada comparar sets que reciba dos listas de numeros 
enteros. Convierte ambas listas en conjuntos y realiza lo siguiente:
• Devuelve el conjunto que contiene los elementos comunes entre las dos
listas.
• Luego, devuelve el conjunto resultante de la diferencia simetrica 
entre los dos conjuntos.
• Ambos resultados deben ser devueltos como una tupla de conjuntos
Ejemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
Ejemplo de salida: ({3, 4}, {1, 2, 5, 6})"""


def comparar_sets (lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    interseccion = conjunto1 & conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    return interseccion, diferencia_simetrica

entrada1 = input("Ingresa la primera lista de numeros: ")
entrada2 = input("Ingresa la segunda lista de numeros: ")

lista1 = [] 
for num in entrada1.split():
    lista1.append(int(num))

lista2 = [] 
for num in entrada2.split():
    lista2.append(int(num))

resultado = comparar_sets(lista1, lista2)
print(resultado)