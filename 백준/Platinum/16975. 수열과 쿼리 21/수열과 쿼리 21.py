import sys
import math

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

max_n = 2 ** (math.ceil(math.log2(n)))
seg_tree = [0 for _ in range(max_n * 2)]


def init_update(idx, value):
    idx = max_n + idx
    seg_tree[idx] = value
    while idx > 1:
        idx = idx // 2
        seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]


for i, v in enumerate(arr):
    init_update(i, v)

lazy_tree = [0 for _ in range(max_n * 2)]


def lazy_update(idx, left, right):
    if lazy_tree[idx] != 0:
        seg_tree[idx] += (right - left + 1) * lazy_tree[idx]
        if left != right:
            lazy_tree[idx * 2] += lazy_tree[idx]
            lazy_tree[idx * 2 + 1] += lazy_tree[idx]
        lazy_tree[idx] = 0


def update(start, end, left, right, idx, value):
    lazy_update(idx, left, right)
    if right < start or left > end:
        return
    elif start <= left and right <= end:
        seg_tree[idx] += (right - left + 1) * value
        if left != right:
            lazy_tree[idx * 2] += value
            lazy_tree[idx * 2 + 1] += value
    else:
        mid = (left + right) // 2
        update(start, end, left, mid, idx * 2, value)
        update(start, end, mid + 1, right, idx * 2 + 1, value)
        seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]


def find(start, end, left, right, idx):
    lazy_update(idx, left, right)
    if right < start or left > end:
        return 0
    elif start <= left and right <= end:
        return seg_tree[idx]
    else:
        mid = (left + right) // 2
        l = find(start, end, left, mid, idx * 2)
        r = find(start, end, mid + 1, right, idx * 2 + 1)
        return l + r


m = int(input())

for _ in range(m):
    q, *order = map(int, input().split())

    if q == 1:
        a, b, c = order
        update(a - 1, b - 1, 0, max_n - 1, 1, c)
    elif q == 2:
        x = order[0]
        print(find(x - 1, x - 1, 0, max_n - 1, 1))
