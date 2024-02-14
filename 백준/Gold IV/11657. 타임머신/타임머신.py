n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))

inf = int(1e9)
distance = [inf for _ in range(n+1)]

def bellman(start):
    distance[start] = 0
    
    for i in range(n):
        for node in range(1,n+1):
            if distance[node]!=inf:
                for next_node,weight in graph[node]:
                    if distance[next_node]>distance[node]+weight:
                        distance[next_node]=distance[node]+weight
                        
                        if i==n-1:
                            return False
    return True
    

if bellman(1):
    for i in range(2,n+1):
        if distance[i]!=inf:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)