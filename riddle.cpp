#include <iostream>
#include <string>

void Next1() {
    int answer;
    std::cout << "Which year did America gain independence?\n1. 1776 2. 1774 3. 1800 4. IDK ";
    std::cin >> answer;
    switch (answer) {
    case 1:
        std::cout << "Correct!\nCongratulations! You win!" <<std::endl;
        exit(0);
    case 4:
        std::cout << "Answer: 1776" <<std::endl;
        exit(0);
    default:
        if (answer != 4) {
            std::cout << "Wrong!" <<std::endl;
            exit(0);
        }
    }
}

int main() {
    int answer;
    std::cout << "What is the closest to milky way?\n1. Andromeda 2. Whirpool galaxy 3. IDK ";
    std::cin >> answer;
    switch (answer) {
    case 1:
        std::cout << "Correct!" <<std::endl;
        Next1();
    case 3:
        std::cout << "Answer: andromeda galaxy." <<std::endl;
        exit(0);
    default:
        if (answer != 3) {
            std::cout << "Wrong!" <<std::endl;
            exit(0);
        };
    };
    return 0;
}
