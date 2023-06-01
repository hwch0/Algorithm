import sys

read = sys.stdin.readline

n, m = map(int, read().split())

reault = []

def back(li=[]):
    if len(li) == m:
        print(*li)
        return li
    else:
        for i in range(1, n+1):
            if len(li)==0:
                li.append(i)
                back(li)
                li.pop()
            elif i >= li[-1] and len(li) >=1:
                li.append(i)
                back(li)
                li.pop()

back([])