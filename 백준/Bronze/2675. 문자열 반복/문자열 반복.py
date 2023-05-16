import sys

read= sys.stdin.readline

T = int(read())
result = []
for t in range(T):
    r, s = map(str, read().split())
    result.append(''.join([x*int(r) for x in str(s)]))

for r in result:
    print(r.strip())