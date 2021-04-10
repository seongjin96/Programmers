/*
가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래,
즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles)
{
    int dp[101][101];
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
            dp[i][j] = 1;
    }
    for (int i = 0; i < puddles.size(); i++)
    {
        dp[puddles[i][1]][puddles[i][0]] = 0;
        if (puddles[i][0] == 1)
        {
            for (int j = puddles[i][1]; j <= n; j++)
                dp[j][1] = 0;
        }
        if (puddles[i][1] == 1)
        {
            for (int j = puddles[i][0]; j <= m; j++)
                dp[1][j] = 0;
        }
    }

    for (int i = 2; i <= m; i++)
    {
        for (int j = 2; j <= n; j++)
        {
            if (dp[j][i] != 0)
                dp[j][i] = (dp[j - 1][i] + dp[j][i - 1]) % 1000000007;
        }
    }
    return dp[n][m];
}