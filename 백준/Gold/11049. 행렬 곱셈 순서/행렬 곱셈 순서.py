import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for sub_len in range(2,n+1):
    for start_idx in range(n-sub_len+1): # 스타트 인덱스
        
        end_idx = start_idx+sub_len-1
        dp[start_idx][end_idx]=float('inf')
        for k in range(start_idx,end_idx):
            dp[start_idx][end_idx] = min(dp[start_idx][end_idx],dp[start_idx][k]+dp[k+1][end_idx]+arr[start_idx][0]*arr[k][1]*arr[end_idx][1])

print(dp[0][n-1])