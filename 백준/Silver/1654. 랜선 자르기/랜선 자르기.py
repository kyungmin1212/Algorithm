import sys

input = sys.stdin.readline

k, n = map(int, input().split())

arr = [int(input()) for _ in range(k)]


def find(arr, n):
    start, end = 1, max(arr) + 1

    while start < end:
        mid = (start + end) // 2

        output = sum([item // mid for item in arr])
        if output >= n:
            start = mid + 1
        else:
            end = mid

    return start - 1


print(find(arr, n))
