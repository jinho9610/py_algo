data = list(input())

for i in range(len(data)):
    print(ord(data[i]) - ord('A') + 1, end=' ')
