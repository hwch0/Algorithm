import sys
read= sys.stdin.readline

n, m = map(int, read().split())
li =[]
def back(li):
    if len(li)==m:
        print(' '.join(map(str, li)))
        return li
    
    for i in range(1, n+1):
        if i not in li:
            li.append(i)
            back(li)
            li.pop()

back(li)