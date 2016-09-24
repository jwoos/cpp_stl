WARNING = -Wall

ALL = linked-list.o

default: clean datastructures

debug: default
	valgrind --leak-check=full -v ./datastructures

datastructures: ${ALL}
	$(CC) ${WARNING} $@.c $^ -o $@
	./$@

linked-list.o:
	$(CC) ${WARNING} -c linked-list.c

clean:
	rm ${ALL} datastructures
