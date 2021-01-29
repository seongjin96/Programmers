/*
부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 
최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
*/

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(), d.end());
    int sum = 0;
    for(int i=0; i<d.size(); i++){
        sum += d[i];
        if(sum > budget)
            break;
        else
            answer++;
    }
    return answer;
}