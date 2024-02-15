def move_red(r_r, r_c, b_r, b_c, count, r_complete, b_complete):
    if r_complete and b_complete:
        answer.append(count)
        return
    elif r_complete:
        move_blue(r_r,r_c,b_r,b_c,count,r_complete,b_complete,False,-1,-1)
        blue_check[b_r][b_c]=0
        return
        
    red_check[r_r][r_c]=1
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        next_r = r_r+dr
        next_c = r_c+dc
        if next_r<0 or next_c<0 or next_r>=max_row or next_c>=max_column:
            continue
        
        if red_check[next_r][next_c]==0: # 먼저 갈 수 있는 곳이여야합니다.
            if b_complete: # b가 완료된 상태라면 b로 갈수없습니다.
                if (next_r==b_r and next_c==b_c):
                    continue
                else:
                    if next_r==red_end[0] and next_c==red_end[1]:
                        move_blue(next_r,next_c,b_r,b_c,count,True,b_complete,False,-1,-1)
                        blue_check[b_r][b_c]=0                        
                    else:
                        move_blue(next_r,next_c,b_r,b_c,count,r_complete,b_complete,False,-1,-1)
                        blue_check[b_r][b_c]=0
            else: # b가 완료되지 않았으므로 b쪽으로 이동가능합니다. 대신 교환처리를 안되게 하기 위해 before값을  저장해줍니다
                if (next_r==b_r and next_c==b_c):
                    if next_r==red_end[0] and next_c==red_end[1]:
                        move_blue(next_r,next_c,b_r,b_c,count,True,b_complete,True,r_r,r_c)
                        blue_check[b_r][b_c]=0                        
                    else:
                        move_blue(next_r,next_c,b_r,b_c,count,r_complete,b_complete,True,r_r,r_c)
                        blue_check[b_r][b_c]=0
                else:
                    if next_r==red_end[0] and next_c==red_end[1]:
                        move_blue(next_r,next_c,b_r,b_c,count,True,b_complete,False,-1,-1)
                        blue_check[b_r][b_c]=0
                    else:
                        move_blue(next_r,next_c,b_r,b_c,count,r_complete,b_complete,False,-1,-1)
                        blue_check[b_r][b_c]=0
                
        
def move_blue(r_r,r_c,b_r,b_c,count,r_complete,b_complete,flag, bf_r_r, bf_r_c):
    if r_complete and b_complete:
        answer.append(count+1)
        return
    elif b_complete:
        move_red(r_r,r_c,b_r,b_c,count+1,r_complete,b_complete)
        red_check[r_r][r_c]=0
        return
        
    blue_check[b_r][b_c]=1
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        next_r = b_r+dr
        next_c = b_c+dc
        if next_r<0 or next_c<0 or next_r>=max_row or next_c>=max_column:
            continue
            
        if next_r==blue_end[0] and next_c==blue_end[1] and (next_r!=r_r or next_c!=r_c):
            if flag and (next_r==bf_r_r and next_c==bf_r_c):
                continue
            move_red(r_r,r_c,next_r,next_c,count+1,r_complete,True)
            red_check[r_r][r_c]=0
        elif blue_check[next_r][next_c]==0:
            if flag and (next_r==bf_r_r and next_c==bf_r_c):
                continue

            if (next_r!=r_r or next_c!=r_c): # 같은 곳으로 이동하면 안됨.
                move_red(r_r,r_c,next_r,next_c,count+1,r_complete,b_complete)
                red_check[r_r][r_c]=0

            
def solution(maze):
    global blue_check, red_check, max_row, max_column, answer,red_end, blue_end
    answer =[]
    
    max_row = len(maze)
    max_column = len(maze[0])
    
    red_start = [-1,-1]
    red_end = [-1,-1]
    blue_start = [-1,-1]
    blue_end = [-1,-1]
    
    blue_check = [[0 for _ in range(max_column)] for _ in range(max_row)]
    red_check = [[0 for _ in range(max_column)] for _ in range(max_row)]
    
    for row in range(max_row):
        for column in range(max_column):
            if maze[row][column]==1:
                red_start = [row,column]
                
            elif maze[row][column]==2:
                blue_start = [row,column]
                
            elif maze[row][column]==3:
                red_end = [row,column]
                
            elif maze[row][column]==4:
                blue_end = [row,column]
                
            elif maze[row][column]==5:
                red_check[row][column]=1
                blue_check[row][column]=1
                
    move_red(red_start[0], red_start[1], blue_start[0], blue_start[1], 0, False, False)

    if answer==[]:
        return 0
    else:
        return min(answer)
