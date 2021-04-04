/*
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

string solution(string s)
{
    string answer = s;
    if (answer[0] >= 'a' && answer[0] <= 'z')
        answer[0] -= 32;
    for (int i = 1; i < answer.length(); i++)
    {
        if (answer[i - 1] == ' ' && (answer[i] >= 'a' && answer[i] <= 'z'))
            answer[i] -= 32;
        else if (answer[i - 1] != ' ' && (answer[i] >= 'A' && answer[i] <= 'Z'))
            answer[i] += 32;
    }
    return answer;
}