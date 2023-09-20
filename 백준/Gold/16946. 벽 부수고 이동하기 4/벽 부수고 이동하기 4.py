import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(map(int,list(input().rstrip()))) for _ in range(n)]
origin_arr = deepcopy(arr)
answer = [[0 for _ in range(m)] for _ in range(n)]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    
    arr[r][c]=1
    ans = 0
    while q:
        now_r,now_c = q.popleft()
        area_number[now_r][now_c]=area_id
        ans +=1
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            next_r,next_c = now_r+dr,now_c+dc
            if next_r<0 or next_r>=n or next_c<0 or next_c>=m:
                continue
            if arr[next_r][next_c]==0:
                q.append((next_r,next_c))
                arr[next_r][next_c]=1
    return ans

area_number = [[0 for _ in range(m)] for _ in range(n)]
area_id = 1
area_id_count = {}

for r in range(n):
    for c in range(m):
        if arr[r][c]==0:
            area_id_count[area_id]=bfs(r,c)
            area_id+=1
            
# 1000x1000 = 1000000
for r in range(n):
    for c in range(m):
        if origin_arr[r][c]==0:
            continue
        
        check = set()
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            next_r,next_c = r+dr,c+dc
            if next_r<0 or next_r>=n or next_c<0 or next_c>=m:
                continue
            if origin_arr[next_r][next_c]==0:
                check.add(area_number[next_r][next_c])
        
        sub_ans = 0   
        for id in check:
            sub_ans+=area_id_count[id]
        answer[r][c] = (sub_ans+1)%10

for item in answer:
    for it in item:
        print(it,end='')
    print()