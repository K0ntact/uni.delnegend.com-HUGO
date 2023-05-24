---
title: 2022. G12 Final
draft: false
---

Given an array of 10 elements: 4, 15, 28, 45, 40, 9, 53, 41, 8, 17, 3, 5.

In this problem, we try to find all Pythagorean triplets that consists of 3 integer numbers (a, b, c) where $a^2 + b^2 = c^2$. The Pythagorean triple from the above array is: {(4, 3, 5), (15, 8, 17), (40, 9, 41), (28, 45, 53)}

# Problem 1
Write pseudo code using Recursion to find all Pythagorean triplets, then write a program in C/C++ to complete your proposed algorithm in the pseudo-code.

```cpp
#include <iostream>
using namespace std;

// ===========
// PSEUDO CODE
// ===========

// def condition(a: int, b: int, res: int) -> bool:
//     return a*a + b*b == res*res

// def loop(arr: list, ind_a: int, ind_b: int, ind_c: int, arr_length: int) -> None:
//     a = arr[ind_a]
//     b = arr[ind_b]
//     c = arr[ind_c]
//     if condition(a, b, c) or condition(a, c, b) or condition(b, c, a):
//         print(a, b, c)
//     if ind_c < arr_length - 1:
//         loop(arr, ind_a, ind_b, ind_c + 1, arr_length)
//     elif ind_b < arr_length - 2:
//         loop(arr, ind_a, ind_b + 1, ind_b + 2, arr_length)
//     elif ind_a < arr_length - 3:
//         loop(arr, ind_a + 1, ind_a + 2, ind_a + 3, arr_length)

bool condition(int a, int b, int result) {
    if (a*a + b*b == result*result) {
        return true;
    }
    return false;
}

void loop(int *array, int ind_a, int ind_b, int ind_c, int length) {
    int a = array[ind_a];
    int b = array[ind_b];
    int c = array[ind_c];
    if ((condition(a, b, c) == 1) || (condition(b, c, a) == 1) || (condition(c, a, b) == 1)) {
        cout << a << " " << b << " " << c << endl;
    }
    if (ind_c < length - 1) {
        loop(array, ind_a, ind_b, ind_c + 1, length);
    } else if (ind_b < length - 2) {
        loop(array, ind_a, ind_b + 1, ind_b + 2, length);
    } else if (ind_a < length - 3) {
        loop(array, ind_a + 1, ind_a + 2, ind_a + 3, length);
    }
}
// T(n) = O(n^3)

int main()
{
  int arr[] = {4, 15, 28, 45, 40, 9, 53, 41, 8, 17, 3, 5};
  int arr_length = sizeof(arr) / sizeof(arr[0]);
  loop(arr, 0, 1, 2, arr_length);
}
// T(n) = O(n^3)
```

# Problem 2
- Rewrite the program in C/C++ using **Linked List ADT** to solve this problem.
- Purpose a method to improve the complexity of finding the set of triplet values.

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

Node *createNode(int data) {
    Node *newNode = new Node;
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertNode(Node **head, int data) {
    Node *newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node *temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void printList(Node *head) {
    Node *temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

bool condition(int a, int b, int result) {
    if (a*a + b*b == result*result) {
        return true;
    }
    return false;
}

void loop(Node *head, int ind_a, int ind_b, int ind_c, int length) {
    Node *temp = head;
    int a, b, c;
    for (int i = 0; i < ind_a; i++) {
        temp = temp->next;
    }
    a = temp->data;
    for (int i = 0; i < ind_b - ind_a; i++) {
        temp = temp->next;
    }
    b = temp->data;
    for (int i = 0; i < ind_c - ind_b; i++) {
        temp = temp->next;
    }
    c = temp->data;
    if ((condition(a, b, c) == 1) || (condition(b, c, a) == 1) || (condition(c, a, b) == 1)) {
        cout << a << " " << b << " " << c << endl;
    }
    if (ind_c < length - 1) {
        loop(head, ind_a, ind_b, ind_c + 1, length);
    } else if (ind_b < length - 2) {
        loop(head, ind_a, ind_b + 1, ind_b + 2, length);
    } else if (ind_a < length - 3) {
        loop(head, ind_a + 1, ind_a + 2, ind_a + 3, length);
    }
}
// T(n) = O(n^3)

int main()
{
  Node *head = NULL;
  insertNode(&head, 4);
  insertNode(&head, 15);
  insertNode(&head, 28);
  insertNode(&head, 45);
  insertNode(&head, 40);
  insertNode(&head, 9);
  insertNode(&head, 53);
  insertNode(&head, 41);
  insertNode(&head, 8);
  insertNode(&head, 17);
  insertNode(&head, 3);
  insertNode(&head, 5);
  printList(head);
  loop(head, 0, 1, 2, 12);
}
```