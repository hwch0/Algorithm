import sys

read = sys.stdin.readline

t = int(read())
result = []

for i in range(t):
    n = int(read())
    
    p = [0 for i in range(101)]
    p[1], p[2], p[3] = 1,1,1
    
    if n <= 3:
        result.append(1)
    else :
        for i in range(4, n+1) :
            p[i] = p[i-2] + p[i-3]
        result.append(int(p[n]))
for i in result:
    print(i)