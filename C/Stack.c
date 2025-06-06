#include <stdio.h>
#include <stdlib.h>
#define SIZE 100

typedef struct {
    int arr[SIZE]; // int형 데이터 100개
    int top;
} StackType;

void init(StackType *s) {
    s->top = -1;
}

// empty면 1을 리턴, 아니면 0 리턴
int is_empty(StackType *s) {
    if (s->top == -1)
        return 1;
    return 0;
}

// full이면 1을 리턴, 아니면 0 리턴
int is_full(StackType *s) {
    if (s->top == SIZE - 1)
        return 1;
    return 0;
}

void push(StackType *s, int value) {
    if (is_full(s)) {
        printf("stack is full\n");
        exit(1);
    }
    printf("pushed value : %d\n", value);
    s->arr[++(s->top)] = value;
}

int pop(StackType *s) {
    if (is_empty(s)) {
        printf("stack is empty\n");
        exit(1);
    }
    return s->arr[(s->top)--];
}

int peek(StackType *s) {
    if (is_empty(s)) {
        printf("stack is empty\n");
        exit(1);
    }
    return s->arr[(s->top)];
}

int main() {
    StackType s;
    init(&s);

    push(&s, 3);
    push(&s, 2);
    push(&s, 1);

    printf("value top: %d\n", peek(&s));  // 확인용


    
    printf("value: %d\n", pop(&s));   // 확인용
    
    printf("value: %d\n", pop(&s)); 
    
    printf("value: %d\n", pop(&s)); 


    return 0;
}
