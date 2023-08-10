from typing import List

def buildArray(nums: List[int]) -> List[int]:
	n = len(nums)
	answer = [0] * n 
	for i in range(n):
		answer[i] = nums[nums[i]]
	return answer
print(buildArray([0, 2, 1, 5, 3, 4]))

