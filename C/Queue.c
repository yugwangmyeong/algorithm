#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 3

typedef struct{
    int front;
    int rear;
    int data[MAX];
} Queue;

int is_full(Queue *q){
    if (q-> rear == MAX - 1)
        return ((q->rear)+1 % MAX == q->front);
    return 0;
}

int is_empty(Queue *q){
    return q-> front == q-> rear;
}
void init(Queue *q){
    q -> front = q -> rear = 0;

}
void enqueue(Queue *q, int item){
    if(is_full(q)){
        printf("Error Queue is full");
        exit(1);
    }
    q->rear =(q->rear+1) % MAX;
    q -> data[q->rear] = item;
}

int dequeue(Queue *q){
    if(is_empty(q)){
        printf("Error queue is empty");
        exit(1);
    }
    q -> front = (q->front + 1) % MAX;
    return q->data[q->front];
}

int main(){
    Queue q;
    init(&q);

    enqueue(&q,3);
    enqueue(&q,2);


    printf("%d\n",dequeue(&q));
    printf("%d\n",dequeue(&q));
    

    enqueue(&q,3);
    enqueue(&q,1);
    printf("%d",dequeue(&q));
    printf("%d",dequeue(&q));
    return 0;
}