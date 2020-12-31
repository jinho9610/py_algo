# 322 문자열 재정렬
a = 'jinho'
print(type(a[0: 2]))
c = []
result = 0

data = list(input())

for i in data:
    if 65 <= ord(i) <= 90:
        c.append(i)
    elif 48 <= ord(i) <= 57:
        result += int(i)

c.sort()
for i in c:
    print(i, end='')
print(result)
