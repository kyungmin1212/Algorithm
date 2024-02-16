def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    # 계산횟수
    
    for i,matrix in enumerate(matrix_sizes):
        dp[i][i]=0
        
    for m_l in range(2,n+1):
        for s_idx in range(0,n-m_l+1):
            for k in range(1,m_l):
                dp[s_idx][s_idx+m_l-1]= min(dp[s_idx][s_idx+m_l-1],dp[s_idx][s_idx+(k-1)]+dp[s_idx+k][s_idx+m_l-1]+matrix_sizes[s_idx][0]*matrix_sizes[s_idx+(k-1)][1]*matrix_sizes[s_idx+m_l-1][1])
    
    return int(dp[0][n-1])