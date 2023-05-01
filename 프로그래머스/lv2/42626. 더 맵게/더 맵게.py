import heapq
from heapq import heappush, heappop, heapify

def solution(scoville, k):
    heapify(scoville)
    answer = 0
    
    while scoville[0] < k:
        if len(scoville)<2:
            return -1
        a= heappop(scoville)
        b= heappop(scoville)
        heappush(scoville, (a + b*2))
        answer +=1
    return answer