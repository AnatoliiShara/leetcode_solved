"""
Initialization:
    num_to_piece is initialized as an empty dictionary.
    concatenated is initialized as an empty list.

Iteration 1 (num = 49):

    The code checks if 49 is in num_to_piece. It's not initially present.
    No changes to concatenated at this point.
    The print(concatenated) statement doesn't produce any output.

Iteration 2 (num = 18):

    The code checks if 18 is in num_to_piece. It's not initially present.
    No changes to concatenated at this point.
    The print(concatenated) statement doesn't produce any output.

Iteration 3 (num = 16):

    The code checks if 16 is in num_to_piece. It is found.
    num_to_piece[16] is [16, 18, 49], so the code extends concatenated with this subarray.
    concatenated becomes [16, 18, 49].
    The print(concatenated) statement displays [16, 18, 49].

Comparison:

    After processing all elements in arr, 
    the code compares the concatenated list [16, 18, 49] with the original arr [49, 18, 16].

Final Result:

    The concatenated list [16, 18, 49] is not the same as the original arr [49, 18, 16]. The order of elements is different.
    As a result, the comparison concatenated == arr returns False.

Return Value:

Since the comparison is False, the function canFormArray returns False, 
indicating that it is not possible to form the arr list 
by concatenating subarrays from pieces in the same order as they appear in arr.

In summary, the code processes each element in arr, checks if it is in num_to_piece, 
and concatenates the corresponding subarrays from pieces into the concatenated list. 
After processing all elements, 
it compares concatenated with the original arr to determine if arr can be formed 
by concatenating subarrays from pieces. In this specific case, 
the order of elements in concatenated is different from arr, leading to a False result.
"""


from typing import List

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	#print(num_to_piece)
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
			#print(concatenated)
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr  
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	concatenated = []
	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
	return concatenated == arr
print(canFormArray([49, 18, 16], [[16, 18, 49]]))
print(canFormArray([15,88], [[15], [88]]))
















