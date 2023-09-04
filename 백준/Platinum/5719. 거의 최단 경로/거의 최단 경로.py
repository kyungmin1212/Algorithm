from heapq import heappush,heappop
import sys
from collections import deque

input = sys.stdin.readline

def dijkstra(start,end):
    q=[]
    heappush(q,(0,start))
    
    while q:
        now_distance,now_node = heappop(q) # distance가 짧은거부터 나옴
        
        if now_distance>=distance[now_node]:
            continue
        
        distance[now_node]=now_distance
        
        if now_node == end:
            return now_distance

        for next_node,weight in graph[now_node].items():
            if distance[next_node]==inf:
                heappush(q,(now_distance+weight,next_node))
    return -1

def bfs(end_node):
    
    q = deque()
    q.append(end_node)
    
    while q:
        now_node = q.popleft()
        for before_node,weight in reverse_graph[now_node]:
            if distance[before_node]+weight==distance[now_node]:
                if now_node in graph[before_node]:
                    del graph[before_node][now_node]
                    q.append(before_node)


while True:
    n,m = map(int,input().split())
    
    if n==0 and m==0:
        break
    
    s,d = map(int,input().split())
    
    graph = [dict() for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a][b]=c
        reverse_graph[b].append((a,c))
    
    inf = float('inf')
    distance = [inf for _ in range(n)]
    dijkstra(s,d)
    bfs(d)
    distance = [inf for _ in range(n)]
    print(dijkstra(s,d))