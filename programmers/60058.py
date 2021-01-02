from collections import deque

name = '(()())()'
#name = '()'

q = deque(list(name))


def isBalanced(p):
    a = p.count('(')
    b = p.count(')')
    if a == b:
        return True
    else:
        return False


def isRight(p):
    stack = [p[0]]
    for i in range(1, len(p)):
        stack.append(p[i])
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True


print(isRight(name))


def solution(p):
    if p == '':
        return ''
    if isRight(p):
        return p

    for i in range(len(p)):
        u = p[:i + 1]
        v = p[i + 1:]

        if isBalanced(u) and isBalanced(v):
            if isRight(u):  # u가 올바른 문자열이라면
                v = solution(v)
                return u + v
            else:  # 그렇지 않다면
                tmp = '(' + solution(v) + ')'
                u = list(u[1:-1])
                for i in range(len(u)):
                    if u[i] == '(':
                        u[i] = ')'
                    else:
                        u[i] = '('
                u = ''.join(u)
                return tmp + u

    return p


print(solution(name))
