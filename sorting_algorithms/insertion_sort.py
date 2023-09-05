from typing import List


"""
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

For the provided input data [-3, 5, 0, -8, 1, 10], the insertion sort algorithm unfolds step by step:

Pass 1 (i = 1):

    Element at index 1 (5) is selected as the key element.
    The inner loop (j) starts from i and goes in reverse (j = 1 to 0).
    Compare the key element 5 with the element at index 0 (-3). 
    Since 5 > -3, no swap is required, and the sorted portion remains [-3, 5, 0, -8, 1, 10].

Pass 2 (i = 2):

    Element at index 2 (0) is chosen as the key element.
    The inner loop (j) starts from i and goes in reverse (j = 2 to 0).
    Compare the key element 0 with the element at index 1 (5). 
    Since 0 < 5, a swap occurs, resulting in the list becoming [-3, 0, 5, -8, 1, 10].
    Next, compare the swapped element (0) with the element at index 0 (-3). 
    As 0 > -3, no more swaps are necessary. The sorted portion now comprises [-3, 0, 5, -8, 1, 10].

Pass 3 (i = 3):

    Element at index 3 (-8) is selected as the key element.
    The inner loop (j) starts from i and goes in reverse (j = 3 to 0).
    Compare the key element -8 with the element at index 2 (5). 
    As -8 < 5, a swap occurs, leading to the list changing to [-3, 0, -8, 5, 1, 10].
    Subsequently, compare the swapped element (-8) with the element at index 1 (0). 
    Since -8 < 0, another swap takes place, resulting in the list becoming [-3, -8, 0, 5, 1, 10].
    Finally, compare the swapped element (-8) with the element at index 0 (-3). 
    As -8 < -3, yet another swap happens, and the sorted portion evolves into [-8, -3, 0, 5, 1, 10].

Pass 4 (i = 4):

    Element at index 4 (1) is chosen as the key element.
    The inner loop (j) starts from i and goes in reverse (j = 4 to 0).
    Compare the key element 1 with the element at index 3 (5). 
    Since 1 < 5, a swap takes place, leading to the list transforming into [-8, -3, 0, 1, 5, 10].
    Further, compare the swapped element (1) with the element at index 2 (0). 
    As 1 > 0, no additional swaps are required. The sorted portion expands to [-8, -3, 0, 1, 5, 10].

Pass 5 (i = 5):

    Element at index 5 (10) is already in its correct position within the sorted portion.
    No swaps are needed, and the final sorted list remains [-8, -3, 0, 1, 5, 10].

As the algorithm progresses through each pass (indicated by different values of 'i'), 
and within each pass, iterates through the inner loop (controlled by 'j'), the elements are meticulously positioned to form the sorted list [-8, -3, 0, 1, 5, 10], 
encapsulating the essence of insertion sort.
"""


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


























