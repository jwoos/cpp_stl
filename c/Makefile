WARNING = -Wall

ALL = linked-list.o vector.o

default: clean datastructures

debug: default
	valgrind --leak-check=full -v ./datastructures

datastructures: ${ALL}
	$(CC) ${WARNING} $@.c $^ -o $@
	./$@

linked-list.o:
	$(CC) ${WARNING} -c linked-list.c

vector.o:
	$(CC) ${WARNING} -c vector.c

clean:
	rm ${ALL} datastructures
