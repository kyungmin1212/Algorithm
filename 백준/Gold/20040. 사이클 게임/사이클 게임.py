import sys

input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n)]

def find(a):
    if a==parent[a]:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):

    a = find(a)
    b = find(b)

    if a==b:
        return True
    elif a>b: # 작은게 부모
        parent[a]=b
    elif a<b:
        parent[b]=a
    return False

for i in range(m):
    a,b= map(int,input().split())
    if union(a,b):
        print(i+1)
        exit()
print(0)