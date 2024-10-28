"""2. Ciclos anidados y Diccionarios
Escribe una funcion llamada generar matriz que:
• Reciba dos numeros enteros n y m (numero de filas y columnas).
• Devuelva un diccionario donde las claves sean las coordenadas (i, j) 
y los valores sean numeros enteros consecutivos, comenzando en 1.
Ejemplo de entrada: n = 3, m = 2
Ejemplo de salida: {(0,0): 1, (0,1): 2, (1,0): 3, (1,1): 4, (2,0):
5, (2,1): 6}"""

def generar_matriz (n, m):
    matriz = {}
    contador = 1

    for i in range(n):
        for j in range(m):
            matriz[(i, j)] = contador
            contador += 1

    return matriz

n = int(input("Ingrese un numero de filas: ")) 
m = int(input("Ingrese un numero de columnas: "))

resultado = generar_matriz(n, m)
print(resultado)