import sys

input = sys.stdin.readline

arr = [list(input()) for _ in range(10)]

answer = int(1e9)
for num in range(1<<10):
    turn = [[0 for _ in range(10)] for _ in range(10)]
    bin_num = bin(num)[2:]
    turn[0] = [0 for _ in range(10-len(bin_num))]+list(map(int,list(bin_num)))
    # turn = 1이면 그 위치는 스위치 클릭해야하는것

    for r in range(9):
        for c in range(10):
            if r==0:
                if c==0:
                    if arr[r][c]=='#':
                        if (turn[r][c]+turn[r][c+1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r][c]+turn[r][c+1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1                        
                elif c==9:
                    if arr[r][c]=='#':
                        if (turn[r][c]+turn[r][c-1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r][c]+turn[r][c-1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1    
                    
                else:
                    if arr[r][c]=='#':
                        if (turn[r][c]+turn[r][c-1]+turn[r][c+1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r][c]+turn[r][c-1]+turn[r][c+1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1       
            else:
                if c==0:
                    if arr[r][c]=='#':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c+1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c+1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1                        
                elif c==9:
                    if arr[r][c]=='#':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c-1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c-1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1    
                    
                else:
                    if arr[r][c]=='#':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c-1]+turn[r][c+1])%2==1:
                            turn[r+1][c]=1
                        else:
                            turn[r+1][c]=0
                    elif arr[r][c]=='O':
                        if (turn[r-1][c]+turn[r][c]+turn[r][c-1]+turn[r][c+1])%2==1:
                            turn[r+1][c]=0
                        else:
                            turn[r+1][c]=1 
    stop_flag = False                    
    for c in range(10):
        if c==0:
            if arr[9][c]=="#":
                if (turn[8][c]+turn[9][c]+turn[9][c+1])%2!=0:
                    stop_flag = True
                    break
            elif arr[9][c]=="O":
                if (turn[8][c]+turn[9][c]+turn[9][c+1])%2!=1:
                    stop_flag = True
                    break
        elif c==9:
            if arr[9][c]=="#":
                if (turn[8][c]+turn[9][c]+turn[9][c-1])%2!=0:
                    stop_flag = True
                    break
            elif arr[9][c]=="O":
                if (turn[8][c]+turn[9][c]+turn[9][c-1])%2!=1:
                    stop_flag = True
                    break
        else:
            if arr[9][c]=="#":
                if (turn[8][c]+turn[9][c]+turn[9][c-1]+turn[9][c+1])%2!=0:
                    stop_flag = True
                    break
            elif arr[9][c]=="O":
                if (turn[8][c]+turn[9][c]+turn[9][c-1]+turn[9][c+1])%2!=1:
                    stop_flag = True
                    break
    if not stop_flag:
        answer = min(answer,sum([sum(row) for row in turn]))

if answer==int(1e9):
    print(-1)
else:
    print(answer)