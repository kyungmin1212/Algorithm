from collections import defaultdict

n = int(input())

check_list = [defaultdict(int) for _ in range(10)]

for i in range(1,10):
    check_list[i][1<<i]+=1 # 현재 i번째에 (1<<i 거쳐온 노드들)에 개수 +1

for i in range(2,n+1):
    new_check_list = [defaultdict(int) for _ in range(10)]
    for j in range(10):
        if j==0:
            for k,v in check_list[1].items():
                new_check_list[j][k|(1<<j)]+=v
        elif j==9:
            for k,v in check_list[8].items():
                new_check_list[j][k|(1<<j)]+=v                
        else:
            for k,v in check_list[j-1].items():
                new_check_list[j][k|(1<<j)]+=v
            for k,v in check_list[j+1].items():
                new_check_list[j][k|(1<<j)]+=v

    check_list = new_check_list

count = 0
for idx_dict in check_list:
    count+=idx_dict[(1<<10)-1]
print(count%1000000000)
