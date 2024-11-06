#include <stdio.h>
#include <time.h>

// Source for delay function: GeeksForGeeks
void delay(double seconds) {
    double milliseconds = 1000 * seconds;
    clock_t start_time = clock();

    while (clock() < start_time + milliseconds) {
        ;
    }
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%i", &num);
    printf("\nCountdown starts now!\n");
    for (int i = num; i > 0; i--) {
        delay(1);
        printf("\n%i", i);
    }
    printf("\n\nCountdown finished!");
    return 0;
}