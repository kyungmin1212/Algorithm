def solution(heights):
    # 높이 배열을 정렬합니다.
    heights.sort()
    total_len = len(heights)
    n = total_len // 2
    is_odd = total_len % 2

    # 재배치된 배열을 준비합니다.
    arr = []

    # 홀수와 짝수 길이에 따라 다른 재배치 방식을 적용합니다.
    if is_odd:
        for i in range(n):
            arr.append(heights[i])
            arr.append(heights[n + is_odd + i])
        arr.append(heights[n])
    else:
        for i in range(n):
            arr.append(heights[n + is_odd + i])
            arr.append(heights[i])

    # 인접한 높이 차이를 계산합니다.
    arr.append(arr[0])  # 배열의 처음과 끝을 연결하기 위해
    diff = [abs(arr[j] - arr[j + 1]) for j in range(len(arr) - 1)]

    # 높이 차이 배열을 정렬합니다.
    diff.sort()
    answer = diff[0] if len(diff) == 1 else diff[1]

    return answer


# 테스트
heights = [1, 4, 5, 6, 9]
print(solution(heights))
