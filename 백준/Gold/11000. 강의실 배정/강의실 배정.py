import sys
from heapq import heappush,heappop

input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key=lambda x:x[0])
q = []

for start,end in arr:
    if not q or q[0]>start:
        heappush(q,end)
    else:
        if q[0]<=start:
            heappop(q)
            heappush(q,end)
print(len(q)) 