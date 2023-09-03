from collections import deque

n,m = map(int,input().split())

indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)

q = deque()

def topology_sort():
    result = []
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now_node = q.popleft()
        result.append(now_node)

        for next_node in graph[now_node]:
            indegree[next_node]-=1
            if indegree[next_node]==0:
                q.append(next_node)
    
    return result

print(*topology_sort())
