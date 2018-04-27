#include <stdio.h>
#include <stdlib.h>

union Data {
   int i;
   char str[4];
};

int main(void) {
	union Data a;
	a.i = 100440000;
	for (int i = 0; i < 4; i++) {
		printf("%c", a.str[i]);
	}	

}
