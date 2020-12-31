# 자물쇠와 열쇠
'''
# 내 답, 런타임에러 발생
from pprint import pprint
import copy

key = []
lock = []
for i in range(3):
    key.append(list(map(int, input().split())))
for i in range(3):
    lock.append(list(map(int, input().split())))


def matrix_rotation(mat):
    dummy = []

    n = len(mat)
    m = len(mat[0])

    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(mat[j][i])

        tmp.reverse()
        dummy.append(tmp)

    return dummy


def mov_matrix(arr, dx, dy):
    mat = copy.deepcopy(arr)
    n = len(mat)

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i < dx or j < dy:
                mat[i][j] = 0
            else:
                mat[i][j] = mat[i-dx][j-dy]

    return mat


def open(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if key[i][j] + lock[i][j] != 1:
                return False
    return True


def mani_key(key, lock):
    n = len(lock)
    m = len(lock[0])

    dummy = [[0] * m for i in range(n)]

    for i in range(len(key)):
        for j in range(len(key[0])):
            dummy[i][j] = key[i][j]

    return dummy


def solution(key, lock):
    # 자물쇠는 그냥 있고, key를 움직이자
    key = mani_key(key, lock)  # 자물쇠랑 키의 크기를 맞춰준다
    n, m = len(lock), len(lock[0])
    for k in range(5):
        if k != 0:
            key = matrix_rotation(key)
            for i in range(n):
                for j in range(m):
                    tmp_key = mov_matrix(key, i, j)
                    if open(tmp_key, lock):
                        return True

    return False


if solution(key, lock):
    print('True')
else:
    print('False')
'''

from pprint import pprint
import time

# 모범 답안의 회전 함수보다 내 함수가 근소하게 더 빠름
# def rotate_a_matrix_by_90_degree(a):
#     n = len(a)
#     m = len(a[0])

#     result = [[0]*n for _ in range(m)]

#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = a[i][j]

#     return result


def matrix_rotation(mat):
    dummy = []

    n = len(mat)
    m = len(mat[0])

    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(mat[j][i])

        tmp.reverse()
        dummy.append(tmp)

    return dummy


def check(new_lock):  # 자물쇠의 중간 부분이 모두 1인지 확인
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = matrix_rotation(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False
