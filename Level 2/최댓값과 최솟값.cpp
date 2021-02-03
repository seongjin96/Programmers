/*
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수, solution을 완성하세요.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    string temp = "";
    vector<int> v;
    for(int i=0; i<s.length() + 1; i++){
        if(s[i] != ' ') temp += s[i];
        if(s[i] == ' ' || s[i] == '\0'){
            v.push_back(stoi(temp));
            temp = "";
        }
            
    }
    sort(v.begin(), v.end());
    
    answer = to_string(v.front()) + " " + to_string(v.back());
    
    return answer;
}