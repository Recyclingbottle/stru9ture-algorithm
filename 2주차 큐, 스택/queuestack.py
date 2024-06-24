from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
sequence_A = list(map(int, input().rstrip().split()))
sequence_B = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
sequence_C = list(map(int, input().rstrip().split()))

queue = deque()
for i in range(N):
    if sequence_A[i] == 0:
        queue.appendleft(sequence_B[i])


for i in range(M):
  queue.append(sequence_C[i])
  print(queue.popleft(), end = " ")