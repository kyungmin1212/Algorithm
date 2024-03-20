import sys
import math

input = sys.stdin.readline

n = int(input())

max_n = 2 ** (math.ceil(math.log2(n)))

seg_tree = [0 for _ in range(2 * max_n)]

arr = map(int, input().split())


def init_update(idx, value):
    idx = max_n + idx
    seg_tree[idx] = seg_tree[idx] ^ value
    while idx > 1:
        idx = idx // 2
        seg_tree[idx] = seg_tree[idx * 2] ^ seg_tree[idx * 2 + 1]


for i, value in enumerate(arr):
    init_update(i, value)

lazy_tree = [0 for _ in range(2 * max_n)]


def lazy_update(idx, left, right):
    if lazy_tree[idx] != 0:
        if (right - left + 1) % 2 == 0:
            seg_tree[idx] = seg_tree[idx]
        else:
            seg_tree[idx] = seg_tree[idx] ^ lazy_tree[idx]
        if left != right:
            lazy_tree[idx * 2] = lazy_tree[idx * 2] ^ lazy_tree[idx]
            lazy_tree[idx * 2 + 1] = lazy_tree[idx * 2 + 1] ^ lazy_tree[idx]
        lazy_tree[idx] = 0


def update(start, end, left, right, idx, value):
    lazy_update(idx, left, right)
    if end < left or start > right:
        return
    elif start <= left and right <= end:
        if (right - left + 1) % 2 == 0:
            seg_tree[idx] = seg_tree[idx]
        else:
            seg_tree[idx] = seg_tree[idx] ^ value
        if left != right:
            lazy_tree[idx * 2] = lazy_tree[idx * 2] ^ value
            lazy_tree[idx * 2 + 1] = lazy_tree[idx * 2 + 1] ^ value
    else:
        mid = (left + right) // 2
        update(start, end, left, mid, idx * 2, value)
        update(start, end, mid + 1, right, idx * 2 + 1, value)
        seg_tree[idx] = seg_tree[idx * 2] ^ seg_tree[idx * 2 + 1]


def find(start, end, left, right, idx):
    lazy_update(idx, left, right)
    if end < left or start > right:
        return 0
    elif start <= left and right <= end:
        return seg_tree[idx]
    else:
        mid = (left + right) // 2
        left = find(start, end, left, mid, idx * 2)
        right = find(start, end, mid + 1, right, idx * 2 + 1)
        return left ^ right


m = int(input())

for _ in range(m):
    t, *order = map(int, input().split())
    if t == 1:  # a,b,c를 입력받아 구간 [a,b]의 각 원소에 c를 xor 하기
        a, b, c = order
        update(a, b, 0, max_n - 1, 1, c)
    elif t == 2:  # a번째 원소 값 출력
        print(find(order[0], order[0], 0, max_n - 1, 1))
