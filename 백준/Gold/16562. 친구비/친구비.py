import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

pay_arr = list(map(int, input().split()))


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b

    else:
        parent[b] = a

    pay_arr[a], pay_arr[b] = min(pay_arr[a], pay_arr[b]), min(pay_arr[a], pay_arr[b])


parent = [i for i in range(n)]

for _ in range(m):
    v, w = map(int, input().split())
    union(v - 1, w - 1)

for i in range(n):
    find(i)

parent_set = set(parent)

sum_value = sum([pay_arr[idx] for idx in parent_set])
if sum_value <= k:
    print(sum_value)
else:
    print("Oh no")
