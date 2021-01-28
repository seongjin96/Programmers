/*
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer_arr = {0, 0, 0};
    vector<int> answer;
    
    int arr1[] = {1, 2, 3 ,4, 5};
    int arr2[] = {2, 1, 2, 3, 2, 4, 2, 5};
    int arr3[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    int idx = 0, idx1 = 0, idx2 = 0, idx3 = 0;
    int size = answers.size();
    
    while(size--){
        if(idx1 >= 5)
            idx1 = 0;
        if(idx2 >= 8)
            idx2 = 0;
        if(idx3 >= 10)
            idx3 = 0;
        if(arr1[idx1] == answers[idx])
            answer_arr[0]++;
        if(arr2[idx2] == answers[idx])
            answer_arr[1]++;
        if(arr3[idx3] == answers[idx])
            answer_arr[2]++;
        idx++;
        idx1++;
        idx2++;
        idx3++;
    }
    
    int max = answer_arr[0];
    answer.push_back(1);
    for(int i=1; i<3; i++){
        if(max < answer_arr[i]){
            max = answer_arr[i];
            while(!answer.empty())
                answer.pop_back();
            answer.push_back(i+1);
        } else if(max == answer_arr[i]){
            answer.push_back(i+1);
        }
    }
    
    return answer;
}