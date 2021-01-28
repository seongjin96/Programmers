/*
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int idx = 1;
    while(idx != n+1){
        if(n % idx == 0)
            answer += idx;
        idx++;
    }
    return answer;
}