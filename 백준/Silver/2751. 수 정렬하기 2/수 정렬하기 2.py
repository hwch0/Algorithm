import sys 
N=int(sys.stdin.readline())

num=[]
for n in range(int(N)):
    num.append(int(sys.stdin.readline()))
num.sort()

for n in num:
    print(n)