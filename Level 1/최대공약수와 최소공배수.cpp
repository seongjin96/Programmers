/*
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;
    int r = 0, mul = n * m;
    while(m!=0){
        r = n % m;
        n = m;
        m = r;
    }
    answer.push_back(n);
    answer.push_back(mul / n);
    return answer;
}