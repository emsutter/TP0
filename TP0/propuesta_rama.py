import sys

"""
Contamos con cartas numeradas del 1 al “n” mezcladas en un orden desconocido. No podemos modificar ese orden ni observar que cartas hay, excepto la que se encuentra arriba. 
Debemos iterativamente tomar la carta superior, observarla y apilarla. Una carta puede formar una pila nueva o ubicarse en una existente. Para ubicarla en una existente debe 
ser menor a la carta superior de esa pila. Una vez ubicada la carta, no se puede mover y pasa a ser la carta superior. El objetivo es ubicar todas las cartas en la menor cantidad
de pilas posible.

"""

def read_file(filename):

    with open(filename, "r") as file:
        lines = file.readlines()

    cartas = []

    for line in lines:  
        line = int(line.strip())
        cartas.append(line)
    
    return cartas

def ordenar_cartas(cartas):
    
    pilas = [[cartas[0]]]

    for carta in cartas[1:]:
        pilas.sort(key=lambda x: x[-1])
        colocada = False
        for pila in pilas:

            if carta < pila[-1]:

                pila.append(carta)
                colocada = True
                break
        
        if not colocada:
            pilas.append([carta])

    print(len(pilas))
        
def main():

    filename = sys.argv[1]
    
    try:

        cartas = read_file(filename)
        ordenar_cartas(cartas)
        

    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()