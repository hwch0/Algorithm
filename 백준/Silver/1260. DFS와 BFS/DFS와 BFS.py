import sys 
from collections import deque

read = sys.stdin.readline

n, m , v = map(int, read().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, read().split())
    graph[node1][node2] = True
    graph[node2][node1] = True

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(v):
    dfs_visited[v] = True # 해당 노드 방문 처리
    print(v, end=" ")
    for i in range(1, n+1):
        if not dfs_visited[i] and graph[v][i]: # i를 방문하지 않았고, v와 i가 연결되어 있을 경우        
            dfs(i) # 해당 i와 연결된 인접노드에 대해서 깊이 탐색

def bfs(v):
    que = deque([v])
    bfs_visited[v] = True
    while que:
        node = que.popleft()
        print(node, end=" ")
        
        for i in range(1, n+1):
            if not bfs_visited[i] and graph[node][i]:
                bfs_visited[i] = True
                que.append(i)
    
    
dfs(v)
print()
bfs(v)