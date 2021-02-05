/*
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
*/

#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
	int idx = 0;
	int size = number.size() - k;
	for (int i = 0; i < size; i++) {
		char max = number[idx];
		int max_idx = idx;
		for (int j = idx; j <= k + i; j++) {
			if (max < number[j]) {
				max = number[j];
				max_idx = j;
			}
		}
		idx = max_idx + 1;
		answer += max;
	}
    
    return answer;
}