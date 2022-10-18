from collections import deque

def solution(s):
    d = deque(s)
    stack = []
#     if (d[0] == ')' or d[-1] =='('):
#         return False
    while(d):
        v = d.popleft()
        if v == '(':
            stack.append(v)
        elif v==')' and len(stack)!=0 and stack[-1] == '(':
            stack.pop()
        else: return False
    return False if stack else True