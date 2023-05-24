import sys
from collections import Counter

read = sys.stdin.readline

n = int(read())
li1 = list(map(int, read().split()))
dic = Counter(li1)
m = int(read())
result = [dic[x] for x in list(map(int, read().split()))]
print(*result)