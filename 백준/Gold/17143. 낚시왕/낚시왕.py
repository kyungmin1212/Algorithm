from copy import deepcopy
import sys

input = sys.stdin.readline

R,C,M = map(int,input().split())

arr = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    r=r-1
    c=c-1
    arr[r][c] = [s,d,z]

answer = 0

def find_s_d(r,c,s,d):
    if d==1 or d==2: # 위쪽 or 아래쪽
        s = s%(2*(R-1))
        new_d = d
        for _ in range(s):
            if new_d ==1:
                if r==0:
                    r+=1
                    new_d=2
                else:
                    r-=1
            elif new_d ==2:
                if r==R-1:
                    r-=1
                    new_d=1
                else:
                    r+=1
    elif d==3 or d==4: # 왼쪽 or 오른쪽
        s = s%(2*(C-1))
        new_d = d
        for _ in range(s):
            if new_d ==4:
                if c==0:
                    c+=1
                    new_d=3
                else:
                    c-=1
            elif new_d ==3:
                if c==C-1:
                    c-=1
                    new_d=4
                else:
                    c+=1
    return (r,c,s,new_d)

for now_c in range(C):
    for i in range(R):
        if arr[i][now_c]!=[]:
            answer+=arr[i][now_c][2] #
            arr[i][now_c]=[]
            break
        
    new_arr = [[[] for _ in range(C)] for _ in range(R)]
    for n_r in range(R):
        for n_c in range(C):
            if arr[n_r][n_c]!=[]:
                
                n_s,n_d,n_z = arr[n_r][n_c] # s 속력 , d 방향, z 크기
                new_r,new_c,new_s,new_d = find_s_d(n_r,n_c,n_s,n_d)
                if new_arr[new_r][new_c]!=[]:
                    if new_arr[new_r][new_c][2]<n_z:
                        new_arr[new_r][new_c] = [new_s,new_d,n_z]
                    else:
                        continue
                else:
                    new_arr[new_r][new_c] = [new_s,new_d,n_z]
    arr = deepcopy(new_arr)
    
print(answer)