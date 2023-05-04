from collections import deque

a, b = map(int, input().split())

q = deque(range(1, a+1))
result = []
i=1

while q:
    num = q.popleft()
    if i==b:
        result.append(num)
        i=1
    else :
        q.append(num)
        i +=1

print('<',', '.join(list(map(str, result))),'>',sep="")