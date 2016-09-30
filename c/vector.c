#include <stdlib.h>
#include <stdio.h>

#include "vector.h"

static void increaseCapacity(Vector* vector) {
	vector -> capacity *= 2;

	vector -> arr = realloc(vector -> arr, sizeof(int) * (vector -> capacity));
}

Vector* initializeVector() {
	Vector* vector = malloc(sizeof(Vector));

	vector -> size = 0;
	vector -> capacity = 1;
	vector -> arr = malloc(sizeof(int));

	return vector;
}

void deconstructVector(Vector* vector) {
	free(vector -> arr);
	free(vector);

	vector = NULL;
}

void printVector(const Vector* vector) {
	for (int i = 0; i < vector -> size; i++) {
		printf("%d -> ", vector -> arr[i]);
	}

	printf("\n");
}

void pushVector(Vector* vector, int data) {
	if (vector -> size == vector -> capacity) {
		increaseCapacity(vector);
	}

	vector -> arr[vector -> size] = data;
	vector -> size++;
}

int popVector(Vector* vector) {
	vector -> size--;

	int data = vector -> arr[vector -> size];
	vector -> arr[vector -> size] = 0;

	return data;
}

int getVector(const Vector* vector, int index) {
	return vector -> arr[index];
}

void setVector(Vector* vector, int index, int data) {
	vector -> arr[index] = data;
}

void insertVector(Vector* vector, int index, int data) {
	if (vector -> size == vector -> capacity) {
		increaseCapacity(vector);
	}

	vector -> size++;

	for (int i = vector -> size - 1; i > index; i--) {
		vector -> arr[i] = getVector(vector, i - 1);
	}

	setVector(vector, index, data);
}

void deleteVector(Vector* vector, int index) {
	for (int i = index; i < vector -> size - 1; i++) {
		vector -> arr[i] = getVector(vector, i + 1);
	}

	vector -> size--;
}

void clearVector(Vector* vector) {
	free(vector -> arr);
	vector -> arr = malloc(sizeof(int));
	vector -> size = 0;
	vector -> capacity = 1;
}
