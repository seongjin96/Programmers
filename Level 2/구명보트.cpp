/*
사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
	int sum = 0;
	int idx = 0;
	int size = people.size();
	sort(people.begin(), people.end());

	while (idx <= size / 2) {
		if (people[idx] + people.back() <= limit) {
			idx++;
		}
		people.pop_back();
		answer++;
        if (people.back() <= limit / 2) {
			answer += (people.size() - idx + 1) / 2;
			break;
		}
	}
    
    return answer;
}