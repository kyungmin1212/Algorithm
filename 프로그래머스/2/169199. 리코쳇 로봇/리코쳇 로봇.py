def dfs(row,column,count,board):
    if row == end_point[0] and column ==end_point[1]: # 도착한 경우
        answer.append(count)
        return
    
    if visited[row][column]<=count:
        return
    
    visited[row][column] = count
    
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        before_r = row
        before_c = column
        while True:
            next_dr = before_r+dr
            next_dc = before_c+dc
            if next_dr<0 or next_dc<0 or next_dr>=n_row or next_dc>=n_column:
                break
            
            if board[next_dr][next_dc]=="D":
                break
                
            before_r = next_dr
            before_c = next_dc
            
        if before_r==row and before_c==column:
            continue
        else:
            dfs(before_r,before_c,count+1,board)
                

def solution(board):
    global end_point,answer,visited,n_row,n_column
    answer = []
    
    n_row = len(board)
    n_column = len(board[0])
    visited = [[float("inf") for _ in range(n_column)] for _ in range(n_row)]
    
    start_point = [-1,-1]
    end_point = [-1,-1]
    
    for row in range(n_row):
        for column in range(n_column):
            if board[row][column]=="R":
                start_point =[row,column]
            elif board[row][column]=='G':
                end_point =[row,column]
                
    dfs(start_point[0],start_point[1],0,board)
    if not answer:
        return -1
    else:
        return min(answer)