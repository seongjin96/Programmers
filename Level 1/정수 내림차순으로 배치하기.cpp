/*
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
*/

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(long long n) {
    long long answer = 0;
    vector<int> v;
    while(n!=0){
        v.push_back(n%10);
        n/=10;
    }
    sort(v.rbegin(), v.rend());
    answer = v[0];
    for(int i=1; i<v.size(); i++){
        answer *= 10;
        answer += v[i];
    }
    
    return answer;
}