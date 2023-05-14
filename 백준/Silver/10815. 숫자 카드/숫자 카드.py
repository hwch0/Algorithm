import sys

read= sys.stdin.readline

n = int(read())
cards = list(map(int, read().split()))
cards.sort()
result = [0 for i in range(int(read()))]
targets = list(map(int, read().split()))

for index, t in enumerate(targets):
    start = 0
    end = len(cards)-1    
    
    while start <= end:
        mid= (start+end)//2
        if t == cards[mid]:
            result[index]=1
            break
        elif t < cards[mid]:
            end = mid -1
        else:
            start = mid+1
    
print(*result)