/*
특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
*/

#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<int> solution(string s)
{
    vector<int> answer;
    vector<int> v;
    map<int, int> m;
    for (int i = 1; i < s.length(); i++)
    {
        string num = "";
        if (s[i] == '{' || s[i] == ',')
        {
            while (s[i + 1] >= '0' && s[i + 1] <= '9')
            {
                num += s[i + 1];
                i++;
            }
            if (s[i] >= '0' && s[i] <= '9')
                v.push_back(stoi(num));
        }
    }
    sort(v.begin(), v.end());
    int cnt = 1;
    for (int i = 0; i < v.size(); i++)
    {
        if (i == v.size() - 1)
            m.insert(pair<int, int>(cnt, v[i]));
        else
        {
            if (v[i] == v[i + 1])
            {
                cnt++;
                continue;
            }
            m.insert(pair<int, int>(cnt, v[i]));
            cnt = 1;
        }
    }
    for (auto it = m.rbegin(); it != m.rend(); it++)
        answer.push_back(it->second);
    return answer;
}