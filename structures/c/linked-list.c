#include <stdlib.h>
#include <stdio.h>

#include "linked-list.h"

List* listInitialize(ListNode* node) {
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

void listDeconstruct(List* list) {
	ListNode* current = list -> head;

	while (current != list -> tail) {
		ListNode* next = current -> next;

		free(current);

		current = next;
	}

	free(list);
	list = NULL;
}

ListNode* listNodeInitialize(int data, ListNode* next) {
	ListNode* node = malloc(sizeof(ListNode));

	node -> data = data;
	node -> next = next ? next : NULL;

	return node;
}

void listNodeDeconstruct(ListNode* node) {
	free(node);
}

void listPrint(List* list) {
	ListNode* current = list -> head;

	while (current != NULL) {
		printf("%d -> ", current -> data);
		current = current -> next;
	}

	printf("\n");
}

void listPush(List* list, int data) {
	ListNode* tail = list -> tail;

	ListNode* newElem = listNodeInitialize(data, NULL);

	tail -> next = newElem;
	list -> tail = newElem;
	list -> size++;
}

ListNode* listPop(List* list) {
	ListNode* tail = list -> tail;

	ListNode* current = list -> head;
	while (current -> next -> next != NULL) {
		current = current -> next;
	}

	current -> next = NULL;
	list -> tail = current;
	list -> size--;

	return tail;
}

ListNode* listGetElement(List* list, int index) {
	if (index >= list -> size) {
		printf("Element not found at index %d - outside of range\n", index);
		return NULL;
	}

	ListNode* node = list -> head;

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

void listSetElement(List* list, int index, int newData) {
	ListNode* atIndex = listGetElement(list, index);

	if (atIndex == NULL) {
		printf("Not setting - aborting...\n");
		return;
	}

	atIndex -> data = newData;
}

void listInsert(List* list, int index, int newData) {
	ListNode* atIndex = listGetElement(list, index - 1);

	ListNode* newNode = listNodeInitialize(newData, atIndex -> next);
	atIndex -> next = newNode;

	list -> size++;
}

void listDelete(List* list, int index) {
	ListNode* prevIndex = listGetElement(list, index - 1);
	ListNode* temp = prevIndex -> next;

	prevIndex -> next = prevIndex -> next -> next;

	free(temp);
	list -> size--;
}

void listClear(List* list) {
	ListNode* current = list -> head;
	ListNode* tempHolder[list -> size];

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
