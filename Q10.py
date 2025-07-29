import os

def limparTerminal():
    os.system("cls" if os.name == "nt" else "clear")

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo_node = Node(valor)
        
        if not self.cabeca:
            self.cabeca = novo_node
        else:
            atual = self.cabeca
            
            while atual.proximo:
                atual = atual.proximo
            
            atual.proximo = novo_node

    def imprimir(self):
        atual = self.cabeca
        valores = []
        
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        
        print(" -> ".join(valores))

    def selectionSort(self):
        atual = self.cabeca
        
        while atual:
            menor = atual
            proximo = atual.proximo
            
            while proximo:
                if proximo.valor < menor.valor:
                    menor = proximo
                
                proximo = proximo.proximo

            atual.valor, menor.valor = menor.valor, atual.valor
            atual = atual.proximo

def main():
    limparTerminal()
    lista = ListaEncadeada()
    numeros = [29, 10, 14, 37, 13]

    for num in numeros:
        lista.inserir(num)
    
    limparTerminal()
    print("Lista antes da ordenação:")
    lista.imprimir()

    lista.selectionSort()

    print("\nLista após ordenação com Selection Sort:")
    lista.imprimir()
    print("")

if __name__ == "__main__":
    main()