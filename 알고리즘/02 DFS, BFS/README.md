### 그래프 탐색 알고리즘
연결되어 있는 개체 중 **특정 개체**를 찾는 알고리즘
1. 경로탐색 유형(최단시간,거리)
2. 네트워크형(연결된 그룹의 수, 두 개체가 연결되어 있는지 등)
3. 조합형 문제
<br>

![image](https://github.com/chominyeong/tobigs_20-21_Hyehwa/assets/81460659/6516b461-7e88-46ba-ac6b-4fe9a9a98cac)

### _DFS(Depth-First-Search)_, 깊이 우선 탐색 → 한놈만 팬다
1. **Stack**   
  a. 시작 노드를 stack에 넣는다.   
  b. stack에서 노드 하나를 꺼내고, 그 노드의 자식 노드를 stack에 쌓는다. 꺼낸 노드는 출력한다.    
  c. 또 stack에서 **제일 나중에** 들어간 노드를 꺼내고, 그 노드의 자식 노드를 stack에 쌓는다. 꺼낸 노드는 출력한다.   
  d. 더 이상 stack에서 꺼낼 노드가 없을 때까지 반복한다.
<br>

2. **재귀함수**   
![image](https://github.com/chominyeong/tobigs_20-21_Hyehwa/assets/81460659/01520acd-9ee6-42e9-8129-900fe16850ef)
재귀는 출력 먼저, 그 다음에 호출!    
   ```
   dfsR(0)
   └── dfsR(1)
       └── dfsR(2)   # stack과 다르게 정방향으로 호출해서 2를 출력한다.(stack은 3을 먼저 꺼내서 3이 출력됨)
           └── dfsR(4)
               └── dfsR(3)
                   └── dfsR(5)
                       ├── dfsR(6)
                       │   └── dfsR(8)
                       └── dfsR(7)
   ```
출력 : 0 1 2 4 3 5 6 8 7    
<br>
<br>

### _BFS(Breadth-First-Search)_, 너비 우선 탐색 → 여러놈을 때리면서 간다
1. **Queue**
  a. 시작 노드를 queue에 넣는다.   
  b. queue에서 노드 하나를 꺼내고, 그 노드의 자식 노드들을 queue에 쌓는다. 꺼낸 노드는 출력한다.   
  c. 또 stack에서 **제일 먼저** 들어간 노드를 꺼내고, 그 노드의 자식 노드를 queue에 쌓는다. 꺼낸 노드는 출력한다.   
  d. 더 이상 queue에서 꺼낼 노드가 없을 때까지 반복한다.   
<br>

2. **LinkedList**

<br>
<br>

> **deque 라이브러리**
>   ```
>q1 = deque('love')
>print("q1 :", q1)
>
>q2 = deque()
>q2.append('l')
>q2.append('o')
>q2.append('v')
>q2.append('e')
>print("q2 :", q2)
>
> 출력
> q1 : deque(['l', 'o', 'v', 'e'])
> q2 : deque(['l', 'o', 'v', 'e'])
>   ```


   ```
