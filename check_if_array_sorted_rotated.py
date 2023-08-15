from typing import List

def check(nums: List[int]) -> bool:
	Sorted = sorted(nums)
	for i in range(len(nums)):
		if nums[i: ] + nums[: i] == Sorted:
			print(f"Rotation possible at iteration: {i}")
			return True
	return False

nums = [3,4,5,1,2]
res = check(nums)
print(f"Rotation possible: {res}")

"""

"""

def check300(nums: List[int]) -> bool:
	n = len(nums)
	# find index of the smallest element in array
	smallest_idx = 0
	for i in range(1, n):
		if nums[i] < nums[smallest_idx]:
			smallest_idx = i 

	# check if array is sorted after rotation
	for i in range(n):
		original_idx = (i + smallest_idx) % n 
		if nums[i] != nums[original_idx]:
			return False
	return True










