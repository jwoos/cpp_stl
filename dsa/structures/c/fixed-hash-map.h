#ifndef FIXED_HASH_MAP_H
#define FIXED_HASH_MAP_H


#include <stdlib.h>
#include "single-linked-list.h"


typedef struct FixedHashMap {
	unsigned int currentSize;
	unsigned int maxSize;
	SingleList* store;
} FixedHashMap;

typedef struct FixedHashMapNode {
	char* key;
	void* data;
} FixedHashMapNode;


FixedHashMap* hashMapConstruct(unsigned int);

void hashMapDeconstruct(FixedHashMap*);

FixedHashMapNode* hashMapNodeConstruct(char*, void*);

void hashMapNodeDeconstruct(FixedHashMapNode*);


#endif
