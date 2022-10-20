def solution(prices) :
    answer = []
    for i,p in enumerate(prices):
        result = sum(list(map(lambda x : x >=p, prices[i+1:])))
        answer.append(result)
    return answer