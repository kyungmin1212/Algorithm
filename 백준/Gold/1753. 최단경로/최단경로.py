import sys
from heapq import heappush,heappop

input  = sys.stdin.readline

v,e = map(int,input().split())

start_node = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    

def dijstra(start):
    q = []
    answer = [float('inf') for _ in range(v+1)]
    heappush(q,(0,start))
    while q:

        now_weight,now_node = heappop(q)
        if answer[now_node]==float('inf'):
            answer[now_node]=now_weight
        else:
            continue
        
        for next_node,weight in graph[now_node]:
            if answer[next_node]==float('inf'):
                heappush(q,(now_weight+weight,next_node))
                
    return answer

answer = [item if item!=float('inf') else 'INF' for item in dijstra(start_node)]
for item in answer[1:]:
    print(item)
