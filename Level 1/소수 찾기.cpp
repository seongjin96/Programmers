/*
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
*/

#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<bool> v(n+1);
    for(int i=0; i<n; i++)
        v.push_back(false);
    v[0] = v[1] = true;
    for(int i=2; i<sqrt(n); i++){
        if(!v[i]){
            for(int j=i+i; j<=n; j+=i)
                v[j] = true;
        }
    }
    for(int i=1; i<=n; i++){
        if(!v[i]) answer++;
    }
    return answer;
}