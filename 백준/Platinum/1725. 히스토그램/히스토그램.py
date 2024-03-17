import sys

input = sys.stdin.readline

n = int(input())  # 막대의 개수
histogram = [int(input()) for _ in range(n)] + [0]  # 끝 처리를 위해 0 추가
stack = []  # 인덱스를 저장할 스택
max_area = 0  # 최대 넓이 저장

for i, height in enumerate(histogram):
    # 스택이 비어있지 않고, 현재 막대의 높이가 스택의 top에 있는 막대의 높이보다 낮은 경우
    while stack and histogram[stack[-1]] > height:
        # 스택에서 막대를 팝하고, 해당 막대의 높이로 만들 수 있는 최대 넓이를 계산
        top = stack.pop()
        # 스택이 비어있지 않으면 현재 인덱스에서 스택 top 인덱스까지의 거리를 너비로 사용
        width = i if not stack else i - stack[-1] - 1
        # 최대 넓이 업데이트
        max_area = max(max_area, histogram[top] * width)
    # 현재 막대의 인덱스를 스택에 푸시
    stack.append(i)

print(max_area)