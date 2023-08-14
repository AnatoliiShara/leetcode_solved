from typing import List

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
	num_to_piece = {piece[0]: piece for piece in pieces}
	print(num_to_piece)
	concatenated = []

	for num in arr:
		if num in num_to_piece:
			concatenated.extend(num_to_piece[num])
			print(concatenated)

	return concatenated == arr

print(canFormArray([49, 18, 16], [[16, 18, 49]]))