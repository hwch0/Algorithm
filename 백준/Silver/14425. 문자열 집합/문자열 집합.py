import sys

read= sys.stdin.readline

n, m = map(int, read().split())

S =[]
s_list =[]

for i in range(n):
    S.append(str(read()))
for i in range(m):
    s_list.append(str(read()))
    
cnt =0

for string in s_list:
    if string in S:
        cnt +=1

print(cnt)