#2606
import sys
input = sys.stdin.readline
# 컴퓨터 수
n = int(input())
# 컴퓨터 쌍의 수 = 연결선의 개수
m = int(input())


## 1. 그래프 생성
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    ## 노드(컴퓨터) 양방향 연결
    graph[a] += [b]
    graph[b] += [a]
    '''
    [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    '''


## 2. dfs(재귀함수 사용)
# 방문한 노드 수
cnt = 0
# 컴퓨터별 방문 여부
visited = [0 for _ in range(n+1)]

def dfs(pc_num):
    global cnt
    # 방문(→방문 여부 1로 변경)
    visited[pc_num] = 1

    # 각 노드 별 자식 노드 방문
    for i in graph[pc_num]:
        # 방문하지 않았으면
        if (visited[i]==0):
            # 방문
            dfs(i)
            # 방문한 노드 수 1 증가
            cnt += 1
    return cnt


print(dfs(1))