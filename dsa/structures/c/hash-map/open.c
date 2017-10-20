#include "open.h"


OpenHashMap* openHashMapConstruct(unsigned int s) {
	OpenHashMap* hm = malloc(sizeof *hm);
	if (!hm) {
		return NULL;
	}

	hm -> currentSize = 0;
	hm -> maxSize = s;
	/*hm -> store = listConstruct();*/

	return hm;
}

void openHashMapDeconstruct(OpenHashMap* hm) {
	listDeconstruct(hm -> store);
	free(hm);
	hm = NULL;
}

OpenHashMapNode* openHashMapNodeConstruct(char* key, void* data) {
	OpenHashMapNode* hmNode = malloc(sizeof *hmNode);
	hmNode -> key = key;
	hmNode -> data = data;

	return hmNode;
}

void openHashMapNodeDeconstruct(OpenHashMapNode* hmNode) {
	free(hmNode);
}
