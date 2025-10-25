#include <stdio.h>
int main(){
    int nilai;

scanf("%d" , &nilai);

if (nilai == 0) {
    printf("nol");
} else if (0 > nilai) {
    printf("negatif");
} else {
    printf("positif");
}
}