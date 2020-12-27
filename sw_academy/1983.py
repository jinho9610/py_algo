import math

T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    scores = {}
    target = 0
    for i in range(n):
        m, f, h = map(int, input().split())
        score = 0.35*m + 0.45 * f + 0.2*h
        scores[i+1] = score
    scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    for i in range(n):
        if scores[i][0] == k:
            print('#'+str(test_case)+' '+grade[math.ceil((i+1)*10/n)-1])

# t = int(input())
# for tc in range(1, t+1):
#     N, K = map(int, input().split())
#     rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
#     temp = []
#     for n in range(N):
#         first, second, third = map(int, input().split())
#         score = (first * 0.35) + (second * 0.45) + (third * 0.20)
#         temp.append(score)
#     index = N//10
#     student = list(reversed(sorted(temp)))
#     target = temp[K-1]
#     target_index = student.index(target)
#     for i in range(0, len(student), index):
#         for j in range(i, i+index):
#             student[j] = rank[i//index]
#     print("#{} {}".format(tc, student[target_index]))
