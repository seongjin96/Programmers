def solution(rows, columns, queries):
    answer = []
    matrix = []
    
    for i in range(rows):
        arr = []
        for j in range(1, columns+1):
            arr.append(columns * i + j)
        matrix.append(arr)
    
    for idx in range(len(queries)):
        a_x = queries[idx][0] - 1
        a_y = queries[idx][1] - 1
        b_x = queries[idx][2] - 1
        b_y = queries[idx][-1] - 1

        min_list = [matrix[a_x][a_y]]
        for i in range(a_y, b_y):
            tmp = matrix[a_x][i+1]
            matrix[a_x][i+1] = matrix[a_x][a_y]
            matrix[a_x][a_y] = tmp
            min_list.append(tmp)
        
        for i in range(a_x, b_x):
            tmp = matrix[i+1][b_y]
            matrix[i+1][b_y] = matrix[a_x][a_y]
            matrix[a_x][a_y] = tmp
            min_list.append(tmp)
        
        for i in range(b_y, a_y, -1):
            tmp = matrix[b_x][i-1]
            matrix[b_x][i-1] = matrix[a_x][a_y]
            matrix[a_x][a_y] = tmp
            min_list.append(tmp)
        
        for i in range(b_x, a_x, -1):
            tmp = matrix[i-1][a_y]
            matrix[i-1][a_y] = matrix[a_x][a_y]
            matrix[a_x][a_y] = tmp
            min_list.append(tmp)

        answer.append(min(min_list))
        min_list.clear()
        
    return answer