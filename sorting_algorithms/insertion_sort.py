from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
	N = len(arr)
	for i in range(1, N):
		for j in range(i, 0, -1):
			if arr[j] < arr[j - 1]:
				arr[j], arr[j - 1] = arr[j - 1], arr[j]
			else:
				break
	return arr
print(insertion_sort([-3,5,0,-8,1, 10]))