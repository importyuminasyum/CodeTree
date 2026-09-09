n = int(input())
grid = [input() for _ in range(n)]

# Please write your code here.
'''
격자에 숫자가 있으면 동전이 있음 - 동전 번호
각 위치에 최대 한 개
최소 3개의 동전 수집 - 도착점으로 도달
번호가 증가하는 순서대로 수집
지나가도 동전 수집하지 않아도 됨, 같은 위치 또 지나가도 됨 - 방문체크 x
3개 이상 뽑기
조합 - 이게 정렬되어있겠지?
아니면 부분집합 - cur_coin 끝까지 갔을 때, cnt >= 3인 것만 경로 찾을 거

0 이 아니면 딕셔너리?에 넣을까?
동전 번호: 행열 좌표
이 키를 뽑아보기 - 

이거 근데 그냥 조건부 조합인거지.. 
comb(0, 0)
# 현재 cur_coin(수) 만큼 지나왔고, 0 ~ cur_coin 중 cnt개 만큼을 뽑은 상태

def comb(cur_coin, cnt):
    if cur_coin == N + 1:
        if cnt > 2:
            return pick_numbers # 인덱스

    # 처음에는 0을 넣고 '넣었다' 라고 보내기
    pick_numbers.append(cur_coin)
    comb(cur_coin + 1, cnt + 1)
    pick_numbers.pop()
    # 처음에는 0을 안 넣고 '안 넣었다'라고 보내기
    comb(cur_coin + 1, cnt)


comb(0, 0) 배열에 대해서
선택된 동전을 지나는 경우의 수 구하기

이거는 각 동전에 대해서 최솟값의 합이 무조건 전체에 대한 최솟값임
- S - 동전 1
- 동전 1 - 동전 2
- 동전 2 - 동전 3
- 동전 3 - E

그러면 그 뽑은 동전 인덱스에 대해서
지금 인덱스와 다음 인덱스의 거리를 구하면 됨
어떻게? 다 상관없으니까 그냥 abs(r1 - r2) + abs(c1 - c2)
이거 더한 값이 그냥 최솟값
그럼 내가 구한 배열에 대해서 최솟값 갱신해놓고 출력하면 끝

불가능한 경우는 동전 배열의 개수가 3 미만인 경우 뿐임


'''
from collections import deque

def cal_distance(rc1, rc2):
    return abs(rc1[0] - rc2[0]) + abs(rc1[1] - rc2[1])

def cal_min_move(comb):
    # comb: 뽑은 동전 번호, 행, 열

    move = cal_distance(s, comb[0][1:]) + cal_distance(comb[-1][1:], e)
    
    for idx in range(len(comb) - 1):
        move += cal_distance(comb[idx][1:], comb[idx + 1][1:])

    return move

def combination(depth, cnt):
    global min_move

    if depth == len(coins):
        if cnt > 2:
            min_move = min(min_move, cal_min_move(pick_coins)) # 인덱스
            return
        return

     # 처음에는 0을 안 넣고 '안 넣었다'라고 보내기
    combination(depth + 1, cnt)
    # 처음에는 0을 넣고 '넣었다' 라고 보내기
    pick_coins.append(coins[depth])
    combination(depth + 1, cnt + 1)
    pick_coins.pop()
   
coins = []
for r in range(n):
    for c in range(n):
        if grid[r][c].isdigit():
            coin = int(grid[r][c])
            coins.append((coin, r, c))

        elif grid[r][c] == 'S':
            s = (r, c)
        elif grid[r][c] == 'E':
            e = (r, c)

pick_coins = []
min_move = float('inf')

coins.sort()

if len(coins) < 3:
    print(-1)

else:
    combination(0, 0)
    print(min_move)
