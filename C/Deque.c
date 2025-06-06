#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DEQUE_SIZE 5

typedef int element;

typedef struct{
    element data[MAX_DEQUE_SIZE];
    int front,rear;
} Deque;

void error(char *message){
    fprintf(stderr,"%s\n",message);
    exit(1);

}

int is_full(Deque *d){
    return ((d->rear+1) % MAX_DEQUE_SIZE == d->front);
}

int is_empty(Deque *d){
    return d-> front == d-> rear;
}
void init_deque(Deque *d){
    d -> front = d -> rear = 0;

}
void add_front(Deque *d, int item){
    if(is_full(d)){
        printf("Error Queue is full\n");
        exit(1);
    }
    d->front = (d->front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
    d->data[d->front]= item;
    
}
element delete_front(Deque *d){
    if (is_empty(d))
        error("Deque is empty");

    element item = d->data[d->front];  // 현재 front 위치의 데이터를 꺼내고
    if (d->front == d->rear) {          // 만약 이게 마지막 요소였다면
        init_deque(d);                  // 덱을 초기화 (front = rear = 0)
    } else {
        d->front = (d->front + 1) % MAX_DEQUE_SIZE;  // 아니면 그냥 front 이동
    }
    return item;
}



void add_rear(Deque *d,element item){
    if(is_full(d))
        error("Deque is full");
    d->rear = (d->rear + 1) % MAX_DEQUE_SIZE;
    d->data[d->rear] = item;
}

element delete_rear(Deque *d){
    if (is_empty(d))
        error("Deque is empty");

    element item = d->data[d->rear];
    if (d->front == d->rear) {
        init_deque(d);
    } else {
        d->rear = (d->rear - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
    }
    return item;
}

element get_front(Deque *d){
    if(is_empty(d))
        error("Deque is empty");
    return d->data[d->front];
}

element get_rear(Deque *d){
    if(is_empty(d))
        error("Deque is empty");
    return d->data[d->rear];
}



int main(){
    Deque d;
    init_deque(&d);

    add_rear(&d, 1);
    add_rear(&d, 2);
    add_front(&d, 5);
    add_front(&d, 7);
    printf("Front: %d\n", get_front(&d)); // 0
    printf("Rear: %d\n", get_rear(&d));   // 2

    printf("%d\n", delete_front(&d)); // 7
    printf("%d\n", delete_rear(&d));  // 2

    printf("%d\n", delete_front(&d)); // 5
    printf("%d\n", delete_rear(&d));  // 1

    return 0;
}