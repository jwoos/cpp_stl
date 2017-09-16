#include "fixed-hash-map.h"


FixedHashMap* hashMapConstruct(unsigned int s) {
	FixedHashMap* hm = malloc(sizeof *hm);
	if (!hm) {
		return NULL;
	}

	hm -> currentSize = 0;
	hm -> maxSize = s;
	hm -> store = listConstruct();

	return hm;
}

void hashMapDeconstruct(FixedHashMap* hm) {
	listDeconstruct(hm -> store);
	free(hm);
	hm = NULL;
}

FixedHashMapNode* hashMapNodeConstruct(char* key, void* data) {
	FixedHashMapNode* hmNode = malloc(sizeof *hmNode);
	hmNode -> key = key;
	hmNode -> data = data;

	return hmNode;
}

void hashMapNodeDeconstruct(FixedHashMapNode* hmNode) {
	free(hmNode);
}
