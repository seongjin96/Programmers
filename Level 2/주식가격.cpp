/*
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
*/

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    for(int i=0; i<prices.size(); i++){
        int low = 0;
        for(int k=i+1; k<prices.size();k++){
            low++;
            if(prices[i] > prices[k]){
                break;
            }
        }
        answer.push_back(low);
    }
    return answer;
}