def solution(n):
    answer = 0
    if n%2==1:
        return 0
    elif n==2:
        return 3
    
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    dp[2]=3

    for i in range(4,n+1,2):
        value = (dp[i-2]*3)%1000000007
        
        idx = i-4
        while idx>=0:
            value+=(dp[idx]*2)%1000000007
            value = value%1000000007
            idx-=2
        dp[i]=value
        
    return dp[n]