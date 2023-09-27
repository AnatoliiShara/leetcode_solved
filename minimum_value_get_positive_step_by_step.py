

from typing import List

def minStartValue(nums: List[int]) -> int:
	prefix_sum = 0
	min_prefix_sum = 0
	for num in nums:
		prefix_sum += num 
		if prefix_sum < min_prefix_sum:
			min_prefix_sum = prefix_sum
	if min_prefix_sum <= 0:
		return abs(min_prefix_sum) + 1
	return 1 
print(minStartValue([-3,2,-3,4,2]))


def minStartValue100(nums: List[int]) -> int:
	prefix_sum_list = []
	prefix_sum = 0
	for num in nums:
		prefix_sum += num
		prefix_sum_list.append(prefix_sum)
	min_prefix_sum = min(prefix_sum_list)
	if min_prefix_sum <= 0:
		return abs(min_prefix_sum) + 1
	return 1 
print(minStartValue100([-3,2,-3,4,2]))