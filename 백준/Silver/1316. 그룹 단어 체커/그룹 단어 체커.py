import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
cnt = 0

for i in range(n):
    q = deque(read())
    stack=['']
    check = True
    if len(q)==1:
        cnt +=1
        break
    else:        
        while q:
            a = q.popleft()
            if a in stack and stack[-1]!= a:                
                check=False
                break
            stack.append(a)
        if check:
            cnt +=1
    
print(cnt)