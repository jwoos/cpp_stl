#include <stdlib.h>
#include <stdio.h>

#include "linked-list.h"

List* initializeList(Node* node) {
	List* list = malloc(sizeof(List));

	if (!node) {
		list -> head = NULL;
		list -> tail = NULL;
		list -> size = 0;
	} else {
		list -> head = node;
		list -> tail = node;
		list -> size = 1;
	}

	return list;
}

void deconstructList(List* list) {
	Node* current = list -> head;

	while (current != list -> tail) {
		Node* next = current -> next;

		free(current);

		current = next;
	}

	free(list);
	list = NULL;
}

Node* initializeNode(int data, Node* next) {
	Node* node = malloc(sizeof(Node));

	node -> data = data;
	node -> next = next ? next : NULL;

	return node;
}

void deconstuctNode(Node* node) {
	free(node);
}

void printList(List* list) {
	Node* current = list -> head;

	while (current != NULL) {
		printf("%d -> ", current -> data);
		current = current -> next;
	}

	printf("\n");
}

void pushList(List* list, int data) {
	Node* tail = list -> tail;

	Node* newElem = initializeNode(data, NULL);

	tail -> next = newElem;
	list -> tail = newElem;
	list -> size++;
}

Node* popList(List* list) {
	Node* tail = list -> tail;

	Node* current = list -> head;
	while (current -> next -> next != NULL) {
		current = current -> next;
	}

	current -> next = NULL;
	list -> tail = current;
	list -> size--;

	return tail;
}

Node* getElementList(List* list, int index) {
	if (index >= list -> size) {
		printf("Element not found at index %d - outside of range\n", index);
		return NULL;
	}

	Node* node = list -> head;

	int i = 0;
	while (i < index) {
		if (node != NULL) {
			i++;
			node = node -> next;
		} else {
			printf("Element not found at index %d outside of range\n", index);
			return NULL;
		}
	}

	return node;
}

void setElementList(List* list, int index, int newData) {
	Node* atIndex = getElementList(list, index);

	if (atIndex == NULL) {
		printf("Not setting - aborting...\n");
		return;
	}

	atIndex -> data = newData;
}

void insertList(List* list, int index, int newData) {
	Node* atIndex = getElementList(list, index - 1);

	Node* newNode = initializeNode(newData, atIndex -> next);
	atIndex -> next = newNode;

	list -> size++;
}

void deleteList(List* list, int index) {
	Node* prevIndex = getElementList(list, index - 1);
	Node* temp = prevIndex -> next;

	prevIndex -> next = prevIndex -> next -> next;

	free(temp);
	list -> size--;
}

void clearList(List* list) {
	Node* current = list -> head;
	Node* tempHolder[list -> size];

	int i = 0;
	while (current != NULL) {
		tempHolder[i] = current;
		current = current -> next;
		i++;
	}

	for (int i = 0; i < list -> size; i++) {
		free(tempHolder[i]);
	}

	list -> head = NULL;
	list -> tail = NULL;
	list -> size = 0;
}
