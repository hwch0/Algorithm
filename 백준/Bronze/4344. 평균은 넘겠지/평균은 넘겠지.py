import sys

read = sys.stdin.readline
n = int(read())

result = []
for i in range(n):
    li = list(map(int, read().split()))[1:]
    avg = float(sum(li) / len(li))
    cnt = sum(list(map(lambda x:x >avg, li)))
    result.append(float((cnt/len(li)))*100)

for p in result:
    print(('%0.3f'%p)+'%')