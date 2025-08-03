// Equipe 03: Dhiego Cavalcanti da Silveira, João Pedro dos Santos Jacome da Silva, Luís Guilherme Ferreira da Costa, Maria Eduarda Araujo Sales, Victor Oliveira do Nascimento
#include <iostream>
#include <vector>

using namespace std;

class Node
{
private:
    char value;
    Node *left;
    Node *right;

public:
    Node(char value)
    {
        this->value = value;
        this->left = nullptr;
        this->right = nullptr;
    }

    char getValue() { return this->value; }
    Node *getLeft() { return this->left; }
    Node *getRight() { return this->right; }

    void setValue(char value) { this->value = value; }
    void setLeft(Node *node) { this->left = node; }
    void setRight(Node *node) { this->right = node; }
};

class Tree
{
private:
    Node *root;

    Node *buildTreeFromArray(const vector<char> &arr, int index)
    {
        if (index >= arr.size() || arr[index] == ' ')
        {
            return nullptr;
        }

        Node *node = new Node(arr[index]);
        node->setLeft(buildTreeFromArray(arr, 2 * index + 1));
        node->setRight(buildTreeFromArray(arr, 2 * index + 2));
        return node;
    }

public:
    Tree() : root(nullptr) {}

    void buildFromArray(const vector<char> &arr)
    {
        root = buildTreeFromArray(arr, 0);
    }

    Node *getRoot() { return root; }

    void preorder(Node *current)
    {
        if (current)
        {
            cout << current->getValue() << " ";
            preorder(current->getLeft());
            preorder(current->getRight());
        }
    }

    void inorder(Node *current)
    {
        if (current)
        {
            inorder(current->getLeft());
            cout << current->getValue() << " ";
            inorder(current->getRight());
        }
    }

    void postorder(Node *current)
    {
        if (current)
        {
            postorder(current->getLeft());
            postorder(current->getRight());
            cout << current->getValue() << " ";
        }
    }
};

int main()
{
    vector<char> arr = {
        'A', // 0
        'B', // 1
        'C', // 2
        'D', // 3
        'E', // 4
        'F', // 5
        'G', // 6
        'H', // 7
        'I', // 8
        'J', // 9
        'K', // 10
        'L', // 11
    };

    Tree tree;
    tree.buildFromArray(arr);

    cout << "Pré-ordem: ";
    tree.preorder(tree.getRoot());
    cout << "\nEm ordem: ";
    tree.inorder(tree.getRoot());
    cout << "\nPós-ordem: ";
    tree.postorder(tree.getRoot());
    cout << endl;

    return 0;
}