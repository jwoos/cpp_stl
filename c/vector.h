/*
 * dynamic array
 */

typedef struct Vector {
	int size;
	int capacity;
	int* arr;
} Vector;

Vector* initializeVector();

void deconstructVector(Vector*);

void printVector(const Vector*);

void pushVector(Vector*, int);

int popVector(Vector*);

int getVector(const Vector*, int);

void setVector(Vector*, int, int);

void insertVector(Vector*, int, int);

void deleteVector(Vector*, int);

void clearVector(Vector*);
