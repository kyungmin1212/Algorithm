n = int(input())

top = list(map(int, input().split()))

stack = []
answer = []

for idx, item in enumerate(top, 1):
    while stack:
        if stack[-1][1] < item:
            stack.pop()
        else:
            break

    if stack:
        answer.append(stack[-1][0])
    else:
        answer.append(0)
    stack.append((idx, item))

print(*answer)