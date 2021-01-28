/*
 1.지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류로 이루어져 있다.
 2.전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 지도 1과 지도 2라고 하자. 
   지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 
   지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
 3.지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다.
 4.암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.
*/
#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<vector<string>> v(n, vector<string>(n, " "));
    string line = "";
    
    for(int i=0; i<n; i++){
        for(int j=n-1; j>=0; j--){
            if(arr1[i] % 2 == 1 || arr2[i] % 2 == 1)
                v[i][j] = '#';
            arr1[i] /= 2;
            arr2[i] /= 2;
        }
    }  
    for(int i=0; i<n; i++){
        line = "";
        for(int j=0; j<n; j++)
            line += v[i][j];
        answer.push_back(line);
    }
    return answer;
}