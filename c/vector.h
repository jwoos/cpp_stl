#ifndef VECTOR_H
#define VECTOR_H

/*
 * dynamic array
 */

typedef struct Vector {
	int size;
	int capacity;
	int* arr;
} Vector;

Vector* vectorInitialize();

void vectorDeconstruct(Vector*);

void vectorPrint(const Vector*);

void vectorPush(Vector*, int);

int vectorPop(Vector*);

int vectorGet(const Vector*, int);

void vectorSet(Vector*, int, int);

void vectorInsert(Vector*, int, int);

void vectorDelete(Vector*, int);

void vectorClear(Vector*);

#endif
