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
left = 2 
right = 5 
print(is_covered(ranges, left, right))

def is_covered1(ranges: List[List[int]], left: int, right: int) -> bool:
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
left = 2 
right = 5 
print(is_covered1(ranges, left, right))

def is_covered2(ranges: List[List[int]], left: int, right: int) -> bool:
	covered = [False] * (right + 1)
	for start, end in ranges:
		for i in range(start, end + 1):
			if i <= right:
				covered[i] = True
	for i in range(left, right + 1):
		if not covered[i]:
			return False
	return True

def is_covered3(ranges: List[List[int]], left: int, right: int) -> bool:
	covered = [False] * (right + 1)
	for start, end in ranges:
		for i in range(start, end + 1):
			if i <= right:
				covered[i] = True
	for i in range(left, right + 1):
		if covered[i]:
			return True 
	return False
ranges = [[1,2], [3,4], [5,6]]
left = 2 
right = 5 
print(is_covered3(ranges, left, right))

def is_covered4(ranges: List[List[int]], left: int, right: int) -> bool:
	covered = [False] * (right + 1)
	for start, end in ranges:
		for i in range(start, end + 1):
			if i <= right:
				covered[i] = True
	for i in range(left, right + 1):
		if covered[i]:
			return True
	return False
ranges = [[1,2], [3,4], [5,6]]
left = 2 
right = 5 
print(is_covered4(ranges, left, right))	

def is_covered5(ranges: List[List[int]], left: int, right: int) -> bool:
	covered = [False] * (right + 1)
	for start, end in ranges:
		for i in range(start, end + 1):
			if i <= right:
				covered[i] = True
	for i in range(left, right + 1):
		if covered[i]:
			return True
	return False
ranges = [[1,2], [3,4], [5,6]]
left = 2 
right = 5 
print(is_covered5(ranges, left, right))























