import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

def find(start,end):
    global answer
    if start>end:
        return
    mid = (start+end)//2
    left = mid-1
    right = mid+1
    
    min_height = arr[mid]
    count = 1
    answer = max(answer,min_height)
    while True:
        count+=1
        if left<start and right>end:
            break
        
        elif left<start: # 오른쪽으로만 이동가능
            right_height = min(min_height,arr[right])
            right+=1
            min_height = right_height
            answer = max(answer,min_height*count)
            
        elif right>end: # 왼쪽으로만 이동 가능
            left_height = min(min_height,arr[left])
            left-=1
            min_height = left_height
            answer = max(answer,min_height*count)
            
        else: # 양쪽으로 이동가능
            left_height = min(min_height,arr[left])
            right_height = min(min_height,arr[right])
            
            if left_height>=right_height:
                left-=1
                min_height = left_height
                answer = max(answer,min_height*count)
            else:
                right+=1
                min_height = right_height
                answer = max(answer,min_height*count)
    if start!=end:
        find(start,mid-1)
        find(mid+1,end)
        
answer = 0
find(0,n-1)
print(answer)