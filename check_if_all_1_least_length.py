from typing import List

def kLengthApart(nums: List[int], k: int) -> bool:
	dist = k 
	for num in nums:
		if num == 0:
			dist += 1
		elif num == 1 and dist >= k:
			dist = 0
		else:
			return False
	return True
nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2 
print(kLengthApart(nums, k))





























































