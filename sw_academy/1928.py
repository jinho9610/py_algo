T = int(input())

for t in range(1, T+1):
    data = list(input())

    enc = ''
    for i in range(len(data)):

        if 'A' <= data[i] <= 'Z':
            enc += format(ord(data[i]) - ord('A'), 'b').zfill(6)
        elif 'a' <= data[i] <= 'z':
            enc += format(ord(data[i]) - ord('a') + 26, 'b').zfill(6)
        elif '0' <= data[i] <= '9':
            enc += format(ord(data[i]) - ord('0') + 52, 'b').zfill(6)
        elif data[i] == '+':
            enc += format(62, 'b').zfill(6)
        elif data[i] == '/':
            enc += format(63, 'b').zfill(6)

    result = ''
    while True:
        if len(enc) <= 8:
            result += chr(int(enc, base=2))
            break
        else:
            result += chr(int(enc[:8], base=2))
            enc = enc[8:]

    print(f'#{t} {result}')
