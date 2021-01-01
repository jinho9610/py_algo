from itertools import combinations

n, m = map(int, input().split())

arr = [[0]*(n+1) for _ in range(n+1)]
house, chicken = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:  # 집
            house.append((i+1, j+1))
        elif data[j] == 2:
            chicken.append((i+1, j+1))


def getChickenDistance(house, chicken):
    distances = []
    for h in house:
        x, y = h[0], h[1]
        min = 10000
        for c in chicken:
            if min > abs(c[0] - x) + abs(c[1] - y):
                min = abs(c[0] - x) + abs(c[1] - y)
        distances.append(min)
    return sum(distances)


def getCityChickenDistance(house, chicken):
    global m
    new_chicken = list(combinations(chicken, m))  # m개만 골라낸 치킨 집 리스트
    result_set = []
    for i in range(len(new_chicken)):
        result_set.append(getChickenDistance(house, new_chicken[i]))
    return sorted(result_set)[0]


print(getCityChickenDistance(house, chicken))
