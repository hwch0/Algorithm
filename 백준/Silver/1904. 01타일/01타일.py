import sys

read = sys.stdin.readline
n = int(read())
if n==1 :
    print(n)
else :
    S = [0 for i in range(n+1)]
    S[1], S[2] = 1, 2
    for i in range(3, n+1):
        S[i] = (S[i-1] + S[i-2]) % 15746

    print(int(S[n]))