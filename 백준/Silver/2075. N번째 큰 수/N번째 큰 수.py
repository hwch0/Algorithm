import sys 
import heapq
num = int(sys.stdin.readline())
nums = []
nums.append(max(list(map(int, sys.stdin.readline().split()))))
    
for i in range(num-1):
    cur = nums[0]
    for j in list(map(int, sys.stdin.readline().split())):
        if j > cur:
            heapq.heappush(nums, j)
        if len(nums) > num:
            heapq.heappop(nums)
       
print(int(nums[0]))