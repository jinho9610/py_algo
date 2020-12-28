T = int(input())

base = [2, 3, 5, 7, 11]

for t in range(1, T+1):
    result = [0]*5
    data = int(input())
    while True:
        if data == 1:
            break
        for i in range(5):
            if data % base[i] == 0:
                result[i] += 1
                data = data//base[i]
                if data == 1:
                    break

    print('#{} {} {} {} {} {}'.format(
        t, result[0], result[1], result[2], result[3], result[4]))
