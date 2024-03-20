n = int(input())

w = [list(map(int,input().split())) for _ in range(n)]

dp = [[None for _ in range(n)] for _ in range(1<<n)]

def find(mask,last):
    if dp[mask][last] != None:
        return dp[mask][last]
    
    if mask==(1<<n)-1: # 모든 도시를 방문했다면 처음 출발 도시인 0으로 돌아가면됨
        if w[last][0]>0:
            return w[last][0]
        else: # 만약 돌아가는 길이 없다면 무한대를 반환하기 
            return int(1e9)
    
    temp = int(1e9)
    for i in range(n):
        if mask&(1<<i)==0 and w[last][i]!=0:
            temp = min(temp,find(mask|(1<<i),i)+w[last][i])
    
    dp[mask][last] = temp
    return dp[mask][last]
    
print(find(1,0))