#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;             // 데이터 저장
    struct Node* next;    // 다음 노드를 가리키는 포인터
} Node;

// 새 노드를 생성하는 함수
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));  // 메모리 동적 할당
    newNode->data = data;
    newNode->next = NULL;  // 초기에는 다음 노드 없음
    return newNode;
}

// 리스트 앞에 노드 삽입
void insertAtHead(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;  // 새 노드의 next가 기존 head를 가리킴
    *head = newNode;        // head를 새 노드로 갱신
}

// 리스트 출력 함수
void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// 메모리 해제
void freeList(Node* head) {
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    Node* head = NULL;  // 처음에는 빈 리스트

    insertAtHead(&head, 10);
    insertAtHead(&head, 20);
    insertAtHead(&head, 30);

    printList(head);  // 예상 출력: 30 -> 20 -> 10 -> NULL

    freeList(head);
    return 0;
}
