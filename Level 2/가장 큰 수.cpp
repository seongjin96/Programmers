/*
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string &s1, string &s2){
    return s1 + s2 > s2 + s1;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    for(int i=0; i<numbers.size(); i++)
        v.push_back(to_string(numbers[i]));
    
    sort(v.begin(), v.end(), compare);
    
    if(v.front() == "0")
        answer = "0";
    else{
        for(int j = 0; j < v.size(); j++)
            answer += v[j];
    }
    return answer;
}