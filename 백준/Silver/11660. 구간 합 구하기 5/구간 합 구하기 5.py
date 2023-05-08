import sys, copy

read = sys.stdin.readline

n, m = map(int, read().split())

arr = [[0] * (n+1)]

for i in range(n):
    arr.append([0] + [int(x) for x in read().split()])

matrix = [ [0 for _ in range(n+1)] for _ in range(n+1)]    
    
for i in range(1, n+1):
    for j in range(1, n+1):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1] + arr[i][j]
    
for i in range(m):
    a, b, c, d = map(int, read().split())
    result = matrix[c][d] - matrix[a-1][d] - matrix[c][b-1] + matrix[a-1][b-1]
    print(result)