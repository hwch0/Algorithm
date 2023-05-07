from heapq import heappush, heappop
import sys
read = sys.stdin.readline
n = int(read())

heap = []
for _ in range(n):
    heappush(heap, int(read()))

count1 = 0
count2 = 0

while len(heap)>1:
    count1 = heappop(heap)+ heappop(heap)
    heappush(heap, count1)
    count2 += count1

    
print(count2)