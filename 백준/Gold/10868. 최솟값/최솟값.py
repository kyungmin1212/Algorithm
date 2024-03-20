import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

max_n = 2 ** (math.ceil(math.log2(n)))

seg_tree = [int(1e9) for _ in range(2 * max_n)]


def update(n, value):
    idx = max_n + n
    seg_tree[idx] = value

    while idx > 1:
        idx = idx // 2
        seg_tree[idx] = min(seg_tree[idx * 2], seg_tree[idx * 2 + 1])


for i in range(n):
    update(i, int(input()))


def find(n_1, n_2, s, e, idx):
    if n_1 <= s and e <= n_2:
        return seg_tree[idx]
    elif n_1 > e or n_2 < s:
        return int(1e9)
    else:
        left = find(n_1, n_2, s, (s + e) // 2, idx * 2)
        right = find(n_1, n_2, (s + e) // 2 + 1, e, idx * 2 + 1)
        return min(left, right)


for _ in range(m):
    a, b = map(int, input().split())
    print(find(a - 1, b - 1, 0, max_n - 1, 1))
