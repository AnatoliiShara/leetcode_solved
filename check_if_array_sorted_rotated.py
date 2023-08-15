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