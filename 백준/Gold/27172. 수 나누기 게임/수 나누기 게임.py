from collections import defaultdict

n = int(input())

arr = list(map(int,input().split()))

check_arr = defaultdict(lambda : False)
for item in arr:
    check_arr[item]=True

max_arr = max(arr)

sort_arr = sorted(arr)

score_list = [0 for _ in range(max_arr+1)]

for v in sort_arr:
    for i in range(v*2,max_arr+1,v):
        if check_arr[i]:
            score_list[v]+=1
            score_list[i]-=1

for x in arr:
    print(score_list[x],end=' ')