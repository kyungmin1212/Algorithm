from collections import deque
from copy import deepcopy

def solution(maps):
    
    n_rows = len(maps)
    n_columns = len(maps[0])
    
    visited=[[0 for _ in range(n_columns)] for _ in range(n_rows)]
    for row in range(n_rows):
        for column in range(n_columns):
            if maps[row][column]=="S":
                start_point = [row,column]
            elif maps[row][column]=="E":
                end_point = [row,column]
            elif maps[row][column]=="L":
                lever_point = [row,column]
            elif maps[row][column]=="X":
                visited[row][column]=1
                
    q = deque([start_point+[0]])
    copy_visited = deepcopy(visited)
    
    lever_flag = False
    answer = 0
    while q:
        now_r,now_c,now_distance = q.popleft()
        if now_r==lever_point[0] and now_c==lever_point[1]:
            lever_flag=True
            answer+=now_distance
            break
        
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            next_r = now_r+dr
            next_c = now_c+dc
            if next_r<0 or next_c<0 or next_r>=n_rows or next_c>=n_columns:
                continue
                
            if copy_visited[next_r][next_c]==0:
                q.append([next_r,next_c,now_distance+1])
                copy_visited[next_r][next_c]=1
                
    if not lever_flag:
        return -1
    
    q = deque([lever_point+[0]])
    copy_visited = deepcopy(visited)
    
    end_flag = False
    while q:
        now_r,now_c,now_distance = q.popleft()
        if now_r==end_point[0] and now_c==end_point[1]:
            end_flag=True
            answer+=now_distance
            break
        
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            next_r = now_r+dr
            next_c = now_c+dc
            if next_r<0 or next_c<0 or next_r>=n_rows or next_c>=n_columns:
                continue
                
            if copy_visited[next_r][next_c]==0:
                q.append([next_r,next_c,now_distance+1])
                copy_visited[next_r][next_c]=1    
    
    if not end_flag:
        return -1
    
    return answer