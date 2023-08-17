from typing import List

def is_covered(ranges: List[List[int]], left: int, right: int) -> bool:
	covered = [False] * (right + 1)

	for start, end in ranges:
		for i in range(start, end + 1):
			if i <= right:
				covered[i] = True

	for i in range(left, right + 1):
		if not covered[i]:
			return False

	return True
ranges = [[1,2], [3,4], [5,6]]
left = 1 
right = 5 
print(is_covered(ranges, left, right))
