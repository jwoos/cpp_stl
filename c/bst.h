#ifndef BINARY_SEARCH_TREE_H
#define BINARY_SEARCH_TREE_H

typedef struct BSTNode {
	int data;
	struct BSTNode* left;
	struct BSTNode* right;
	struct BSTNode* parent;
} BSTNode;

typedef struct BST {
	BSTNode* root;
} BST;

BST* bstInitialize(BSTNode*);

void bstDeconstruct(BST*);

BSTNode* bstNodeInitialize(int, BSTNode*, BSTNode*, BSTNode*);

void bstNodeDeconstruct(BSTNode*);

void bstInsert(BST*, int);

#endif
