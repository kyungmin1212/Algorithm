import sys

sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def postorder(start, end):  # start~ end까지 탐색
    if start > end:
        return

    # start가 가장 클 경우,
    # 오른쪽 서브 트리는 없기 때문에 없는 값인 end+1로 지정해주기
    div = end + 1
    root = arr[start]  # start 는 root 노드
    for i in range(start + 1, end + 1):
        if root < arr[i]:
            div = i  # i 부터 오른쪽 서브트리입니다.
            break

    postorder(start + 1, div - 1)  # 왼쪽 서브트리
    postorder(div, end)  # 오른쪽 서브트리
    print(arr[start])


postorder(0, len(arr) - 1)
