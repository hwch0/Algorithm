import sys
from heapq import heappop, heappush

read = sys.stdin.readline

n = int(read())
heap = []
result = []
for i in range(n):
    x = int(read())
    
    if x == 0 and len(heap)==0:
        result.append(0)
    elif x == 0 and len(heap)!=0:
        result.append(-heappop(heap))
    elif x > 0:
        heappush(heap, -x)

for i in result:
    print(i)