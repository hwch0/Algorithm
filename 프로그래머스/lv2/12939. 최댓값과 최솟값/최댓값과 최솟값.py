def solution(s):
    s = s.split(" ")
    new = [int(i) for i in s]
    
    result = [str(min(new)), str(max(new))]
    result = " ".join(result)
    
    
    return result