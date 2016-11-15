#ifndef DSA_UTILS_H
#define DSA_UTILS_H

#include <unistd.h>

void flush();

void printError(char*, int);

void writeStdout(char*, int);

// don't use this - use printError or perror
void writeStderr(char*, int);

void freeArray(void**, int);

#endif
