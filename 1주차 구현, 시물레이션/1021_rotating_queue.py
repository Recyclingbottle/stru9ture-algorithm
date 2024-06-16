# 1012번 회전하는 큐 

from collections import deque

n, m = map(int, input().split())
input_arr = list(map(int, input().split()))

# 양방향 큐 => 파이썬에선 덱 deque 를 사용
dq = deque(range(1, n+1))

count = 0 # 연산 횟수 

for k in input_arr:
    # k (뽑아야하는 수) 가 어느 인덱스에 있는지 찾고
    idx = dq.index(k)
    # 왼쪽으로 이동하는 게 빠른 경우
    if idx < len(dq) - idx:
        # 뽑아야 하는 수의 인덱스가 전체 큐 길이 절반 보다 작으면 왼쪽
        dq.rotate(-idx)  # 왼쪽으로 idx 만큼 회전
        count += idx
    else:
        # 뽑아야 하는 수의 인덱스가 전체 큐 길이 절반 보다 크면 오른쪽
        dq.rotate(len(dq) - idx)  # 오른쪽으로 (len(dq) - idx) 만큼 회전
        count += len(dq) - idx
    dq.popleft()  # 찾는 원소를 찾으면 왼쪽 원소 빼기

print(count)
