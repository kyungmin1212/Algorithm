import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

sorted_arr = sorted(arr)

dp = []
index = [-1 for _ in range(n)]
length = 0
for i,(a,b) in enumerate(sorted_arr):
    if not dp or b>dp[-1]:
        dp.append(b)
        index[i] = length
        length+=1
    else:
        idx = bisect_left(dp,b)
        dp[idx] = b
        index[i] = idx

now_length = length-1

answer = []

for i in reversed(range(n)):
    if index[i]==now_length:
        now_length -=1
        continue
    else:
        answer.append(sorted_arr[i][0])

print(len(answer))
for item in sorted(answer):
    print(item)