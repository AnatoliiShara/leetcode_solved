from typing import List


def countElements(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if any(num > x and num < y for x in nums for y in nums):
            count += 1
    return count
print(countElements([11,7,2,15]))

def countElements100(nums: List[int]) -> int:
	res = 0 
	mn = min(nums)
	mx = max(nums)
	for num in nums:
		if num > mn and num < mx:
			res += 1
	return res 
print(countElements100([11,7,2,15]))