import math
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

max_n = 2**(math.ceil(math.log(n,2)))

arr = [0 for _ in range(max_n*2)]

for i in range(n):
    arr[max_n+i]=int(input())
    
# 초기화
for i in reversed(range(1,max_n)):
    arr[i]=arr[i*2]+arr[i*2+1]
    
# update 함수
def update(idx,v): # idx는 1부터 시작
    idx = max_n+idx-1
    arr[idx]=v
    while True:
        idx = idx//2
        if idx<=0:
            break
        arr[idx]=arr[idx*2]+arr[idx*2+1]

# find 함수
# 3가지 경우 존재
# 1. find_left,find_right 일부 또는 전체가 now_left,now_right에 걸친경우 -> 절반씩 나눠서 각각 찾으러 들어가야함.
# 2. find_left,find_right 가 now_left,now_right에 하나도 걸치지 않은경우 -> 이건 아무것도 없는 값 0 return
# 3. find_left,find_right 안에 now_left,now_right가 있는 경우 -> 이건 필요한 값 arr[idx]값을 가져오기
def find(find_left,find_right,now_left,now_right,idx):
    if find_left>now_right or find_right<now_left:
        return 0
    elif find_left<=now_left and find_right>=now_right:
        return arr[idx]
    else:
        left = find(find_left,find_right,now_left,(now_left+now_right)//2,idx*2)
        right = find(find_left,find_right,(now_left+now_right)//2+1,now_right,idx*2+1)
        return left+right
    
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        update(b,c)
    elif a==2:
        print(find(b-1,c-1,0,max_n-1,1))