# 17144번 미세먼지 안녕! 

# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

# 이건 함수로 만드는 게 편할 거 같다 

from sys import stdin

# 입력 받기
R, C, T = map(int, stdin.readline().split())
room = [list(map(int, stdin.readline().split())) for _ in range(R)]

def spread(room, R, C):
    # 새로운 방 상태를 저장할 배열 초기화
    new_room = [[0] * C for _ in range(R)]
    
    # 각 위치의 미세먼지를 확산시킴
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                # 공기청정기 위치는 그대로 유지
                new_room[r][c] = -1
            elif room[r][c] > 0:
                # 확산될 미세먼지 양 계산
                spread_amount = room[r][c] // 5
                spread_count = 0
                # 네 방향으로 확산
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        new_room[nr][nc] += spread_amount
                        spread_count += 1
                # 확산 후 남은 미세먼지 양
                new_room[r][c] += room[r][c] - spread_amount * spread_count
    return new_room

def clean(room, R, C, air_cleaners):
    top, bottom = air_cleaners

    # 위쪽 공기청정기 반시계 방향 순환
    # 왼쪽 열을 위로 이동
    for r in range(top - 1, 0, -1):
        room[r][0] = room[r - 1][0]
    # 맨 윗 행을 왼쪽으로 이동
    for c in range(C - 1):
        room[0][c] = room[0][c + 1]
    # 오른쪽 열을 아래로 이동
    for r in range(top):
        room[r][C - 1] = room[r + 1][C - 1]
    # 맨 아랫 행을 오른쪽으로 이동
    for c in range(C - 1, 1, -1):
        room[top][c] = room[top][c - 1]
    room[top][1] = 0  # 공기청정기에서 나오는 바람은 미세먼지가 없음

    # 아래쪽 공기청정기 시계 방향 순환
    # 왼쪽 열을 아래로 이동
    for r in range(bottom + 1, R - 1):
        room[r][0] = room[r + 1][0]
    # 맨 아랫 행을 왼쪽으로 이동
    for c in range(C - 1):
        room[R - 1][c] = room[R - 1][c + 1]
    # 오른쪽 열을 위로 이동
    for r in range(R - 1, bottom, -1):
        room[r][C - 1] = room[r - 1][C - 1]
    # 맨 윗 행을 오른쪽으로 이동
    for c in range(C - 1, 1, -1):
        room[bottom][c] = room[bottom][c - 1]
    room[bottom][1] = 0  # 공기청정기에서 나오는 바람은 미세먼지가 없음

# 공기청정기 위치 찾기
air_cleaners = [i for i in range(R) if room[i][0] == -1]

# T초 동안 확산 및 정화 반복
for _ in range(T):
    room = spread(room, R, C)
    clean(room, R, C, air_cleaners)

# 남아있는 미세먼지 양 계산
total_dust = sum(sum(cell for cell in row if cell > 0) for row in room)
print(total_dust)
