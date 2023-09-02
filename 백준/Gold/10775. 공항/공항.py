import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

g = int(input())
p = int(input())

check_g = [i for i in range(g+1)]

def check(i):
    if check_g[i]==i:
        return i
    
    check_g[i]=check(check_g[i])
    return check_g[i]


count = 0
for _ in range(p):
    g_i = int(input())
    last = check(g_i)
    if last >0:
        count+=1
        check_g[last] = check(last-1)
    else:
        break
print(count)