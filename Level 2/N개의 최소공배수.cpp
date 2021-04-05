/*
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
*/

#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b)
{
    int c;
    while (b != 0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}

int solution(vector<int> arr)
{
    int answer = 0;
    int num1 = 0, num2 = 0;
    while (arr.size() != 1)
    {
        num1 = arr.back();
        arr.pop_back();
        num2 = arr.back();
        arr.pop_back();
        arr.push_back(lcm(num1, num2));
    }
    answer = arr[0];
    return answer;
}