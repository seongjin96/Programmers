/*
0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때,
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s)
{
    vector<int> answer(2, 0);
    if (s.length() == 1)
        return answer;
    else
        answer[0]++;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '0')
            answer[1]++;
    }
    int len = s.length() - answer[1];
    while (len != 1)
    {
        int length = 0;
        while (len > 0)
        {
            if (len % 2 == 0)
                answer[1]++;
            else
                length++;
            len /= 2;
        }
        answer[0]++;
        len = length;
    }
    return answer;
}