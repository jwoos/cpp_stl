CC = gcc
CFLAGS = -Wall -std=gnu11 -ggdb -O0
LDLIBS =

OBJECTS = single-linked-list.o vector.o bst.o graph.o

default: clean datastructures

debug: default
	valgrind --leak-check=full -v ./datastructures

datastructures: datastructures.c ${OBJECTS}
	./$@

clean:
	touch ${OBJECTS} datastructures && rm ${OBJECTS} datastructures
