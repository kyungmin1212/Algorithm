import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [0]+list(map(int,input().split()))

def find(a):
    if a==parent[a]:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a==b:
        return
    elif a<b:
        parent[b]=a
        group_sum[a]+=group_sum[b] # 사탕 수
        group_count[a]+=group_count[b] # 인원수
    elif a>b:
        parent[a]=b
        group_sum[b]+=group_sum[a] # 사탕 수 
        group_count[b]+=group_count[a] # 인원수

parent = [i for i in range(n+1)]
group_sum = arr[:]
group_count = [1] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

groups = [(group_sum[i],group_count[i]) for i in range(1,n+1) if parent[i]==i and group_count[i]<k]

dp = [0 for _ in range(k)]

# 뒤에서부터 업데이트 해야지 
# dp가 하나로 처리가능
# 아니면 앞에거 업데이트 되면 뒤에거에 또 영향을 미치게 됨.
for candy_count,child_count in groups:
    for i in reversed(range(child_count,k)):
        dp[i] = max(dp[i],dp[i-child_count]+candy_count)
    
print(max(dp))
