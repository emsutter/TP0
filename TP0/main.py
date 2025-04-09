# Contamos con cartas numeradas del 1 al “n” mezcladas en un orden desconocido.
# No podemos modificar ese orden ni observar que cartas hay, excepto la que se encuentra arriba. 
# Debemos iterativamente tomar la carta superior, observarla y apilarla. 
# Una carta puede formar una pila nueva o ubicarse en una existente. 
# Para ubicarla en una existente debe ser menor a la carta superior de esa pila. 
# Una vez ubicada la carta, no se puede mover y pasa a ser la carta superior. 
# El objetivo es ubicar todas las cartas en la menor cantidad de pilas posible.

# Se pide:
# Presentar un programa en python que resuelva el problema. 
# Debe cumplir AL PIE DE LA LETRA el formato de entrada y salida según se detalla posteriormente.

# Indicar qué estructuras de datos utiliza para su programa.
# Indicar la complejidad temporal y espacial del programa (sin análisis).
# Explicar en una oración la estrategia greedy.
# Definir en una oración cuál es el óptimo local
# Formato del programa:
# El archivo a ejecutar se debe llamar main.py Debe recibir por parámetro el nombre de un archivo que contenga las cartas mezcladas.
# El formato del archivo de cartas debe ser texto. Cada línea del archivo corresponde a una carta. Por ejemplo:

# 1
# 4
# 10
# 7
# 2
# 5
# 9
# 3
# 8
# 6
# La salida del programa debe ser por pantalla y solo contener un número con la cantidad de pilas construidas.
# Formato de ejecución del programa: main.py archivo.txt
import sys

def apilar_cartas(archivo):
    with open(archivo, 'r') as f:
        cartas = [int(line.strip()) for line in f]

    pilas = []
    
    for carta in cartas:
        apilada = False
        for pila in pilas:
            if carta < pila[-1]:
                pila.append(carta)
                apilada = True
                break
        if not apilada:
            pilas.append([carta])
    print(len(pilas))
    
def main():
    archivo = sys.argv[1]
    apilar_cartas(archivo)

main()