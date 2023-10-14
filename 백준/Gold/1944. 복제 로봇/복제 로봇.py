from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

node_point = {}

idx = 0
for r in range(n):
    for c in range(n):
        if arr[r][c]=="S":
            node_point[(r,c)]=idx
            idx+=1
        elif arr[r][c]=="K":
            node_point[(r,c)]=idx
            idx+=1
            
def bfs(r,c):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q =  deque()
    q.append((r,c,0))
    node = node_point[(r,c)]
    visited[r][c] = True
    while q:
        now_r,now_c,now_distance = q.popleft()
        if arr[now_r][now_c]=='S' or arr[now_r][now_c]=='K':
            next_node = node_point[(now_r,now_c)]
            if now_distance!=0 and (next_node,node,now_distance) not in graph:
                graph.add((node,next_node,now_distance))
            
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            next_r,next_c = now_r+dr,now_c+dc
            if next_r<0 or next_r>=n or next_c<0 or next_c>=n:
                continue
            if not visited[next_r][next_c] and arr[next_r][next_c]!='1':
                visited[next_r][next_c] = True
                q.append((next_r,next_c,now_distance+1))
graph = set()

for r in range(n):
    for c in range(n):
        if arr[r][c] == "S" or arr[r][c]=="K":
            bfs(r,c)

graph = list(graph)
graph.sort(key=lambda x:x[2])

parent = [i for i in range(len(node_point))]

def find(x):
    if x==parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a==b:
        return False 
    if a>b:
        parent[a]=b

    elif a<b:
        parent[b]=a
        
    return True
        
answer = 0
for n1,n2,distance in graph:
    if union(n1,n2):
        answer+=distance

flag = parent[0]

for i in range(1,len(parent)):
    if parent[i]!=flag:
        answer=-1
        break
print(answer)