/*
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
*/

#include <string>
#include <vector>

using namespace std;
vector<int> dp;
int fibonacci(int n){
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    if (dp[n] != -1)
        return dp[n];
    dp[n] = (fibonacci(n - 2) % 1234567) + (fibonacci(n - 1) % 1234567);
    return dp[n];
}

int solution(int n) {
    int answer = 0;
    dp.resize(n + 1, -1);
    answer = fibonacci(n) % 1234567;
    return answer;
}