from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))
operators = []

a, b, c, d = map(int, input().split())
for i in range(a):
    operators.append('+')
for i in range(b):
    operators.append('-')
for i in range(c):
    operators.append('x')
for i in range(d):
    operators.append('/')

new_oper = list(set(list(permutations(operators, n-1))))

result = []
for y in range(len(new_oper)):
    ans = nums[0]
    for i in range(1, n):
        if new_oper[y][i-1] == '+':
            ans += nums[i]
        elif new_oper[y][i-1] == '-':
            ans -= nums[i]
        elif new_oper[y][i-1] == 'x':
            ans *= nums[i]
        else:
            ans = int(ans/nums[i])
    result.append(ans)

result.sort()

print(result[-1])
print(result[0])
