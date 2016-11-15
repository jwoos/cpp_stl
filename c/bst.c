#include <stdlib.h>
#include <stdbool.h>

#include "bst.h"

BST* bstInitialize(BSTNode* node) {
	BST* bst = malloc(sizeof(BST));

	bst -> root = node ? node : NULL;

	return bst;
}

// TODO
void bstDeconstruct(BST* bst) {
	BSTNode* current = bst -> root;
}

BSTNode* bstNodeInitialize(int data, BSTNode* parent, BSTNode* left, BSTNode* right) {
	BSTNode* node = malloc(sizeof(BSTNode));

	node -> data = data ? data : 0;
	node -> parent = parent ? parent : NULL;
	node -> left = left ? left : NULL;
	node -> right = right ? right : NULL;

	return node;
}

void bstNodeDeconstruct(BSTNode* node) {
	free(node);
}

void bstInsert(BST* bst, int data) {
	BSTNode* current = bst -> root;

	if (current == NULL) {
		return;
	}

	while (true) {
		if (data < current -> data) {
			if (current -> left == NULL) {
				current -> left = bstNodeInitialize(data, current -> left, NULL, NULL);
				break;
			}

			current = current -> left;
		} else {
			if (current -> right == NULL) {
				current -> right = bstNodeInitialize(data, current -> right, NULL, NULL);
				break;
			}

			current = current -> right;
		}
	}
}
