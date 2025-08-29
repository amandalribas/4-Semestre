#include <stdio.h>
#include <stdlib.h>

int x = 1;
int retornaCinco() {
    x = x + 3;
    return 5;
}

int main() {
    int y;
    y = retornaCinco () + x;
    printf("%d\n",y);
    return 0;
}
