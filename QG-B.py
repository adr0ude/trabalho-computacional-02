import random
import time
import math
import matplotlib.pyplot as plt

# ---------- Algoritmos de Ordenação ----------
def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

# ---------- Algoritmos de Busca ----------
def busca_linear(vetor, chave):
    for i in range(len(vetor)):
        if vetor[i] == chave:
            return i
    return -1

def busca_linear_sentinela(vetor, chave):
    vetor.append(chave)
    i = 0
    while vetor[i] != chave:
        i += 1
    vetor.pop()
    return i if i < len(vetor) else -1

def busca_binaria(vetor, chave):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def busca_binaria_rapida(vetor, chave):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return esquerda if esquerda < len(vetor) and vetor[esquerda] == chave else -1

# ---------- Parâmetros ----------
tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos = {
    "busca_linear": [],
    "busca_linear_sentinela": [],
    "busca_binaria": [],
    "busca_binaria_rapida": []
}

# ---------- Entrada da chave ----------
entrada = input("Digite o valor da chave a ser buscada (ou pressione Enter para gerar aleatoriamente): ")
chave_usuario = int(entrada) if entrada.strip().isdigit() else None

# ---------- Execução dos testes ----------
for tamanho in tamanhos:
    print(f"Executando testes para vetor de tamanho {tamanho}...")
    vetor = random.sample(range(0, tamanho * 2), tamanho)
    chave = chave_usuario if chave_usuario is not None else random.choice(vetor)

    # Linear
    inicio = time.perf_counter()
    busca_linear(vetor[:], chave)
    tempos["busca_linear"].append(time.perf_counter() - inicio)

    # Linear com sentinela
    inicio = time.perf_counter()
    busca_linear_sentinela(vetor[:], chave)
    tempos["busca_linear_sentinela"].append(time.perf_counter() - inicio)

    # Ordenar para busca binária
    vetor_ordenado = vetor[:]
    insertion_sort(vetor_ordenado)

    # Binária
    inicio = time.perf_counter()
    busca_binaria(vetor_ordenado[:], chave)
    tempos["busca_binaria"].append(time.perf_counter() - inicio)

    # Binária rápida
    inicio = time.perf_counter()
    busca_binaria_rapida(vetor_ordenado[:], chave)
    tempos["busca_binaria_rapida"].append(time.perf_counter() - inicio)

# ---------- Gráfico de tempo de execução ----------
plt.figure(figsize=(10, 6))
for metodo, valores in tempos.items():
    plt.plot(tamanhos, valores, marker='o', label=metodo.replace("_", " ").capitalize())

plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo de execução (s)")
plt.title("Comparativo de Tempo de Execução das Buscas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Gráfico do número de comparações ----------
comparacoes = {
    "Busca Linear": [n / 2 for n in tamanhos],
    "Busca Linear Sentinela": [n / 2 for n in tamanhos],
    "Busca Binária": [math.log2(n) for n in tamanhos],
    "Busca Binária Rápida": [math.log2(n) for n in tamanhos]
}

plt.figure(figsize=(10, 6))
for metodo, valores in comparacoes.items():
    plt.plot(tamanhos, valores, label=metodo)

plt.xlabel("Número de elementos (N)")
plt.ylabel("Número de comparações")
plt.title("Comparativo de Número de Comparações nas Buscas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Comentários sobre os gráficos ----------
print("\nComentários:")
print("1. A busca linear e a com sentinela têm tempo proporcional a N.")
print("2. As buscas binárias são muito mais rápidas com crescimento logarítmico.")
print("3. Para vetores grandes, a ordenação para a busca binária compensa.")
print("4. A busca com sentinela é levemente mais rápida que a linear padrão.")
