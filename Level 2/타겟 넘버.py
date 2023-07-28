'''
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
'''

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    graph = [0]

    for num in numbers:
        sub_graph = []
        for graph_num in graph:
            sub_graph.append(graph_num + num)
            sub_graph.append(graph_num - num)
        graph = sub_graph

    for num in graph:
        if num == target:
            answer += 1

    return answer

print(solution(numbers, target))