// Equipe 03: Dhiego Cavalcanti da Silveira, João Pedro dos Santos Jacome da Silva, Luís Guilherme Ferreira da Costa, Maria Eduarda Araujo Sales, Victor Oliveira do Nascimento
#include <iostream>
#include <vector>

using namespace std;

class No
{
private:
    char valor;
    No *esquerda;
    No *direita;

public:
    No(char valor)
    {
        this->valor = valor;
        this->esquerda = nullptr;
        this->direita = nullptr;
    }

    char getValor() { return this->valor; }
    No *getEsquerda() { return this->esquerda; }
    No *getDireita() { return this->direita; }

    void setValor(char valor)
    {
        this->valor = valor;
    }
    void setEsquerda(No *node)
    {
        this->esquerda = node;
    }
    void setDireita(No *node)
    {
        this->direita = node;
    }
};

class Arvore
{
private:
    No *raiz;

    No *construirArvoreArray(const vector<char> &arr, int i)
    {
        if (i >= arr.size() || arr[i] == ' ')
        {
            return nullptr;
        }

        No *no = new No(arr[i]);
        no->setEsquerda(construirArvoreArray(arr, 2 * i + 1));
        no->setDireita(construirArvoreArray(arr, 2 * i + 2));
        return no;
    }

public:
    Arvore() : raiz(nullptr) {}

    void construirArvore(const vector<char> &arr)
    {
        raiz = construirArvoreArray(arr, 0);
    }

    No *getRaiz() { return raiz; }

    void preOrdem(No *noAtual)
    {
        if (noAtual)
        {
            cout << noAtual->getValor() << " ";
            preOrdem(noAtual->getEsquerda());
            preOrdem(noAtual->getDireita());
        }
    }

    void emOrder(No *noAtual)
    {
        if (noAtual)
        {
            emOrder(noAtual->getEsquerda());
            cout << noAtual->getValor() << " ";
            emOrder(noAtual->getDireita());
        }
    }

    void posOrdem(No *noAtual)
    {
        if (noAtual)
        {
            posOrdem(noAtual->getEsquerda());
            posOrdem(noAtual->getDireita());
            cout << noAtual->getValor() << " ";
        }
    }
};

int main()
{
    vector<char> arr = {
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
    };

    Arvore arvore;
    arvore.construirArvore(arr);

    cout << "Pré-ordem: ";
    arvore.preOrdem(arvore.getRaiz());
    cout << "\nEm ordem: ";
    arvore.emOrder(arvore.getRaiz());
    cout << "\nPós-ordem: ";
    arvore.posOrdem(arvore.getRaiz());
    cout << endl;

    return 0;
}