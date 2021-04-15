/*
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.
마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.
*/

#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> land)
{
    int answer = 0;
    vector<vector<int>> v(land.size(), vector<int>(4, 0));
    for (int i = 0; i < 4; i++)
        v[0][i] = land[0][i];
    for (int i = 1; i < land.size(); i++)
    {
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                if (j == k)
                    continue;
                v[i][j] = max(v[i][j], v[i - 1][k] + land[i][j]);
            }
        }
    }
    for (int i = 0; i < 4; i++)
        answer = max(answer, v[land.size() - 1][i]);
    return answer;
}