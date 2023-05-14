import sys

read = sys.stdin.readline

n, m = map(int, read().split())

basket = [i for i in range(1,n+1)]

for i in range(m):
    a, b = map(int, read().split())
    if a != b:
        basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

print(*basket)