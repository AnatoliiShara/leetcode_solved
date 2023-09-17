"""
Input:

    List of numbers: [-1, 0, 3, 5, 9, 12]
    Target: 9

    Initialization:
        left is initially set to 0, 
        which corresponds to the first index of the list.
        right is initially set to 5, 
        which corresponds to the last index of the list (since the list has 6 elements).

    Binary Search Loop:
        We enter a while loop that continues as long as left is less than or equal to right.

    Iteration 1:
        Calculate the mid index as (0 + 5) // 2, which is 2.
        Check if nums[2] (the element at index 2) is equal to the target (9). 
        It's not equal, so we move to the next step.

    Iteration 2:
        Since nums[mid] (nums[2]) is less than the target, 
        we adjust the left pointer to mid + 1, which becomes 3.
        The search interval now becomes [5, 9, 12] (the right half of the original list).

    Iteration 3:
        Calculate the new mid index as (3 + 5) // 2, which is 4.
        Check if nums[4] (the element at index 4) is equal to the target (9). It is equal, so we return mid, which is 4.

    Target Found:
        The function returns 4, which is the index where the target value (9) was found in the list [-1, 0, 3, 5, 9, 12].
"""

from typing import List

def search(nums: List[int], target: int) -> int:
	left = 0
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2 
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1 
	return -1 
print(search([-1, 0, 3, 5, 9, 12], 9))

def search(nums: List[int], target: int) ->	int:
	left = 0 
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2
		if nums[mid] == target:
			return mid 
		elif nums[mid] > target:
			right = mid - 1 
		else:
			left = mid + 1
	return -1
print(search([-1, 0, 3, 5, 9, 12], 9))

def search(nums: List[int], target: int) -> int:
	left = 0 
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2 
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1 
print(search([-1, 0, 3, 5, 9, 12], 2))

def search(nums: List[int], target: int) -> int:
	left = 0
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2 
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1

def search(nums: List[int], target: int) -> int:
	left = 0 
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2 
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1 

def search(nums: List[int], target: int) -> int:
	left = 0 
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2 
		if nums[mid] == target:
			return -1 
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1 
	

























































































































