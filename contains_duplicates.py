from typing import List

def containsDuplicates(nums: List[int]) -> bool: 
	seen = set()
	for num in nums:
		if num in seen:
			return True
		seen.add(num)
	return False
nums1 = [1, 2, 3, 1]
print(containsDuplicates(nums1))