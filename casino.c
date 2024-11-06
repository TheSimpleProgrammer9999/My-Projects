#include <stdio.h>
#include <stdlib.h>
// Thanks to GeeksForGeeks for the idea! And thanks to GeeksForGeeks and StackOverflow!

int maximum = 10;
int minimum = 1;

int randomNum(int min, int max) {
    for (int i = 0; i < 1; i++) {
        int rd_num = rand() % (max - min + 1) + min;
    }
}


// Main func
int main() {
    srand(time(NULL));

    int winNum = randomNum(1, 10);
    int num1 = randomNum(1, 10);
    int num2 = randomNum(1, 10);
    int num3 = randomNum(1, 10);

    printf("\nYou need all the numbers a %i to win the casino.", winNum);
    // generates random value for winNum, num, num2, and num3
    printf("\nnum1: %i\nnum2: %i\nnum3: %i", num1, num2, num3);

    if (num1 == winNum) {
        if (num2 == winNum) {
            if (num3 == winNum) {
                int money = randomNum(10, 100);
                printf("\nYou win! You get %i$!", money);
            }
            else {
                printf("\nYou lose.");
            }
        }
        else {
            printf("\nYou lose.");
        }
    }
    else {
        printf("\nYou lose.");
    }
    return 0;
}