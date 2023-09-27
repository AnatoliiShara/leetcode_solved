from typing import List

"""
Initialize variables:

missing_count is set to 0. This variable will count the missing positive integers.
current_number is set to 1. This variable represents the current number being checked.
index is set to 0. It keeps track of the current position in the arr array.

Enter the while loop:

Check if index is less than the length of arr, and if the value at arr[index] is equal to current_number. 
In the beginning, index is 0, and arr[index] is 2, which is not equal to current_number (1).
Since 1 is missing, missing_count is incremented to 1.

Move to the next number:

current_number is incremented to 2.

Repeat the process:

current_number is 2, and index is now 0. 

The value at arr[index] is 2, which is equal to current_number.
Since 2 is found in arr, index is incremented to 1, and no increment in missing_count occurs.

Move to the next number:

current_number is incremented to 3.

Repeat the process:

current_number is 3, and index is still 1. The value at arr[index] is 3, 
which is equal to current_number.
Since 3 is found in arr, index is incremented to 2, and no increment in missing_count occurs.

Move to the next number:

current_number is incremented to 4.

Repeat the process:

current_number is 4, and index is still 2. 

The value at arr[index] is 4, which is equal to current_number.
Since 4 is found in arr, index is incremented to 3, and no increment in missing_count occurs.

Move to the next number:

current_number is incremented to 5.

Repeat the process:

current_number is 5, and index is still 3. 

The value at arr[index] is 7, which is greater than current_number.
Since 5 is missing, missing_count is incremented to 2.

Check if missing_count (2) is equal to k (5):

Since they are not equal, the loop continues.

Move to the next number:

current_number is incremented to 6.

Repeat the process:
   
current_number is 6, and index is still 3. The value at arr[index] is 7, 
which is less than current_number.
Since 6 is missing, missing_count is incremented to 3.

Check if missing_count (3) is equal to k (5):
    
Since they are not equal, the loop continues.

Continue this process until missing_count equals k:
    
current_number is 7, which matches the value at arr[index]. Increment index to 4.
current_number is 8, which is missing. Increment missing_count to 4.
current_number is 9, which is missing. Increment missing_count to 5.

Check if missing_count (5) is equal to k (5):
    
Now, missing_count is equal to k, which means we've found the 5th missing positive integer.

Return the current value of current_number, which is 9.

So, for the input arr = [2,3,4,7,11] and k = 5, 
the function correctly finds that the 5th missing positive integer is 9 
and returns that value as the output.
"""


def findKthPositive(arr: List[int], k: int) -> int:
	# initialize variables
	missing_count = 0 			# count of missing numbers
	current_number = 1 			# current number to check
	index = 0                   # index for the arr array
	while True:
		if index < len(arr) and arr[index] == current_number:
			# if current number matches an element in array
			index += 1
		else:
			# if current number is missing
			missing_count += 1
		if missing_count == k:
			# if we found kth missing number
			return current_number
		# move to next number
		current_number += 1
	return current_number
print(findKthPositive([2,3,4,7,11], 5))

def findKthPositive(arr: List[int], k: int) -> int:
	missing_count = 0
	current_number = 1 
	index = 0
	while True:
		if index < len(arr) and arr[index] == current_number:
			index += 1
		else:
			missing_count += 1
		if missing_count == k:
			return current_number
		current_number += 1
	return current_number
print(findKthPositive([2,3,4,7,11], 5))








