class Elemento:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
    
    def entra_en_mochila(self, mochila):
        return mochila.capacidad_restante >= self.peso

    def valor_por_kilo(self):
        return self.valor / self.peso

class Mochila:
    def __init__(self, capacidad_inicial):
        self.valor_acumulado = 0
        self.capacidad_restante = capacidad_inicial
        
    def agregar_elemento(self, elemento):
        self.valor_acumulado += elemento.valor
        self.capacidad_restante -= elemento.peso

def mochila_algoritmo_A(mochila, elementos):
    #ordenar los elementos por valor de mayor a menor
    elementos_por_valor = sorted(elementos, key=lambda x: x.valor, reverse= True)
    for elemento in elementos_por_valor:
        while elemento.entra_en_mochila(mochila):
            mochila.agregar_elemento(elemento)
    return mochila.valor_acumulado

def mochila_algoritmo_B(mochila, elementos):
    #ordenar los elementos por valor por kilo de mayor a menor
    elementos_por_valor = sorted(elementos, key=lambda x: x.valor_por_kilo(), reverse= True)
    for elemento in elementos_por_valor:
        while elemento.entra_en_mochila(mochila):
            mochila.agregar_elemento(elemento)
    return mochila.valor_acumulado

# Para probar nuevos ejemplos modificar las siguientes variables
# =======================
capacidad_mochila = 8
elementos = [ #Elemento(peso, valor)
    Elemento(7,35),
    Elemento(2,10)
]
# =======================

valor_en_mochila_A = mochila_algoritmo_A(Mochila(capacidad_mochila), elementos)
valor_en_mochila_B = mochila_algoritmo_B(Mochila(capacidad_mochila), elementos)
print("Valor final en mochila segun algoritmo A", valor_en_mochila_A)
print("Valor final en mochila segun algoritmo B", valor_en_mochila_B)
