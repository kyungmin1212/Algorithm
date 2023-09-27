import sys
import math

input = sys.stdin.readline

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]

l = min(range(n), key=lambda i: (points[i][1], points[i][0]))
anchor = points.pop(l)

def polar_angle(p0, p1):
    y_span = p1[1] - p0[1]
    x_span = p1[0] - p0[0]
    return math.atan2(y_span, x_span)
# 만약 y가 0이고, x가 양수인 경우, atan2의 값은 0입니다.
# 만약 y가 0이고, x가 음수인 경우, atan2의 값은 π 또는 −π입니다.
# 만약 x가 0이고, y가 양수인 경우, atan2의 값은 π/2 입니다.
# 만약 x가 0이고, y가 음수인 경우, atan2의 값은 -π/2 입니다.

def distance(p0, p1):
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

points.sort(key=lambda p: (polar_angle(anchor, p), distance(anchor, p)))

def ccw(a, b, c):
    # 외적 공식 
    # 두개의 벡터 (a와 b 벡터) (b와 c 벡터)
    # 양수면 왼쪽(반시계), 음수면 오른쪽(시계) ,0이면 같은 선상
    # i            j
    # (b[0]-a[0]) (b[1]-a[1])
    # (c[0]-b[0]) (c[1]-b[1])

    val = (b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0])
    
    if val == 0: return 0  # 콜리니어
    return 1 if val > 0 else -1  # 반시계(1인경우) or 시계(-1인경우)    

hull = [anchor, points[0]]

for i in range(1, n - 1):
    while len(hull) >= 2 and ccw(hull[-2], hull[-1], points[i]) != 1:
        hull.pop()
    hull.append(points[i])

print(len(hull))