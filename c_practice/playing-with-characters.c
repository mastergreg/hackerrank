#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef MAX_LEN
#define MAX_LEN 100
#endif

int main(int argc, char **argv) {
  char line[MAX_LEN];

  for (int i = 0; i < 3; i++) {
    scanf("%[^\n]%*c", line);
    printf("%s\n", line);
  }
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
}