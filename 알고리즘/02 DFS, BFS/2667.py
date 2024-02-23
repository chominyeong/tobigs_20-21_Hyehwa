#2667
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

## 1. 그래프 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
'''
[[0, 1, 1, 0, 1, 0, 0],
 [0, 1, 1, 0, 1, 0, 1], 
 [1, 1, 1, 0, 1, 0, 1], 
 [0, 0, 0, 0, 1, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 0], 
 [0, 1, 1, 1, 0, 0, 0]]
'''

## 2. 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

## 3. bfs
def bfs(x,y):
    q = deque([[x,y]])   # queue 생성
    graph[x][y] = 0      # 방문한 위치는 0으로 변경
    cnt = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if (0<=next_x<n) and (0<=next_y<n):
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = 0
                    q.append((next_x, next_y))
                    cnt += 1
    return cnt


## 모든 노드에서 갈 수 있는 경로가 있는지 확인해야 함
lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            lst.append(bfs(i,j))


## 조건에 맞게 출력
lst.sort()
print(len(lst))
for i in lst:
    print(i)