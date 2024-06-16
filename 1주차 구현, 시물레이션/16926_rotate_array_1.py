# 16926번 배열 돌리기1

from collections import deque

n, m, r = map(int, input().split())

input_arr = []
answer = [[0] * m for _ in range(n)]
deq = deque()
for _ in range(n):
    row = list(map(int, input().split()))
    input_arr.append(row)

# r 만큼 회전 시켜야함 
# 회전이 층마다 이루어짐 
# 그렇다면 층마다 구분해서 1차원 배열로 만들어서 회전

# 1 2 3 4 8 6 2 3 4 5 9 5 로 바깥층이 되어있는데 
# 2회전 후 
# 3 4 8 6 2 3 4 5 9 5 1 2 
# r, 회전 수 만큼 앞에 원소를 뒤로 보내면 됨
# deque 를 사용하면 될 거 같다 

# 일단 껍질 끼리 분리해야겠다 

loops = min(n,m) // 2 # 껍질 갯수 

for i in range(loops):
    deq.clear()
    # 1차원 배열로 변환
    # 위쪽
    deq.extend(input_arr[i][i:m-i])
    # 오른쪽
    deq.extend(input_arr[j][m-i-1] for j in range(i+1, n-i-1))
    # 아래쪽
    deq.extend(input_arr[n-i-1][i:m-i][::-1])
    # 왼쪽
    deq.extend(input_arr[j][i] for j in range(n-i-2, i, -1))
    
    # 회전
    deq.rotate(-r)
    
    # 다시 2차원 배열로 변환
    # 위쪽
    for j in range(i, m-i):
        answer[i][j] = deq.popleft()
    # 오른쪽
    for j in range(i+1, n-i-1):
        answer[j][m-i-1] = deq.popleft()
    # 아래쪽
    for j in range(m-i-1, i-1, -1):
        answer[n-i-1][j] = deq.popleft()
    # 왼쪽
    for j in range(n-i-2, i, -1):
        answer[j][i] = deq.popleft()    
# 결과 출력
for line in answer:
    print(" ".join(map(str, line)))
