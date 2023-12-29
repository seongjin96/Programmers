'''
보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 
board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.
'''

board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1

def solution(board, h, w):
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    n = len(board[0])
    count = 0

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if h_check < 0 or h_check >= n or w_check < 0 or w_check >= n:
            continue
        if board[h][w] == board[h_check][w_check]:
            count += 1

    return count

print(solution(board, h, w))