#include <stdlib.h>
#include <stdio.h>

#include "linked-list.h"

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

int main() {
	checkList();

	return 0;
}
