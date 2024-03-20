import math
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
# 4->4 5->8 ~ 8->8
max_n = 2**math.ceil(math.log(n,2))

arr = [0 for _ in range(max_n*2)]
lazy = [0 for _ in range(max_n*2)]

for i in range(n):
    arr[max_n+i]=int(input())

# 초기화
for i in reversed(range(1,max_n)):
    arr[i]=arr[i*2]+arr[i*2+1]

# 세그먼트 트리 3가지 경우
# left right 안에 now_left now_right 있는 겨웅
# left right 박에 now_left now_right 있는 경우
# 걸치는 경우
def propagate(now_left,now_right,idx):
    if lazy[idx]!=0:
        v = lazy[idx]
        arr[idx]+=(now_right-now_left+1)*v
        if now_right!=now_left:
            lazy[idx*2]+=v
            lazy[idx*2+1]+=v
        lazy[idx]=0
# update
def update(left,right,now_left,now_right,idx,value):
    propagate(now_left,now_right,idx)
    if left<=now_left and right>=now_right:
        arr[idx] += (now_right-now_left+1)*value
        if now_left!=now_right:
            lazy[2*idx] +=value
            lazy[2*idx+1] +=value
        return
    if left>now_right or right<now_left:
        return
    
    mid = (now_left+now_right)//2
    l = update(left,right,now_left,mid,idx*2,value)
    r = update(left,right,mid+1,now_right,idx*2+1,value)
    arr[idx]=arr[idx*2]+arr[idx*2+1]
    
def find(left,right,now_left,now_right,idx):
    propagate(now_left,now_right,idx)
    if left<=now_left and right>=now_right:
        return arr[idx]
    if left>now_right or right<now_left:
        return 0
    
    mid = (now_left+now_right)//2
    l = find(left,right,now_left,mid,idx*2)
    r = find(left,right,mid+1,now_right,idx*2+1)
    return l+r
    
for _ in range(m+k):
    a,*check_list = map(int,input().split())
    if a==1:
        b,c,d=check_list
        update(b-1,c-1,0,max_n-1,1,d)
    elif a==2:
        b,c=check_list
        print(find(b-1,c-1,0,max_n-1,1))