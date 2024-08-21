from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])

count = 1
answer = []
while q:
    if count == k:
        count = 1
        answer.append(str(q.popleft()))

    else:
        count += 1
        q.append(q.popleft())

print("<" + ", ".join(answer) + ">")
