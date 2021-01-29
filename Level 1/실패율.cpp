/*
실패율은 다음과 같이 정의한다.
    - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<double,int> a, pair<double,int> b){
    if(a.first == b.first)
        return a.second < b.second;
    else
        return a.first > b.first;
            
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> v;
    int size = 0, cnt = 0;
    
    sort(stages.begin(), stages.end());
    
    while(N != 0){
        if(!stages.empty()){
            while(stages.back() >= N){
                size++;
                if(stages.back() == N) cnt++;
                stages.pop_back();
                if(stages.empty()) break;
            }
        }
        if(size == 0)
             v.push_back({0, N});
        else
            v.push_back({(double)cnt / (double)size, N});
        cnt = 0;
        N--;
    }
    sort(v.begin(), v.end(), compare);
    
    for(int i=0; i<v.size(); i++)
        answer.push_back(v[i].second);
    
    return answer;
}