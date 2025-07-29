import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def insertionSort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        
        vetor[j + 1] = chave
    
    return vetor

def contarOcorrencias(vetor, valor):
    contador = 0
    
    for item in vetor:
        if item == valor:
            contador += 1
    
    return contador

def main():
    limparTerminal()
    print("Digite 10 números inteiros:\n")
    numeros = []

    for i in range(10):
        num = int(input(f"{i + 1}° Número: "))
        numeros.append(num)

    numeros_ordenados = insertionSort(numeros.copy())

    menor = numeros_ordenados[0]
    maior = numeros_ordenados[-1]

    freq_menor = contarOcorrencias(numeros_ordenados, menor)
    freq_maior = contarOcorrencias(numeros_ordenados, maior)

    limparTerminal()
    print("\nNúmeros desordendos:", numeros)
    print("Números ordenados:", numeros_ordenados)
    print(f"\nMenor número: {menor} (aparece {freq_menor} vezes)")
    print(f"Maior número: {maior} (aparece {freq_maior} vezes)\n")

if __name__ == "__main__":
    main()