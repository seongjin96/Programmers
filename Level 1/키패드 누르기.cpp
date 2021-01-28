/*
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
*/

#include <string>
#include <vector>
#include <utility>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    vector<pair<int, int>> v;
    for(int i=0; i<4; i++){
        for(int j=0; j<3; j++){
            v.push_back(pair<int, int>(i, j));
        }
    }
    
    int Lx = v[9].first, Ly = v[9].second;
    int Rx = v[11].first, Ry = v[11].second;
    int Ldistance = 0, Rdistance = 0;
    
    for(int i=0; i<numbers.size(); i++){
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
			answer += "L";
			Lx = v[numbers[i] - 1].first;
			Ly = v[numbers[i] - 1].second;
		}
		else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
			answer += "R";
			Rx = v[numbers[i] - 1].first;
			Ry = v[numbers[i] - 1].second;
		}
		else {
			if (numbers[i] == 0) {
				numbers[i] = 11;
			}
            
			Ldistance = abs(v[numbers[i] - 1].first - Lx) + abs(v[numbers[i] - 1].second - Ly);
			Rdistance = abs(v[numbers[i] - 1].first - Rx) + abs(v[numbers[i] - 1].second - Ry);

			if (Ldistance > Rdistance) {
				answer += "R";
				Rx = v[numbers[i] - 1].first;
				Ry = v[numbers[i] - 1].second;
			}
			else if (Ldistance < Rdistance) {
				answer += "L";
				Lx = v[numbers[i] - 1].first;
				Ly = v[numbers[i] - 1].second;
			}
			else {
				if (hand.compare("left") == 0) {
					answer += "L";
					Lx = v[numbers[i] - 1].first;
					Ly = v[numbers[i] - 1].second;
				}
				else {
					answer += "R";
					Rx = v[numbers[i] - 1].first;
					Ry = v[numbers[i] - 1].second;
				}
			}
			
		}
    }
    return answer;
}