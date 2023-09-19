from typing import List

"""
Initialize a variable dist to k. 
This variable keeps track of the distance between the last encountered 1 
and the current position in the nums list. 
In the beginning, we assume that the first 1 can be found at least k positions away from the start.

Iterate through the nums list using a for loop, examining each element num one by one.

Inside the loop, there are three cases to consider:

a. If num is 0, it means we've encountered a zero. In this case, we increment the dist variable by 1. 
This step is to keep track of the distance between the last 1 and the current position.

b. If num is 1, it means we've encountered a one. 
In this case, we check if the value of dist is greater than or equal to k. 
If it is, this means there are at least k zeros between this 1 and the last one. 
We reset the dist variable to 0 because we are now starting to measure the distance 
between this 1 and the next one.

c. If num is neither 0 nor 1, we return False immediately. 
This indicates that the input list nums contains values other than 0 and 1, 
which is not allowed according to the problem statement.

After iterating through the entire nums list, we return True. 
This means that there are at least k zeros between every pair of ones in the list.

Using the provided input data:

    The first 1 is encountered at position 0. We set dist to k, which is 2.
    We encounter three zeros in a row (positions 1, 2, and 3). dist becomes 5 (2 + 1 + 1 + 1).
    
    The second 1 is encountered at position 4. Since dist is greater than or equal to k, 
    we reset dist to 0.
    We encounter two zeros in a row (positions 5 and 6). dist becomes 2 (0 + 1 + 1).
    
    The third 1 is encountered at position 7. Since dist is greater than or equal to k, 
    we reset dist to 0.

The loop has now finished, and we return True. 
This indicates that there are at least 2 zeros between every pair of ones in the nums list.
"""

def kLengthApart(nums: List[int], k: int) -> bool:
	dist = k 
	for num in nums:
		if num == 0:
			dist += 1
		elif num == 1 and dist >= k:
			dist = 0
		else:
			return False
	return True
nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2 
print(kLengthApart(nums, k))












