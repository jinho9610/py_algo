# 기둥과 보 설치
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or (x-1, y, 1) in answer or (x, y, 1) in answer or (x, y-1, 0) in answer:
                continue
            else:
                return False
        else:
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치라면
            answer.append((x, y, a))
            if not possible(answer):
                answer.remove((x, y, a))
        if b == 0:
            answer.remove((x, y, a))
            if not possible(answer):
                answer.append((x, y, a))

    return sorted(answer)


a = [(1, 2)]

a.append((3, 4))
print(a)
a.remove((1, 2))
print(a)
