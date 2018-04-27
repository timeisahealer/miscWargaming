#include <stdio.h>
#include <stdlib.h>
int main(int argc, char ** argv) {
	int start = atoi(argv[1]);
	int end = atoi(argv[2]);
	FILE * fp = fopen(argv[3], "w");
	for(int i = start; i <= end; ++i) {
		fprintf(fp, "%d\n", i);
	}
	fclose(fp);

}
