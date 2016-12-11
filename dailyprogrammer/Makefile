COMPILER = g++
WARNING = -Wall
STANDARD = -std=c++1y
DEBUG = -g
OPTIMIZATION = -O0
DIRECTORY = -I.
BASE = $(basename $(FILE))
FILE =
LINK =

default:
	$(COMPILER) ${WARNING} ${STANDARD} ${DEBUG} ${DIRECTORY} ${FILE} ${LINK} -o ${BASE}.out
	./${BASE}.out

# TODO: separate C and C++ targets
