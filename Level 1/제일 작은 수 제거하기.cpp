/*
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int min = arr.front();
    
    for(int i=0; i<arr.size(); i++){
        if(min > arr[i]){
            min = arr[i];
        }
    }
    
    for(int i=0; i<arr.size(); i++){
        if(arr[i] != min)
            answer.push_back(arr[i]);
    }
    if(answer.empty())
        answer.push_back(-1);
    
    return answer;
}