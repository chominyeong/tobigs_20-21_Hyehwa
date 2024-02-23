#2178
import sys
input = sys.stdin.readline
from collections import deque
# n×m 행렬
n, m = map(int, input().split())


## 1. 그래프 생성
graph = [[0]*(m) for _ in range(n)]
for i in range(n):
  graph[i] = list(map(int, input().rstrip()))
'''
[[1, 0, 1, 1, 1, 1], 
 [1, 0, 1, 0, 1, 0],
 [1, 0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1, 1]]
'''


## 2. 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# (0,1):R / (0,-1):L / (-1,0):U / (1,0):D


## 3. bfs(동시에 여러 경로 탐색, 최단 거리)
def bfs(a,b):
  # queue 생성
  q = deque([[a,b]])

  while q:
    # 현재 위치
    x,y = q.popleft()

    for i in range(4):
      ## 상하좌우 이동을 해보고
      next_x = x + dx[i]
      next_y = y + dy[i]

      ## 행렬 안에 있으면서
      if (0 <= next_x < n) and (0 <= next_y < m):
        ## 이동가능한 경로면
        if graph[next_x][next_y] == 1:
          ## 이동
          graph[next_x][next_y] = graph[x][y]+1
          q.append((next_x, next_y))

  return graph[n-1][m-1]  #도착 지점

print(bfs(0,0))  #시작 지점

'''
최종 그래프
[[3, 0, 9, 10, 11, 12], 
 [2, 0, 8,  0, 12,  0], 
 [3, 0, 7,  0, 13, 14], 
 [4, 5, 6,  0, 14, 15]]
'''