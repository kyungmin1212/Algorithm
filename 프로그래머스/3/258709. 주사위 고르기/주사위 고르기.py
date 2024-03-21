from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    answer = []
    n = len(dice)
    idx_list = [i for i in range(n)]
    idx_set = set(idx_list)
    
    max_count = 0
    max_comb = 0
    for comb in combinations(idx_list,n//2):
        available_list_1=[sum(item) for item in product(*[dice[idx] for idx in comb])]
        
        diff_comb = idx_set-set(comb)
        available_list_2=[sum(item) for item in product(*[dice[idx] for idx in diff_comb])]
        available_list_2.sort()
        total_len = len(available_list_2)
        count=0
        for item in available_list_1:
            count += bisect_left(available_list_2,item)
        if count>max_count:
            max_count = count
            max_comb = comb
    
    answer = sorted(list(max_comb))
    answer = [item+1 for item in answer]
    
    return answer