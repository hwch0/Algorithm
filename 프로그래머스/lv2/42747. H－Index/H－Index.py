def solution(citations):
    
    if len(citations)!=1 and citations[0]!=0:
        
        for h in range(len(citations),0, -1):
            n = len(list(filter(lambda x: x>=h, citations)))

            if n>=h:
                break
    else: h=0
        
    return h