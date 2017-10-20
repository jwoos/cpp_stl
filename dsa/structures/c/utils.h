#ifndef DSA_UTILS_H
#define DSA_UTILS_H


#include <unistd.h>
#include <stdint.h>


void flush();

void printError(char*, int);

void writeStdout(char*, int);

// don't use this - use printError or perror
void writeStderr(char*, int);

void freeArray(void**, int);

uint64_t hashJDB2(unsigned char*);

uint64_t hashSBDM(unsigned char*);


#endif
