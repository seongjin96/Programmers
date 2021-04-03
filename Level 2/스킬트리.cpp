/*
선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때,
가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees)
{
    int answer = 0;
    for (int i = 0; i < skill_trees.size(); i++)
    {
        int index = 0;
        bool check = true;
        for (int j = 0; j < skill_trees[i].length(); j++)
        {
            int idx = skill.find(skill_trees[i][j]);
            if (idx == string::npos)
                continue;
            else if (idx == index)
                index++;
            else
            {
                check = false;
                break;
            }
        }
        if (check)
            answer++;
    }
    return answer;
}