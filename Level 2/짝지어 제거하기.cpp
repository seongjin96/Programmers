/*
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string s)
{
    int answer = 0;
    vector<char> v;
    for (int i = 0; i < s.length(); i++)
    {
        if (v.empty())
            v.push_back(s[i]);
        else if (v.back() == s[i])
            v.pop_back();
        else
            v.push_back(s[i]);
    }
    if (v.empty())
        answer = 1;
    return answer;
}