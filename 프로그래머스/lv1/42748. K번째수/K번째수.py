import numpy as np

def solution(array, commands):
    answer = []
    for c in commands:
        li = sorted(array[c[0]-1: c[1]])
        answer.append(li[c[2]-1])
    
    return answer