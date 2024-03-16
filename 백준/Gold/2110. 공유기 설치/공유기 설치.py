import sys

input = sys.stdin.readline

n, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()
start, end = 0, arr[-1] - arr[0] + 1

while start < end:
    mid = (start + end) // 2

    output = 1
    before_point = arr[0]
    # 제일 처음을 설치해야 가장 인접한 두 공유기 사이의 거리가 최대
    for i in range(1, n):
        if arr[i] - before_point >= mid:
            output += 1
            before_point = arr[i]

    if output >= c:
        start = mid + 1
    else:
        end = mid

print(start - 1)
