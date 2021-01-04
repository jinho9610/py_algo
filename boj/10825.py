n = int(input())

info = []
for i in range(n):
    data = input().split()
    info.append((data[0], int(data[1]), int(data[2]), int(data[3])))

info = sorted(
    info, key=lambda student: (-student[1], student[2], -student[3], student[0]))

for s in info:
    print(s[0])
