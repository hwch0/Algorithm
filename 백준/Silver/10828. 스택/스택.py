import sys
read = sys.stdin.readline
n = int(read())
stack = []
result=[]
for i in range(n):
    m = list(read().split())
    method = m[0]
    if method == "push":
        stack.append(int(m[1]))
    elif len(stack) !=0 and method =="top":
        result.append(stack[-1])
    elif len(stack) !=0 and method =="pop":
        result.append(stack.pop())
    elif len(stack)==0 and (method == "top" or method=="pop"):
        result.append(-1)
    elif method == "size":
        result.append(len(stack))
    elif method=="empty":
        result.append(int(len(stack)==0))
 
for i in result:
    print(i)