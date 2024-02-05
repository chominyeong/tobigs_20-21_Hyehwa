#1260
import sys
input = sys.stdin.readline
from collections import deque

# 정점 수, 간선 수, 시작점
n, m, v = map(int, input().split())

## 1. 그래프 그리기
graph = [[0]*(n+1) for _ in range(n+1)]
#graph = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
#graph = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]


## 2. 방문 여부 리스트 생성, 아직 방문 안했으므로 모두 0 입력
dlst = [0]*(n+1)
blst = [0]*(n+1)

## 3-1. dfs → stack+재귀함수
def dfs(v):
  # 방문하면 1로 변경
  dlst[v] = 1
  # 방문한 노드 출력
  print(v, end=" ")
  # 방문 시작
  for i in range(1,n+1):
    # 아직 방문하지 않았고, 연결되어 있다면 재귀호출로 방문하면 됨
    if (dlst[i]==0) and (graph[v][i]==1):
      dfs(i)

dfs(v)   # 함수호출 순서 : dfs(1)→dfs(2)→dfs(4)→dfs(3)

print()

## 3-2. bfs → queue
def bfs(v):
  # 방문하면 큐에 넣음
  q = deque([v])
  # 방문하며 1로 변경
  blst[v] = 1
  # 방문 시작
  while q:
    # 큐 맨 앞에 있는 값 꺼내서 출력
    v = q.popleft()
    print(v, end=" ")
    for i in range(1, n+1):
      # 아직 방문하지 않았고, 인접노드라면 큐에 추가
      if (blst[i]==0) and (graph[v][i]==1):
        q.append(i)
        # 방문했으므로 1로 변경
        blst[i] = 1

bfs(v)

