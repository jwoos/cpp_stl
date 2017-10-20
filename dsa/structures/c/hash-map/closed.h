#ifndef CLOSED_HASH_MAP_H
#define CLOSED_HASH_MAP_H


#include <stdint.h>

#include "../utils.h"


typedef struct ClosedHashMap {
	unsigned int currentSize;
	unsigned int maxSize;
} ClosedHashMap;

typedef struct ClosedHashMapNode {
	char* key;
	void* data;
} ClosedHashMapNode;


ClosedHashMap* closedHashMapConstruct(unsigned int);

void closedHashMapDeconstruct(ClosedHashMap*);

ClosedHashMapNode* closedHashMapNodeConstruct(char*, void*);

void closedHashMapNodeDeconstruct(ClosedHashMapNode*);


#endif
