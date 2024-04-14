import sys

input = sys.stdin.readline

t = int(input())


def flip(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1


for _ in range(t):
    n, *arr = list(map(int, input().split()))

    answer = []
    count = 0
    for i in reversed(range(2, len(arr) + 1)):
        max_value = max(arr[:i])
        max_idx = arr.index(max_value)
        if max_idx == i - 1:  # 이미 올바른 위치에 있으면 무시
            continue
        if max_idx != 0:  # 첫 위치가 아니면, 첫 위치로 이동
            answer.append(max_idx + 1)  # 0-based to 1-based index for output
            flip(arr, 0, max_idx)
        answer.append(i)  # 최종 위치로 이동
        flip(arr, 0, i - 1)

    print(len(answer), *answer)
