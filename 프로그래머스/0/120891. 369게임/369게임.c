#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int order) {
    int answer = 0;
    while (order > 0) {
        int digit = order % 10;
        if (digit == 3 || digit == 6 || digit == 9) {
            answer++;
        }
        order /= 10;
    }
    return answer;
}
