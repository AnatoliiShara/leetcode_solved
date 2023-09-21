"""
Here's how i and j change during the execution of the code:

i = 0, num = 1

It checks if num (which is 1) is already in the seen dictionary 
(it's not since this is the first value encountered).
 So, it doesn't enter the if block and adds 1 to the seen dictionary with i as the index: seen[1] = 0.

i = 1, num = 2
It checks if num (which is 2) is already in the seen dictionary (it's not). 
So, it doesn't enter the if block and adds 2 to the seen dictionary with i as the index: seen[2] = 1.

i = 2, num = 3
It checks if num (which is 3) is already in the seen dictionary (it's not). 
So, it doesn't enter the if block and adds 3 to the seen dictionary with i as the index: seen[3] = 2.

i = 3, num = 1
It checks if num (which is 1) is already in the seen dictionary (it is). It also checks if abs(i - seen[num]), which is abs(3 - 0), is less than or equal to k (which is 3). Both conditions are met.
Therefore, the function returns True 
because it found two distinct indices i and j such that nums[i] == nums[j] (both are 1) 
and abs(i - j) <= k (abs(3 - 0) <= 3).

So, the output of the function with the provided data is True, 
indicating that there are two distinct indices in the array nums1 that meet the specified conditions.
"""

from typing import List 

def containsDuplicatesII(nums: List[int], k: int) -> bool:
	seen = dict()
	for i, num in enumerate(nums):
		if num in seen and abs(i - seen[num]) <= k:
			return True
		else:
			seen[num] = i 
	return False
nums1 = [1, 2, 3, 1]
k1 = 3
print(containsDuplicatesII(nums1, k1))
