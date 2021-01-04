import heapq

n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

result = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum = a + b
    result += sum
    heapq.heappush(card, sum)

print(result)
