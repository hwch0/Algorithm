import sys

read = sys.stdin.readline

n = int(read())

result = list(map(int, read().split()))

print(min(result), max(result))