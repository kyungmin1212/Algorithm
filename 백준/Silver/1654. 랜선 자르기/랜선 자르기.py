import sys
k,n=map(int,sys.stdin.readline().split())
arr=[]
for i in range(k):
    arr.append(int(sys.stdin.readline()))
lower_bound,upper_bound=1,max(arr)
result = 0

while lower_bound<=upper_bound:
    mid=(lower_bound+upper_bound)//2
    cut_sum=sum([(i//mid) for i in arr])
    if cut_sum>=n:
        result=mid
        lower_bound=mid+1
    elif cut_sum<n:
        upper_bound=mid-1
print(result)