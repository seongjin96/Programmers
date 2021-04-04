/*
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;
    int first = 0;

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < scoville.size(); i++)
        pq.push(scoville[i]);
    while (pq.top() < K)
    {
        if (pq.size() < 2)
            break;
        first = pq.top();
        pq.pop();
        pq.push(first + pq.top() * 2);
        pq.pop();
        answer++;
    }
    if (pq.top() < K)
        return -1;
    return answer;
}