/*
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle)
{
    int answer = 0;
    int len = triangle.size();
    int dp[501][501] = {0};
    dp[0][0] = triangle[0][0];
    for (int i = 1; i < len; i++)
    {
        dp[i][0] = dp[i - 1][0] + triangle[i][0];
        dp[i][triangle[i].size() - 1] = dp[i - 1][triangle[i - 1].size() - 1] + triangle[i].back();
    }
    for (int i = 2; i < len; i++)
    {
        for (int j = 1; j < i; j++)
        {
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
        }
    }
    for (int i = 0; i < len; i++)
    {
        answer = max(answer, dp[len - 1][i]);
    }
    return answer;
}