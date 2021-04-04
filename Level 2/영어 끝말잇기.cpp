#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<int> solution(int n, vector<string> words)
{
    vector<int> answer;
    multiset<string> ms;
    ms.insert(words[0]);
    for (int i = 1; i < words.size(); i++)
    {
        ms.insert(words[i]);
        if (words[i - 1][words[i - 1].length() - 1] != words[i][0] || ms.count(words[i]) == 2)
        {
            answer.push_back(i % n + 1);
            answer.push_back(i / n + 1);
            return answer;
        }
    }
    answer.push_back(0);
    answer.push_back(0);

    return answer;
}