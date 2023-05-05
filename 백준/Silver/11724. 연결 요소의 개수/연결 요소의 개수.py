from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for i in range(m): # 재귀함수 구현을 위한 그래프 만들기
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

        
def dfs(v):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w)
    return visited

visited = []
cnt = 0
for k in range(1,n+1):
    if k not in visited:
        dfs(k)
        cnt+=1

print(cnt)