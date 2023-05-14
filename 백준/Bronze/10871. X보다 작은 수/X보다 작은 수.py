import sys

read = sys.stdin.readline

n, x = map(int, read().split())

result = [int(i) for i in map(int, read().split()) if i < x]

print(*result)