def solution(li, location) :
    prop = 1
    index = list(range(len(li)))
    target = index[location]
    stack = []
    
    while li :
        if li[0] == max(li):
            stack.append(index[0])
            li = li[1:]
            index = index[1:]
            if stack[-1] == target : 
                break
            else : prop = prop +1 
        
        else :
            li.append(li[0])
            li = li[1:]
            index.append(index[0])
            index = index[1:]
    
    return prop