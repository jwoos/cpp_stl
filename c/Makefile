WARNING = -Wall
DEBUG = -g
OPTIMIZE = -O0

ALL = linked-list.o vector.o bst.o

default: clean datastructures

debug: default
	valgrind --leak-check=full -v ./datastructures

datastructures: ${ALL}
	$(CC) ${WARNING} ${DEBUG} ${OPTIMIZE} $@.c $^ -o $@
	./$@

linked-list.o:
	$(CC) ${WARNING} ${DEBUG} ${OPTIMIZE} -c linked-list.c

vector.o:
	$(CC) ${WARNING} ${DEBUG} ${OPTIMIZE} -c vector.c

bst.o:
	$(CC) ${WARNING} ${DEBUG} ${OPTIMIZE} -c bst.c

clean:
	rm ${ALL} datastructures
