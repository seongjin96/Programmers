/*
전화번호가 문자열 phone_number로 주어졌을 때, 
전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
*/

#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    for(int i=0; i<phone_number.length()-4; i++){
        answer += "*";
    }
    for(int i= phone_number.length()-4; i< phone_number.length(); i++){
        answer += phone_number[i];
    }
    return answer;
}