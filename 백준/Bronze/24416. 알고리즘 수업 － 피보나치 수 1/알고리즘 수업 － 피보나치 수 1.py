import sys

read = sys.stdin.readline
n = int(read())

def fib(n):
    if n ==1 or n==2 :
        return 1
    else: return (fib(n-1) + fib(n-2))
    
def fibonacci(n) :
    return n-2

print(fib(n), fibonacci(n))