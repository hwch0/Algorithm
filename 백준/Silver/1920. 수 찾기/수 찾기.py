# 방법2. 이분탐색 활용
# 리스트가 오름차순으로 정렬이 되어있을 때 해당 리스트의 중간값을 활용해서 범위를 좁혀가며 탐색
# O(logN) 시간복잡도 발생
# left와 right를 list 타입으로 정의하지 말고, 인덱스로 사용

import sys 
read = sys.stdin.readline

n = int(read())
n_list = list(map(int, read().split()))
n_list.sort()

m = int(read())
m_list = map(int, read().split())


for i in m_list:
    start = 0
    end = len(n_list)-1
    
    while start <= end:
        mid = (start+end) //2
        target=n_list[mid]
        
        if i == target:
            break
        elif i < target:
            end = mid-1
        else:
            start = mid+1
    print(int(i==target))