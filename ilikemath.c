#include <stdio.h>

/*
if((
(a * 0x7331deadbeef1337llu) 

& (b) | (93) 

== 0x7517cafebabe7157
{
	}LRMISETLVC$NAWUGFBOODARHYOCEMSJD{MGE	
*/

int main(void) {
	unsigned long long lol = (unsigned long long)'Z' + 3;
	unsigned long long res = 0x7517cafebabe7157;
	lol = 93;
	printf("%lld\n", lol);	
	printf("%lld\n", res);
	unsigned long long a = res & (~lol);
	printf("a: %lld\n", res & (~lol));
	unsigned long long pass1 = a/0x7331deadbeef1337llu;
	printf("a.5: %lld\n", (pass1+ 1)*0x7331deadbeef1337llu); 
	printf("a.5: %lld\n", (pass1)*0x7331deadbeef1337llu); 
	printf("a.5: %lld\n", (pass1 -1)*0x7331deadbeef1337llu); 
	printf("sadf: %lld\n", 0x7517cafebabe7157/0x7331deadbeef1337llu);

}