from typing import List

"""
Pass 1:

    i = 0: Initialize min_ind with 0. Start inner loop from j = 1 to 5 (length of array - 1).
        Compare arr[1] (5) and arr[0] (7). Since 5 is less than 7, update min_ind to 1.
        Compare arr[2] (-8) and arr[1] (5). Since -8 is less than 5, update min_ind to 2.
        Compare arr[3] (0) and arr[2] (-8). Since -8 is less than 0, min_ind remains 2.
        Compare arr[4] (10) and arr[2] (-8). Since -8 is less than 10, min_ind remains 2.
        Compare arr[5] (1) and arr[2] (-8). Since -8 is less than 1, min_ind remains 2.
    Swap arr[0] (7) and arr[2] (-8), making the array arr = [-8, 5, 7, 0, 10, 1].

List after Pass 1: [-8, 5, 7, 0, 10, 1]

Pass 2:

    i = 1: Initialize min_ind with 1. Start inner loop from j = 2 to 5.
        Compare arr[2] (7) and arr[1] (5). Since 5 is less than 7, update min_ind to 1.
        Compare arr[3] (0) and arr[1] (5). Since 0 is less than 5, update min_ind to 3.
        Compare arr[4] (10) and arr[1] (5). Since 5 is less than 10, min_ind remains 3.
        Compare arr[5] (1) and arr[1] (5). Since 1 is less than 5, update min_ind to 5.
    Swap arr[1] (5) and arr[3] (0), making the array arr = [-8, 0, 7, 5, 10, 1].

List after Pass 2: [-8, 0, 7, 5, 10, 1]

Pass 3:

    i = 2: Initialize min_ind with 2. Start inner loop from j = 3 to 5.
        Compare arr[3] (5) and arr[2] (7). Since 5 is less than 7, update min_ind to 3.
        Compare arr[4] (10) and arr[2] (7). Since 7 is less than 10, min_ind remains 3.
        Compare arr[5] (1) and arr[2] (7). Since 1 is less than 7, update min_ind to 5.
    Swap arr[2] (7) and arr[5] (1), making the array arr = [-8, 0, 1, 5, 10, 7].

List after Pass 3: [-8, 0, 1, 5, 10, 7]

Pass 4:

    i = 3: Initialize min_ind with 3. Start inner loop from j = 4 to 5.
        Compare arr[4] (10) and arr[3] (5). Since 5 is less than 10, update min_ind to 3.
        Compare arr[5] (7) and arr[3] (5). Since 5 is less than 7, update min_ind to 5.
    Swap arr[3] (5) and arr[5] (7), but no change is needed since they are already in the correct order.

List after Pass 4: [-8, 0, 1, 5, 10, 7]

Pass 5:

    i = 4: Initialize min_ind with 4. Start inner loop from j = 5 to 5.
        Compare arr[5] (7) and arr[4] (10). Since 7 is less than 10, update min_ind to 5.

No swaps are needed in this pass since the array is already sorted.

Final sorted list: [-8, 0, 1, 5, 7, 10]
"""

def choice_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr
print(choice_sort([7,5,-8,0,10,1]))

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, j):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr

def choice_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr
    



































































