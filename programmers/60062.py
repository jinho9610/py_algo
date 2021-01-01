# https://programmers.co.kr/learn/courses/30/lessons/60062
# 너무 어려움
from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 취약 지점 리스트의 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])

    answer = len(dist) + 1  # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):  # 나열을 위해서 순열 이용
            count = 1  # 투입할 친구의 수
            position = weak[start]+friends[count-1]  # 시작점
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구를 도입
                    if count > len(dist):  # 전부 다 투입했다면
                        break
                    position = weak[index]+friends[count-1]  # 현재까지 점검한 위치
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
