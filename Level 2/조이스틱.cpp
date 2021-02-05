/*
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
조이스틱을 각 방향으로 움직이면 아래와 같습니다.
    ▲ - 다음 알파벳
    ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
    ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
    ▶ - 커서를 오른쪽으로 이동
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
*/

#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    string temp = "";
    int idx = 0, Lidx = 0, Ridx = 0, Ldistance = 0, Rdistance = 0; 
    for(int i=0; i<name.size(); i++) temp += 'A';
    while(1){
        if(name[idx] - temp[idx] <= 13) answer += name[idx] - temp[idx];
        else answer += 26 - (name[idx] - temp[idx]);
        temp[idx] = name[idx];
        if(temp == name) break;
        Lidx = Ridx = idx;
        
        while(1){
            if(name[Ridx] != temp[Ridx]) break;
            Rdistance++;
            Ridx++;
        }
        while(1){
            if(Lidx < 0) Lidx = name.length() - 1;
            if(name[Lidx] != temp[Lidx] || Ldistance > Rdistance) break;
            Ldistance++;
            Lidx--;
        }
        if(Rdistance <= Ldistance){
            answer += Rdistance;
            idx = Ridx;
        }
        else{
            answer += Ldistance;
            idx = Lidx;
        }
        Ldistance = Rdistance = 0;
    }
    
    return answer;
}