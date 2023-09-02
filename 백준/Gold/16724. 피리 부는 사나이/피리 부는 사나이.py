n,m= map(int,input().split())

arr = [list(input()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
check_list = [[(-1,-1) for _ in range(m)] for _ in range(n)]
check_set = set()
def find(r,c):
    visited[r][c]=True
    
    flag = (-1,-1)
    if arr[r][c]=='D':
        if not visited[r+1][c]:
            flag = find(r+1,c)
        else:
            if check_list[r+1][c]==(-1,-1): # 방문했는데, safe zone설정이 안되어져 있는 경우
                flag = (r,c)
            else: # 방문했고, safe zone 설정이 되어져 있는 경우
                flag = check_list[r+1][c]

    elif arr[r][c]=='U':
        if not visited[r-1][c]:
            flag = find(r-1,c)
        else:
            if check_list[r-1][c]==(-1,-1): # 방문했는데, safe zone설정이 안되어져 있는 경우
                flag = (r,c)
            else: # 방문했고, safe zone 설정이 되어져 있는 경우
                flag = check_list[r-1][c]
    elif arr[r][c]=='L':
        if not visited[r][c-1]:
            flag = find(r,c-1)
        else:
            if check_list[r][c-1]==(-1,-1): # 방문했는데, safe zone설정이 안되어져 있는 경우
                flag = (r,c)
            else: # 방문했고, safe zone 설정이 되어져 있는 경우
                flag = check_list[r][c-1]
    elif arr[r][c]=='R':
        if not visited[r][c+1]:
            flag = find(r,c+1)
        else:
            if check_list[r][c+1]==(-1,-1): # 방문했는데, safe zone설정이 안되어져 있는 경우
                flag = (r,c)
            else: # 방문했고, safe zone 설정이 되어져 있는 경우
                flag = check_list[r][c+1]
    check_list[r][c] = flag
    return flag
answer = 0
for row in range(n):
    for column in range(m):
        if not visited[row][column]:
            ans_r,ans_c = find(row,column)
            if (ans_r,ans_c) not in check_set:
                answer+=1
                check_set.add((ans_r,ans_c))
print(answer)