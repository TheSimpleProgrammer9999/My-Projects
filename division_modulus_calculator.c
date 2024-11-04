#include <stdio.h>
#include <math.h>

int main() {
    char operator;
    double divoperand1, divoperand2;
    int modoperand1, modoperand2;

    printf("Enter a operator(m is for modulus and d is for division): ");
    scanf("%c", &operator);

    switch (operator) {
        case 'd':
            printf("\nEnter operand 1: ");
            scanf("%lf", &divoperand1);
            printf("\nEnter operand 2: ");
            scanf("%lf", &divoperand2);
            double doubleans = divoperand1 / divoperand2;
            printf("\nThe quotient is: %lf", doubleans);
            break;

        case 'm':
            printf("\nEnter operand 1: ");
            scanf("%i", &modoperand1);
            printf("\nEnter operand 2: ");
            scanf("%i", &modoperand2);
            int modans = modoperand1 % modoperand2;
            printf("\nThe remainder is: %i", modans);
            break;
    }
    return 0;
}