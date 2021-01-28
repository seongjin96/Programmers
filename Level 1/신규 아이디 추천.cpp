/*
신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, 
네오가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.
*/

#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    vector<char> v;
    for(int i = 0; i< new_id.length(); i++){
        if((new_id[i] >= 97 && new_id[i] <= 122 ) || new_id[i] >= 48 && new_id[i] <= 57)
            v.push_back(new_id[i]);
        else if(new_id[i] >= 65 && new_id[i] <= 90){
            v.push_back(tolower(new_id[i]));
        }
        else if(new_id[i] == '-' || new_id[i] == '_'){
            v.push_back(new_id[i]);
        }
        else if(!v.empty() && new_id[i] == '.'){
            if(v.back() != '.')
                v.push_back(new_id[i]);
        }
    }
    if(v.empty()){
        v.push_back('a');
    }
    if(v.size() >= 16){
        while(v.size() > 15){
            v.pop_back();
        }
    }
    if(v.back() == '.')
        v.pop_back();
    if(v.size() <= 2){
        for(int i=v.size(); i<3; i++){
            v.push_back(v.back());
        }
    }
    
    for(int i=0; i<v.size(); i++){
        answer += v[i];
    }
    return answer;
}