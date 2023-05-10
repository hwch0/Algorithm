import sys
read = input

n, m = map(int, read().split())
arr1 = []
arr2 = []

for i in range(n):
    arr1.append([int(x) for x in input().split()])

for i in range(n):
    arr2.append([int(x) for x in input().split()])

answer = [ [c+d for c, d in zip(a,b)]for a, b in zip(arr1, arr2)]

for i in answer:
    print(*i)
