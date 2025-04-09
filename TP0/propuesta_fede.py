import sys

def min_piles(filename):
    cards=[]
    with open(filename, 'r') as file:
        for line in file:
            cards.append(int(line.strip()))
    
    piles = []
    for card in cards:
        placed = False
        for i in range(len(piles)):
            if card < piles[i][-1]:
                piles[i].append(card)
                placed = True
                break
        if not placed:
            piles.append([card])
    
    return len(piles)

def main():
    if len(sys.argv) != 2:
        print("Modo de Uso: python main.py archivo.txt")
        sys.exit(1)
    
    result = min_piles(sys.argv[1])
    print(result)

main()