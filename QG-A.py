import matplotlib.pyplot as plt
import random
import timeit
import math
import numpy as np

#Bubble Sort
def bubbleSort(lista):

  tamanho = len(lista)

  for i in range(tamanho - 1):
    for j in range(tamanho - 1 - i):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]

  return lista

#Insertion Sort
def insertionSort(lista):

  tamanho = len(lista)

  for i in range(1, tamanho):
    elemento = lista[i]
    j = i - 1
    while j >= 0 and elemento < lista[j]:
      lista[j + 1] = lista[j]
      j = j - 1
    lista[j+1] = elemento

  return lista

#Selection Sort
def selectionSort(lista):

  tamanho = len(lista)

  for i in range(tamanho):
    j = i + 1
    minimo = i
    while j < tamanho:
      if lista[minimo] > lista[j]:
        minimo = j
      j = j + 1

    if lista[i] != lista[minimo]:
      lista[i], lista[minimo] = lista[minimo], lista[i]

  return lista

#Merge Sort
def mergeSort(lista):

  n = len(lista)

  if n <= 1:
    return lista

  metade = n//2
  listaEsquerda = mergeSort(lista[:metade])
  listaDireita = mergeSort(lista[metade:])

  return merge(listaEsquerda, listaDireita)

def merge(esquerda, direita):
  i = j = 0
  resultado = []

  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i = i + 1
    else:
      resultado.append(direita[j])
      j = j + 1

  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])

  return resultado

#Quick Sort
def quickSort(lista):
    quickSortOrdenar(lista, 0, len(lista) - 1)
    return lista

def quickSortOrdenar(lista, inicio, fim):

  if inicio >= fim:
    return

  pivot = particao(lista, inicio, fim)
  quickSortOrdenar(lista, inicio, pivot - 1)
  quickSortOrdenar(lista, pivot + 1, fim)

def particao(lista, inicio, fim):

  pivot = lista[inicio]
  i = inicio + 1

  for j in range(inicio + 1, fim + 1):
      if lista[j] < pivot:
          lista[i], lista[j] = lista[j], lista[i]
          i += 1

  lista[inicio], lista[i - 1] = lista[i - 1], lista[inicio]
  return i - 1

#Counting Sort
def countingSort(lista):

  minimo = min(lista)
  maximo = max(lista)
  tamanho = maximo - minimo + 1
  arrayCopia = [0 for i in range(len(lista))]
  arrayContagem = [0 for i in range(tamanho)]

  for i in range(0, len(lista)):
    arrayContagem[lista[i] - minimo] += 1

  for i in range(1, len(arrayContagem)):
    arrayContagem[i] += arrayContagem[i - 1]

  for i in range(len(lista) - 1, -1, -1):
    valor = lista[i]
    arrayContagem[valor - minimo] -= 1
    posicao = arrayContagem[valor - minimo]
    arrayCopia[posicao] = valor

  return arrayCopia

#Radix Sort
def radixSort(lista):

  negativos = [-x for x in lista if x < 0]
  nao_negativos = [x for x in lista if x >= 0]

  negativos_ordenados = []
  if negativos:
      minimo = max(negativos)
      exp = 1
      while minimo // exp > 0:
          negativos = contagem(negativos, exp)
          exp *= 10
      negativos_ordenados = [-x for x in reversed(negativos)]

  if nao_negativos:
      maximo = max(nao_negativos)
      exp = 1
      while maximo // exp > 0:
          nao_negativos = contagem(nao_negativos, exp)
          exp *= 10

  return negativos_ordenados + nao_negativos

def contagem(lista, exp):

  arrayContagem = [0 for i in range(10)]
  resultado = [0 for i in range(len(lista))]

  for i in range(0, len(lista)):
    digito = (lista[i] // exp) % 10
    arrayContagem[digito] += 1

  for i in range(1, 10):
    arrayContagem[i] += arrayContagem[i - 1]

  for i in range(len(lista) - 1, -1, -1):
    digito = (lista[i] // exp) % 10
    arrayContagem[digito] -= 1
    resultado[arrayContagem[digito]] = lista[i]

  return resultado

def bucketSort(lista):

  maximo = max(lista)
  minimo = min(lista)
  numBaldes = int(math.sqrt(len(lista))) or 1
  intervalo = (maximo - minimo + 1) / numBaldes
  baldes = [[] for _ in range(numBaldes)]

  for valor in lista:
    index = int((valor - minimo) / intervalo)
    if index == numBaldes:
      index -= 1
    baldes[index].append(valor)

  resultado = []
  for balde in baldes:
    balde = insertionSort(balde)
    resultado.extend(balde)

  return resultado

#Shell Sort
def shellSort(lista):

  n = len(lista)
  h = len(lista) // 2

  while h > 0:
    for i in range(h, n):
      valor = lista[i]
      j = i
      while j >= h and valor < lista[j - h]:
        lista[j] = lista[j - h]
        j = j - h
      lista[j] = valor
    h = int(h / 2)

  return lista

#Heap Sort
def heapify(lista, n, i):

  maior = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and lista[left] > lista[maior]:
    maior = left

  if right < n and lista[right] > lista[maior]:
    maior = right

  if maior != i:
    lista[maior], lista[i] = lista[i], lista[maior]
    heapify(lista, n, maior)

def heapSort(lista):

  n = len(lista)

  for i in range(n//2 - 1, -1, -1):
    heapify(lista, n, i)

  for i in range(n - 1, 0, -1):
    lista[0], lista[i] = lista[i], lista[0]
    heapify(lista, i, 0)

  return lista

lista = [random.randint(1, 100) for _ in range(10)]

def geraLista(tam):
  random.seed()
  i = 0
  lista = []
  while i < tam:
    lista.append(random.randint(1, tam))
    i += 1

  return lista

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

tempos = [[] for _ in range(10)]
cor = ['b', 'r', 'g', 'gray', 'pink', 'orange', 'y', 'c', 'navy', 'lightgreen']
labels = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Counting Sort', 'Radix Sort', 'Bucket Sort', 'Shell Sort', 'Heap Sort']

def main():
  for tamanho in tamanhos:
    lista = geraLista(tamanho)
    lista_teste = list(lista)
    i = 0

    tempo = timeit.timeit(lambda: bubbleSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: insertionSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: selectionSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: mergeSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: quickSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: countingSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: radixSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: bucketSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: shellSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    i += 1

    tempo = timeit.timeit(lambda: heapSort(list(lista_teste)), number=1)
    tempos[i].append(tempo)
    print("Lista de tamanho {} ordenada".format(tamanho))

  fig, (ax, ax2) = plt.subplots(2, 1, figsize=(8, 10))
  for i in range(10):
      ax.plot(tamanhos, tempos[i], color=cor[i], marker='o', linestyle='-', label=labels[i])

  ax.set_xlabel("Tamanho da Lista")
  ax.set_ylabel("Tempo (s)")
  ax.set_title("Desempenho do Bubble Sort")
  ax.legend()
  ax.grid(True)

  for i in range(10):
      ax2.plot(tamanhos, tempos[i], color=cor[i], marker='o', linestyle='-', label=labels[i])
  ax2.set_title("Zoom em tempos menores")
  ax2.set_ylabel("Tempo (s)")
  ax2.set_xlabel("Tamanho da Lista")
  ax2.set_ylim(0, 0.15)
  ax2.set_xlim(23500, 24500)
  ax2.legend(loc="upper right")
  ax2.grid(True)

  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
    main()