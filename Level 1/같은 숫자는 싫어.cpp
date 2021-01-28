/*
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
*/

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    answer.push_back(arr[0]);
    for(auto i=1; i<arr.size(); i++){
        if(answer.back() != arr[i])
            answer.push_back(arr[i]);
    }

    return answer;
}