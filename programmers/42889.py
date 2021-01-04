N = 8
stages = [1, 2, 3, 4, 5, 6, 7]


def solution(N, stages):
    stop_stages = [0]*(N+2)  # 특정 스테이지에 머물러 있는 사람

    for i in range(len(stages)):
        stop_stages[stages[i]] += 1

    fail_rate = []

    for i in range(1, N+1):
        if stop_stages[i] != 0:
            fail_rate.append((i, stop_stages[i]/sum(stop_stages[i:])))
        else:
            fail_rate.append((i, 0))
    fail_rate = sorted(fail_rate, key=lambda item: (-item[1], item[0]))

    result = []
    for fail in fail_rate:
        result.append(fail[0])

    return result


print(solution(N, stages))

'''
# 모범 답안
def solution(N, stages):
    answer = []
    length = len(stages)  # 전체 사용자 수

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:  # 현재 스테이지에 도달한 사람이 없다면 = 이후의 스테이지에도 도달한 사람 0라는 의미
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: -t[1])

    answer = [i[0] for i in answer]
    return answer
'''
