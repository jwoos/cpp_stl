CC = gcc
CFLAGS = -Wall -Wextra -std=gnu11 -ggdb -O0
LDLIBS =
LDFLAGS =

UNUSED = graph.o tree/binary-search.o

# implicit rule for %.o
# $(CC) $(CPPFLAGS) $(CFLAGS) -c $@
OBJECTS = utils.o \
		  linked-list/double.o linked-list/single.o \
		  vector.o \
		  hash-map/closed.o hash-map/open.o

default: clean datastructures

datastructures: ${OBJECTS}
	$(CC) datastructures.c $^ $(LDFLAGS) $(LDLIBS) -o $@

debug: default
	valgrind --leak-check=full -v ./datastructures

clean:
	touch ${OBJECTS} datastructures && rm ${OBJECTS} datastructures
