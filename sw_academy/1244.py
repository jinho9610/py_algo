# 개인 풀이 실패, https://mungto.tistory.com/212 모범 답안
# 경우의 수 찾기, 매개변수로 몇번 바꿨는 지를 넘긴다
# 모든 경우의 수 파악하기 위할 때는 완전 탐색이 힘들면, dfs와 가지치기를 결합. 즉 백트래킹으로 해결해보자
def dfs(count):
    global answer
    # count가 0이라면, 즉 교환이 끝나면
    if not count:
        temp = int(''.join(values))  # values 리스트 내부의 값들을 이어붙여서 숫자로 만듦
        # 가지고 있는 최대수보다 크다면 갱신
        if answer < temp:  # 여기 왜 오류발생하는 지 모르겠음
            answer = temp
        return

    for i in range(length):
        # 경우의 수를 찾는거니까 i보다 큰 위치부터
        for j in range(i+1, length):
            # 두개의 위치를 바구고 나서
            values[i], values[j] = values[j], values[i]
            # 가지치기 해야하니 일단 숫자로 합쳐보고 비교
            temp_key = ''.join(values)
            # 어떤 수가 몇회차에 나왔는 지 체크, 1이면 안나온 거니까 경우의 수에 넣어주기
            # 딕셔너리 get 메소드의 인자 a,b에 대해: a라는 키가 존재하지 않으면 get은 b를 return 한다.
            if visited.get((temp_key, count-1), 1):
                visited[(temp_key, count-1)] = 0
                # dfs 재귀
                dfs(count-1)
            # 다 사용했으면 원상 복귀
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    # 원소의 접근이 편하도록 list로 만듦
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}  # 가지치기를 위한 빈 딕셔너리
    dfs(change)
    print(f'#{t+1} {answer}')
