import sys

def solitario(mazo):
    pilas = []

    for c in mazo:
        menor_pila = -1

        for i in range(len(pilas)):
            # eleccion greedy: busco la pila valida de menor valor
            if c < pilas[i]:
                if menor_pila == -1 or pilas[i] < pilas[menor_pila]:
                    menor_pila = i

        if menor_pila != -1:
            pilas[menor_pila] = c
        else:
            pilas.append(c)

    return pilas


def main(argv):
    if len(argv) <= 1:
        return

    src = argv[1] # archivo
    mazo = []

    with open(src, "r") as f:
        c = f.readline()
        while c:
            mazo.append(int(c.rstrip()))
            c = f.readline()

    print(len(solitario(mazo)))


if __name__ == "__main__":
    main(sys.argv)