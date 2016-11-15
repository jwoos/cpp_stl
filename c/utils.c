#include "utils.h"

void flush() {
	writeStdout("\n", 1);
}

void printError(char* message, int shouldExit) {
	perror(message);

	if (shouldExit) {
		_exit(EXIT_FAILURE);
	}
}

void writeStdout(char* message, int bytes) {
	if (write(STDOUT_FILENO, message, bytes) < 0) {
		printError("error writing - exiting", 1);
	}
}

// don't use this - use printError or perror
void writeStderr(char* message, int bytes) {
	if (write(STDERR_FILENO, message, bytes) < 0) {
		printError("error writing - exiting", 1);
	}
}

void freeArray(void** arr, int size) {
	for (int i = 0; i < size; i++) {
		free(arr[i]);
	}

	free(arr);
}
