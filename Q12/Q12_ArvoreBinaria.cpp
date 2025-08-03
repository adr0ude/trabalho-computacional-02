// Equipe 03: Dhiego Cavalcanti da Silveira, João Pedro dos Santos Jacome da Silva, Luís Guilherme Ferreira da Costa, Maria Eduarda Araujo Sales, Victor Oliveira do Nascimento
#include <iostream>
#include <vector>

using namespace std;

class Node
{
private:
    char valor;
    Node *esquerda;
    Node *direita;

public:
    Node(char valor)
    {
        this->valor = valor;
        this->esquerda = nullptr;
        this->direita = nullptr;
    }

    char getValor() { return this->valor; }
    Node *getEsquerda() { return this->esquerda; }
    Node *getDireita() { return this->direita; }

    void setValor(char valor)
    {
        this->valor = valor;
    }
    void setEsquerda(Node *node)
    {
        this->esquerda = node;
    }
    void setDireita(Node *node)
    {
        this->direita = node;
    }
};

class Tree
{
private:
    Node *raiz;

    Node *construirArvoreArray(const vector<char> &arr, int i)
    {
        if (i >= arr.size() || arr[i] == ' ')
        {
            return nullptr;
        }

        Node *node = new Node(arr[i]);
        node->setEsquerda(construirArvoreArray(arr, 2 * i + 1));
        node->setDireita(construirArvoreArray(arr, 2 * i + 2));
        return node;
    }

public:
    Tree() : raiz(nullptr) {}

    void construirArvore(const vector<char> &arr)
    {
        raiz = construirArvoreArray(arr, 0);
    }

    Node *getRaiz() { return raiz; }

    void preOrdem(Node *noAtual)
    {
        if (noAtual)
        {
            cout << noAtual->getValor() << " ";
            preOrdem(noAtual->getEsquerda());
            preOrdem(noAtual->getDireita());
        }
    }

    void emOrder(Node *noAtual)
    {
        if (noAtual)
        {
            emOrder(noAtual->getEsquerda());
            cout << noAtual->getValor() << " ";
            emOrder(noAtual->getDireita());
        }
    }

    void posOrdem(Node *noAtual)
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

    Tree tree;
    tree.construirArvore(arr);

    cout << "Pré-ordem: ";
    tree.preOrdem(tree.getRaiz());
    cout << "\nEm ordem: ";
    tree.emOrder(tree.getRaiz());
    cout << "\nPós-ordem: ";
    tree.posOrdem(tree.getRaiz());
    cout << endl;

    return 0;
}