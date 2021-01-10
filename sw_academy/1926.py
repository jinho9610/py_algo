n = int(input())


def check(x):
    global cnt
    flag = False
    listx = list(str(x))
    for i in range(len(listx)):
        if listx[i] == '3' or listx[i] == '6' or listx[i] == '9':
            flag = True
            cnt += 1
    return flag


for i in range(1, n+1):
    cnt = 0
    if check(i):
        for _ in range(cnt):
            print('-', end='')
        print(end=' ')
    else:
        print(i, end=' ')
