from collections import defaultdict

def solution(edges):
    answer = []
    # 들어오는 간선이 0 개면 그건 연결노드
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    for a,b in edges:
        in_degree[b]+=1
        in_degree[a]+=0
        graph[a].append(b)
        
    node = -1
    for k , v in in_degree.items():
        if v==0 and len(graph[k])>=2:
            node = k
            break

    answer = [node,0,0,0]
    for start_node in graph[node]:
        # 나가는 노드가 2개면 8자
        # 나가는 노드가 1개면 도넛,막대,8자
        # 계속순환 해야함. (자기자신으로 돌아올때까지 2개나 0개가 없으면 그건 도넛)
        # 나가는 노드가 0개면 무조건 막대
        # start_node에서 dfs로 계속 들어가서 자기 자신으로 돌아오면 도넛
        
        now_node = start_node
        while True:
            if len(graph[now_node])==0:
                answer[2]+=1
                break
            if len(graph[now_node])==2:
                answer[3]+=1
                break
            now_node =graph[now_node][0]
            if now_node ==start_node:
                answer[1]+=1
                break

    return answer