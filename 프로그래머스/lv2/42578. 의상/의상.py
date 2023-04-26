from collections import Counter

def solution(clothes) :
    
    clothes = [c[1] for c in clothes]
    counter = dict(Counter(clothes))
    
    s = 0
    

    if len(counter) == 1:
        
        return len(clothes)

    else: 
        i = 1
        for clothe in counter.values():
            i *=(clothe+1)
           
    return i-1
