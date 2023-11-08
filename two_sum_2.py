from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start < end:
        total = numbers[start] + numbers[end]
        if total == target:
            return [start + 1, end + 1]
        if total < target:
            start += 1
        else:
            end -= 1
    return None

print(twoSum([2,7,11,15], 9))

def twoSum1(numbers: List[int], target: int) -> List[int]:
	left = 0 
	right = len(numbers) - 1
	while left < right:
		total = numbers[left] + numbers[right]
		if total == target:
			return [left + 1, right + 1]
		elif total < target:
			left += 1
		else:
			right -= 1
	return -1 
print(twoSum1([2,3,4], 6)) 