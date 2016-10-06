WARNING = -Wall
DEBUG = -g
VERSION = -std=c++14
OPTIMIZE = -O0

ALL = List.o Vector.o utils.o

default: clean main

debug: default
	valgrind --leak-check=full -v ./main

main: ${ALL}
	$(CXX) ${VERSION} ${WARNING} ${OPTIMIZE} ${DEBUG} $@.cpp $^ -o $@
	./$@

List.o:
	$(CXX) ${VERSION} ${WARNING} ${OPTIMIZE} ${DEBUG} -c List.cpp -o $@

Vector.o:
	$(CXX) ${VERSION} ${WARNING} ${OPTIMIZE} ${DEBUG} -c Vector.cpp -o $@

utils.o:
	$(CXX) ${VERSION} ${WARNING} ${OPTIMIZE} ${DEBUG} -c utils.cpp -o $@

clean:
	rm ${ALL} main
