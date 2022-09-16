def solution(a):
    return a % sum(map(lambda x: int(x), str(a))) == 0