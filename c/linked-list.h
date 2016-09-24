/*
 * the Node is the actual list, I opted to wrap it in another struct
 * to avoid having to put the head/tail on each Node as that would be
 * highly inefficient. Also this way, other properties of the list as
 * a WHOLE can be recorded e.g. size
 */

// this should still be available
typedef struct Node {
	int data;
	struct Node* next;
} Node;

// Node wrapper
typedef struct List {
	Node* head;
	Node* tail;
	int size;
} List;

// done
List* initializeList(Node*);

Node* initializeNode(int, Node*);

void printList(List*);

void pushList(List*, int);

Node* popList(List*);

Node* getElementList(List*, int);

void setElementList(List*, int, int);

void insertList(List*, int, int);

void deleteList(List*, int);

void clearList(List*);
