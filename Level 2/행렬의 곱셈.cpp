/*
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    answer.resize(arr1.size());
    for(int i=0; i<answer.size(); i++){
        answer[i].resize(arr2[0].size());
    }

    for(int i=0; i<arr1.size(); i++){
        for(int j=0; j<arr2[0].size(); j++){
            for(int k=0; k<arr1[0].size(); k++){
                answer[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }
    return answer;
}