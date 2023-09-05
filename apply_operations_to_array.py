from typing import List

def applyOperations(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i], nums[i + 1] = nums[i + 1] * 2, 0 
	return sorted(nums, key=lambda x: x==0, reverse=False)
print(applyOperations([1,2,2,2,1,1,0]))


def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2 
			nums[i + 1] = 0 
	non_zeros = [x for x in nums if x != 0]
	zeros = [x for x in nums if x == 0]
	return non_zeros + zeros
print(applyOperations2([1,2,2,2,1,1,0]))

def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2
			nums[i + 1] = 0 
	non_zeros = [x for x in nums if x != 0]
	zeros = [x for x in nums if x == 0]
	return non_zeros + zeros

def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2
			nums[i + 1] = 0
	non_zeros = [x for x in nums if x != 0]
	zeros = [x for x in nums if x == 0]

def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2
			nums[i + 1] = 0 
	non_zeros = [x for x in nums if x != 0]
	zeros = [x for x in nums if x == 0]
	return non_zeros + zeros

def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2
			nums[i + 1] = 0
	non_zeros = [x for x in nums if x == 0]
	zeros = [x for x in nums if x == 0]
	return non_zeros + zeros

def applyOperations2(nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1]:
			nums[i] *= 2
			nums[i + 1] = 0
	non_zeros = [x for x in nums if x != 0]
	zeros = [x for x in nums if x == 0]
	return non_zeros + zeros
























