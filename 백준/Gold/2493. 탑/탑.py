import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
stack = []
answer = []
for idx, item in enumerate(arr):
    while stack:
        if stack[-1][0] < item:
            stack.pop()
        else:
            break

    if stack:
        answer.append(stack[-1][1])
    else:
        answer.append(0)

    stack.append((item, idx + 1))

print(*answer)
