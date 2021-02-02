/*
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
    ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
*/

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 1;
    int num = 0;
    int bridge_weights = 0;
    vector<int> finish;
    queue<int> walk_bridge;
    vector<int> time;
    
    while(finish != truck_weights){
        answer++;
        if(bridge_weights + truck_weights[num] <= weight){
            walk_bridge.push(truck_weights[num]);
            bridge_weights = bridge_weights + truck_weights[num];
            time.push_back(0);
            num++;
        }
        for(int i=0; i<time.size(); i++){
            time[i]++;
            if(time[i] == bridge_length){
                finish.push_back(walk_bridge.front());
                bridge_weights = bridge_weights - walk_bridge.front();
                walk_bridge.pop();
            }
        }
    }
    return answer;
}