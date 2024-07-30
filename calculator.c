#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void addition();
void subtraction();
void multiplication();
void division();
void exponentation();
void squareroot();

int main() {
    char enter;
    printf("Enter an operator(+, -, *, /, p, t). q to exit. h for help. ");
    scanf("%c", &enter);
    if (enter=='q') {
        exit(0);
    }
    else if (enter=='h') {
        printf("+ does addition. - does subtraction. * does multiplication. / does division. p does exponentation. t does square root.");
    }
    switch(enter) {
    case '+':
        addition();
        exit(0);
    case '-':
        subtraction();
        exit(0);
    case '*':
        multiplication();
        exit(0);
    case '/':
        division();
        exit(0);
    case 'p':
        exponentation();
        exit(0);
    case 't':
        squareroot();
        exit(0);
    default:
        if (enter != 'h') {
            printf("\nInvalid operator.");
            exit(0);
        }
    }
    return 0;
}

void addition() {
    double number1;
    double number2;
    printf("First number: ");
    scanf("%lf", &number1);
    printf("Second number: ");
    scanf("%lf", &number2);
    printf("result: %lf", number1 + number2);
}

void subtraction() {
    double number1;
    double number2;
    printf("First number: ");
    scanf("%lf", &number1);
    printf("Second number: ");
    scanf("%lf", &number2);
    printf("result: %lf", number1 - number2);
}

void multiplication() {
    double number1;
    double number2;
    printf("First number: ");
    scanf("%lf", &number1);
    printf("Second number: ");
    scanf("%lf", &number2);
    printf("result: %lf", number1 * number2);
}

void division() {
    double number1;
    double number2;
    printf("First number: ");
    scanf("%lf", &number1);
    printf("Second number: ");
    scanf("%lf", &number2);
    printf("result: %lf", number1 / number2);
}

void exponentation() {
    double number1;
    double number2;
    printf("First number: ");
    scanf("%lf", &number1);
    printf("Second number: ");
    scanf("%lf", &number2);
    printf("result: %lf", pow(number1, number2));
}

void squareroot() {
    double number1;
    printf("number: ");
    scanf("%lf", &number1);
    printf("result: %lf", sqrt(number1));
}
