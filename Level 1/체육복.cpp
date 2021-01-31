/*
전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
    - 전체 학생의 수는 2명 이상 30명 이하입니다.
    - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
    - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
      남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
*/

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> students(n, 1);
    for(int i=0; i<lost.size(); i++)
        students[lost[i] - 1]--;
    for(int i=0; i<reserve.size(); i++)
        students[reserve[i] - 1]++;
    for(int i=0; i<n; i++){
        if(students[i] == 0){
            if(i > 0 && students[i - 1] == 2){
                students[i - 1]--;
                students[i]++;
            }else if(i < n-1 && students[i + 1] == 2){
                students[i + 1]--;
                students[i]++;
            }
        }

    }
    for(int i=0; i<students.size(); i++){
        if(students[i] > 0) answer++;
    }
    return answer;
}