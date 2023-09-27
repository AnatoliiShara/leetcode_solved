
from typing import List 

def smallerNumbersThanCurrent(nums: List[int]):
	output = []
	count = 0
	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[i] > nums[j]:
				count += 1
		output.append(count)
		count = 0
	return output
print(smallerNumbersThanCurrent([8,1,2,2,3]))