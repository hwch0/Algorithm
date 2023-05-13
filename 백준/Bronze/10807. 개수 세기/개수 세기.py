import sys

read = sys.stdin.readline
n = int(read())

num_list = list(map(int, read().split()))

v = int(read())

print(num_list.count(v))