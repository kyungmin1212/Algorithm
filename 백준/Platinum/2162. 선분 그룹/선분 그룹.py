import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

# n은 3000까지
# 최악 -> 3000+2999+2998+...+1 = 4501500
# 모든 점들이 같은 그룹인지 체크하기

def find(x):
    if x==parent[x]:
        return x
    
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y]=x
    elif x>y:
        parent[x]=y


point_list = [list(map(int,input().split())) for _ in range(n)]

parent = [i for i in range(n)]

# (x2-x1),(y2-y1)
# (x3-x1).(y3-y1)

# 양수면 반시계 , 음수면 시계 , 0이면 같은 방향
def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def iscross(x1,y1,x2,y2,x3,y3,x4,y4):
    ab_cd = ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)
    cd_ab = ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)

    if ab_cd<=0 and cd_ab<=0:
        if min(x1,x2)>max(x3,x4) or min(x3,x4)>max(x1,x2) or min(y1,y2)>max(y3,y4) or min(y3,y4)>max(y1,y2):
            return False
        
        return True
    else:
        return False

for i in range(n-1):
    x1,y1,x2,y2 = point_list[i]
    parent_check = [False for _ in range(n)]
    parent_value = parent[i]
    parent_check[i]=True

    for j in range(i+1,n):
        x3,y3,x4,y4 = point_list[j]

        if iscross(x1,y1,x2,y2,x3,y3,x4,y4):
            union(i,j)

for i in range(n):
    parent[i] = find(parent[i])

counter = Counter(parent)
print(len(counter))
print(counter.most_common()[0][1])
