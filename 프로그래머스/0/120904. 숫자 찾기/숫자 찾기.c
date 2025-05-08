int solution(int num, int k) {
    int digits[7];  // 최대 1,000,000이므로 최대 6자리 +1
    int len = 0;

    // num을 배열에 앞에서부터 저장
    int temp = num;
    while (temp > 0) {
        digits[len++] = temp % 10;
        temp /= 10;
    }

    // 배열을 뒤집어 앞자리부터 순서대로 확인
    for (int i = len - 1, pos = 1; i >= 0; i--, pos++) {
        if (digits[i] == k) return pos;
    }

    return -1;
}
