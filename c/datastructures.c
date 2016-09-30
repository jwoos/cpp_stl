#include <stdlib.h>
#include <stdio.h>

#include "linked-list.h"
#include "vector.h"

void checkList() {
	Node* head = initializeNode(10, NULL);
	List* list = initializeList(head);

	for (int i = 2; i < 10; i++) {
		pushList(list, i * 10);
	}

	printList(list);

	Node* popped = popList(list);

	printList(list);
	printf("popped address: %p data: %d\n", (void*) popped, popped -> data);

	printf("index 2: %d\n", getElementList(list, 2) -> data);
	printf("index 10: %p\n", (void*)getElementList(list, 10));

	setElementList(list, 2, 1000);
	printf("index 2: %d\n", getElementList(list, 2) -> data);

	insertList(list, 5, 2000);
	printList(list);
	deleteList(list, 5);
	printList(list);

	clearList(list);
	printList(list);
	printf("size: %d, head: %p tail: %p\n", list -> size, (void*)list -> head, (void*)list -> tail);

	free(popped);
	free(list);
}

void checkVector() {
	Vector* vector = initializeVector();
	for (int i = 0; i < 100; i++) {
		pushVector(vector, i);

		printf("size: %d, capacity: %d \n", vector -> size, vector -> capacity);
	}
	printVector(vector);

	printf("popped data:");
	for (int i = 0; i < 50; i++) {
		printf(" %d,", popVector(vector));
	}
	printf("\n");
	printf("size: %d, capacity: %d \n", vector -> size, vector -> capacity);
	printVector(vector);

	insertVector(vector, 10, 100);
	printVector(vector);
	deleteVector(vector, 10);
	printVector(vector);
	clearVector(vector);
	printf("size: %d, capacity: %d \n", vector -> size, vector -> capacity);

	free(vector -> arr);
	free(vector);
}

int main() {
	checkList();
	checkVector();

	return 0;
}
