/*
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n)
{
    vector<int> answer;
    vector<vector<int>> v(n, vector<int>(n, 0));

    int size = n;
    int row = 1, col = 0;
    v[0][0] = 1;
    while (size > 1)
    {
        // 왼쪽 대각선 채우기
        for (int i = row; i < size; i++)
            if (v[i][col] == 0)
                v[i][col] = v[i - 1][col] + 1;
        // 마지막 줄 채우기
        for (int j = col + 1; j < size; j++)
            if (v[size - 1][j] == 0)
                v[size - 1][j] = v[size - 1][j - 1] + 1;
        // 오른쪽 대각선 채우기
        for (int k = size - 2; k > col; k--)
        {
            if (size == n && v[k][k] == 0)
                v[k][k] = v[k + 1][k + 1] + 1;
            else if (v[k][k - col] == 0)
                v[k][k - col] = v[k + 1][k - col + 1] + 1;
        }
        row++;
        col++;
        size--;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= i; j++)
            answer.push_back(v[i][j]);
    return answer;
}