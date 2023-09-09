n = int(input())

arr = list(map(int,input().split()))

idx_arr = [(item,idx) for idx,item in enumerate(arr)]

sorted_arr = sorted(idx_arr)
ans_dict = {item[1]:idx for idx,item in enumerate(sorted_arr)}

for i in range(n):
    print(ans_dict[i], end=' ')