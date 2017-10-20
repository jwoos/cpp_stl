#ifndef OPEN_HASH_MAP_H
#define OPEN_HASH_MAP_H


#include <stdlib.h>
#include "../linked-list/single.h"


typedef struct OpenHashMap {
	unsigned int currentSize;
	unsigned int maxSize;
	SingleList* store;
} OpenHashMap;

typedef struct OpenHashMapNode {
	char* key;
	void* data;
} OpenHashMapNode;


OpenHashMap* openHashMapConstruct(unsigned int);

void openHashMapDeconstruct(OpenHashMap*);

OpenHashMapNode* openHashMapNodeConstruct(char*, void*);

void openHashMapNodeDeconstruct(OpenHashMapNode*);


#endif
