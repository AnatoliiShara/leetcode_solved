from typing import List 

"""
Pass 1:

First iteration (i = 0, j = 0): Compare 2 and 6. Since 2 is not greater than 6, no swap occurs.
Second iteration (i = 0, j = 1): Compare 6 and 5. Since 6 is greater than 5, a swap occurs. The array becomes arr = [2, 5, 6, 1, 9].
Third iteration (i = 0, j = 2): Compare 6 and 1. Since 6 is greater than 1, a swap occurs. The array becomes arr = [2, 5, 1, 6, 9].
Fourth iteration (i = 0, j = 3): Compare 6 and 9. Since 6 is not greater than 9, no swap occurs.

List after Pass 1: [2, 5, 1, 6, 9]

Pass 2:

    First iteration (i = 1, j = 0): Compare 2 and 5. Since 2 is not greater than 5, no swap occurs.
    Second iteration (i = 1, j = 1): Compare 5 and 1. Since 5 is greater than 1, a swap occurs. The array becomes arr = [2, 1, 5, 6, 9].
    Third iteration (i = 1, j = 2): Compare 5 and 6. Since 5 is not greater than 6, no swap occurs.

List after Pass 2: [2, 1, 5, 6, 9]

Pass 3:

    First iteration (i = 2, j = 0): Compare 2 and 1. Since 2 is greater than 1, a swap occurs. The array becomes arr = [1, 2, 5, 6, 9].
    Second iteration (i = 2, j = 1): Compare 2 and 5. Since 2 is not greater than 5, no swap occurs.
    Third iteration (i = 2, j = 2): Compare 5 and 6. Since 5 is not greater than 6, no swap occurs.

List after Pass 3: [1, 2, 5, 6, 9]

Pass 4:

    First iteration (i = 3, j = 0): Compare 1 and 2. Since 1 is not greater than 2, no swap occurs.
    Second iteration (i = 3, j = 1): Compare 2 and 5. Since 2 is not greater than 5, no swap occurs.
    Third iteration (i = 3, j = 2): Compare 5 and 6. Since 5 is not greater than 6, no swap occurs.

Since no swaps occur in Pass 4, the swapped flag remains False, and the loop breaks.

Final sorted list: [1, 2, 5, 6, 9]

In this implementation of bubble sort, 
the swapped flag helps optimize the algorithm by breaking the loop early if no swaps are made in a pass, indicating that the array is already sorted. 
This reduces unnecessary iterations when the array is mostly sorted.
"""

def bubble_sort(arr: List[int]) -> List[int]:
	n = len(arr)
	for i in range(n):
		# set a flag to optimize algo - if no swaps, algo is sorted
		swapped = False
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr
print(bubble_sort([2,6,5,1,9]))
print(bubble_sort([7,5,-8,0,10,1]))


"""

def bubble_sort2(arr: List[int]) -> List[int]:
	N = len(arr)
	for i in range(0, N - 1):
		for j in range(0, N - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
print(bubble_sort([7,5,-8,0,10,1]))
Pass 1:

First iteration (i = 0, j = 0): Compare 7 and 5. Since 7 is greater than 5, a swap occurs. 
The array becomes arr = [5, 7, -8, 0, 10, 1].
    
Second iteration (i = 0, j = 1): Compare 7 and -8. Since 7 is greater than -8, a swap occurs. 
The array becomes arr = [5, -8, 7, 0, 10, 1].
    
Third iteration (i = 0, j = 2): Compare 7 and 0. Since 7 is greater than 0, a swap occurs. 
The array becomes arr = [5, -8, 0, 7, 10, 1].
    
Fourth iteration (i = 0, j = 3): Compare 7 and 10. Since 7 is not greater than 10, no swap occurs.
    
Fifth iteration (i = 0, j = 4): Compare 10 and 1. Since 10 is greater than 1, a swap occurs. 
The array becomes arr = [5, -8, 0, 7, 1, 10].

List after Pass 1: [5, -8, 0, 7, 1, 10]

Pass 2:

First iteration (i = 1, j = 0): Compare 5 and -8. Since 5 is greater than -8, a swap occurs. 
The array becomes arr = [-8, 5, 0, 7, 1, 10].

Second iteration (i = 1, j = 1): Compare 5 and 0. Since 5 is greater than 0, a swap occurs. 
The array becomes arr = [-8, 0, 5, 7, 1, 10].

Third iteration (i = 1, j = 2): Compare 7 and 1. Since 7 is greater than 1, a swap occurs. 
The array becomes arr = [-8, 0, 5, 1, 7, 10].

Fourth iteration (i = 1, j = 3): Compare 7 and 10. Since 7 is not greater than 10, no swap occurs.

List after Pass 2: [-8, 0, 5, 1, 7, 10]

Pass 3:

First iteration (i = 2, j = 0): Compare -8 and 0. Since -8 is not greater than 0, no swap occurs.

Second iteration (i = 2, j = 1): Compare 0 and 5. Since 0 is not greater than 5, no swap occurs.

Third iteration (i = 2, j = 2): Compare 5 and 1. Since 5 is greater than 1, a swap occurs. 
The array becomes arr = [-8, 0, 1, 5, 7, 10].

List after Pass 3: [-8, 0, 1, 5, 7, 10]

Passes 4 and 5: No swaps occur in these passes since the array is already sorted.

Final sorted list: [-8, 0, 1, 5, 7, 10]

"""

def bubble_sort2(arr: List[int]) -> List[int]:
	N = len(arr)
	for i in range(0, N - 1):
		for j in range(0, N - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
print(bubble_sort2([2,6,5,1,9]))
print(bubble_sort2([7,5,-8,0,10,1]))

def bubble_sort3(arr: List[int]) -> List[int]:
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
print(bubble_sort3([7,5,-8,0,10,1]))

def bubble_sort3(arr: List[int]) -> List[int]:
	n = len(arr)
	for i in range(0, n - 1):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
print(bubble_sort3([7,5,-8,0,10,1]))
print(bubble_sort3([-10,6,-8,0,10,1]))
