#include <stdio.h>
#include <stdlib.h>

// Definição do nó da lista
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Função para criar um novo nó
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Erro ao alocar memória.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Função para inserir no final da lista
void insertEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

// Busca sequencial
Node* sequentialSearch(Node* head, int target) {
    while (head != NULL) {
        if (head->data == target)
            return head;
        head = head->next;
    }
    return NULL;
}

// Função auxiliar para retornar o ponteiro do meio entre dois nós
Node* getMiddle(Node* start, Node* end) {
    if (start == NULL)
        return NULL;
    Node* slow = start;
    Node* fast = start->next;

    while (fast != end) {
        fast = fast->next;
        if (fast != end) {
            slow = slow->next;
            fast = fast->next;
        }
    }
    return slow;
}

// Busca binária (lista ordenada!)
Node* binarySearch(Node* head, int target) {
    Node* start = head;
    Node* end = NULL;

    do {
        Node* mid = getMiddle(start, end);
        if (mid == NULL)
            return NULL;

        if (mid->data == target)
            return mid;
        else if (mid->data < target)
            start = mid->next;
        else
            end = mid;
    } while (end == NULL || end != start);

    return NULL;
}

// Função para imprimir a lista
void printList(Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// Exemplo de uso
int main() {
    Node* list = NULL;
    // Lista ordenada
    insertEnd(&list, 1);
    insertEnd(&list, 3);
    insertEnd(&list, 5);
    insertEnd(&list, 7);
    insertEnd(&list, 9);
    insertEnd(&list, 11);

    printf("Lista:\n");
    printList(list);

    int value = 7;
    Node* resultSeq = sequentialSearch(list, value);
    if (resultSeq)
        printf("Busca Sequencial: Encontrado %d.\n", resultSeq->data);
    else
        printf("Busca Sequencial: Não encontrado.\n");

    Node* resultBin = binarySearch(list, value);
    if (resultBin)
        printf("Busca Binária: Encontrado %d.\n", resultBin->data);
    else
        printf("Busca Binária: Não encontrado.\n");

    return 0;
}