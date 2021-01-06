T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    date = input()  # str

    y = int(date[0:4])
    m = int(date[4:6])
    d = int(date[6:])

    if 0 < m < 13 and 0 < d <= days[m]:
        print('#{3} {0:04d}/{1:02d}/{2:02d}'.format(y, m, d, t+1))
    else:
        print('#{0} -1'.format(t+1))
