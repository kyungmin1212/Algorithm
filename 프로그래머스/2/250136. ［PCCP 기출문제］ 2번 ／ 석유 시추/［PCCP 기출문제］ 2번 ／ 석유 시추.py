import sys

sys.setrecursionlimit(int(1e6))

def find(i,j,check,land):
    global sub_sum
    
    n = len(check_num)
    m = len(check_num[0])
    
    check_num[i][j]=check
    sub_sum+=1
    
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        next_i = i+dx
        next_j = j+dy
        if next_i<0 or next_j<0 or next_i>=n or next_j>=m or check_num[next_i][next_j]!=-1:
            continue
        else:
            if land[next_i][next_j]==1:
                find(next_i,next_j,check,land)

                
def solution(land):
    global check_num,sub_sum

    n = len(land)
    m = len(land[0])
    check_num = [[-1 for _ in range(m)] for _ in range(n)]
    check = 0
    sum_dict = dict()
    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and check_num[i][j]==-1:
                sub_sum=0
                find(i,j,check,land)
                sum_dict[check]=sub_sum
                check+=1
    
    answer = 0
    for column in range(m):
        check_set = set()
        sub_ans = 0
        for row in range(n):
            if check_num[row][column]!=-1:
                if check_num[row][column] not in check_set:
                    check_set.add(check_num[row][column])
                    sub_ans += sum_dict[check_num[row][column]]
        answer = max(answer,sub_ans)
    
    return answer