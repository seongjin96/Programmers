/*
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
*/

#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    for (int i = 0; i < s.length(); i++)
    {
        if (st.empty() && s[i] == ')')
            return false;
        else if (s[i] == '(')
            st.push(s[i]);
        else
            st.pop();
    }
    if (!st.empty())
        answer = false;
    return answer;
}