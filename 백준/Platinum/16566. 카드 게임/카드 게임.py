from bisect import bisect_left, bisect_right

n,m,k = map(int,input().split())

card_num = list(map(int,input().split()))
chulsu_card_num = list(map(int,input().split()))

# 시간복잡도 
# 4000000 번 * 10000
# 40000000000  400억번..

# log2 만큼  log(4000000) - > 21.931568569324174

# card_num을 정렬하면 nlogn -> 4000000 *log2(4000000) 이것도 넘음.
# 이정도는 정렬 가능 80000000 # 약 8000만

# 결국 del을 사용하게 되면 O(KN) 
# del 없이 코드 작성 필요 
# 다음 순서를 지목하는 딕셔너리 (즉, parent랑 비슷)
# 만들고, check 를 통해서 그 카드가 사용되었다면 
# check가 안된 부분까지 find하는 함수를 만들기.

sorted_card_num = sorted(card_num)
check = [0 for _ in range(m)]
parent = {i:i+1 for i in range(m)}

def find(idx):
    if check[idx]==0:
        return idx
    
    parent[idx] = find(parent[idx])
    return parent[idx]

for c_n in chulsu_card_num: # K
    idx = bisect_right(sorted_card_num,c_n)
    
    idx = find(idx)
    check[idx]=1
    print(sorted_card_num[idx])