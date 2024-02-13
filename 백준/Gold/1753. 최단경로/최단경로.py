import sys
from heapq import heappush, heappop

input = sys.stdin.readline

v, e = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(start):
    q = []
    distance = [float('inf')] * (v + 1)
    distance[start] = 0
    heappush(q, (0, start))
    
    while q:
        curr_dist, curr_node = heappop(q)

        if curr_dist > distance[curr_node]:
            continue

        for next_node, weight in graph[curr_node]:
            next_dist = curr_dist + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(q, (next_dist, next_node))
                
    return distance

distances = dijkstra(start_node)
for dist in distances[1:]:
    print(dist if dist != float('inf') else 'INF')