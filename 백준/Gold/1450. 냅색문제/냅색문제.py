import sys
from itertools import combinations
from bisect import bisect_right

input = sys.stdin.readline

n, c = map(int, input().split())

arr = list(map(int, input().split()))

A_list = arr[: n // 2]
B_list = arr[n // 2 :]


def get_weights_list(arr):
    weights = []
    for i in range(len(arr) + 1):
        for comb in combinations(arr, i):
            weights.append(sum(comb))

    return sorted(weights)


A_weights_list = get_weights_list(A_list)
B_weights_list = get_weights_list(B_list)

count = 0
for a in A_weights_list:
    remain = c - a
    if remain >= 0:
        idx = bisect_right(B_weights_list, remain)
        count += idx

print(count)
