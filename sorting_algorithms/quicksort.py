
from typing import List

"""
Initial Array: [7, 5, -8, 0, 10, 1]

Choosing a Pivot: Quicksort begins by selecting a pivot element from the array. 
In this example, we'll choose the last element, which is 1.

Partitioning: 
The array is then partitioned into two subarrays: 
elements less than the pivot and elements greater than the pivot.
Elements less than the pivot: [-8, 0]
Pivot element: 1
Elements greater than the pivot: [7, 5, 10]
Recursion: Quicksort is applied recursively to the two subarrays:
For the subarray [-8, 0]:
    Pivot: 0
    Partitioned subarrays: [-8] (less than) and [0] (greater than)
    Subarray [-8] is sorted.
    Subarray [0] is sorted.

For the subarray [7, 5, 10]:
    Pivot: 10
    Partitioned subarrays: [7, 5] (less than) and [10] (greater than)

    Subarray [7, 5] is further partitioned:
        Pivot: 5
        Partitioned subarrays: [5] (less than) and [7] (greater than)
        Both subarrays are sorted.
    Subarray [10] is sorted.
Combining: The sorted subarrays are combined to produce the final sorted array.

Final sorted array: [-8, 0, 1, 5, 7, 10]
"""

def quicksort(arr):
    # Base case: If the array is empty or has one element, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (in this example, we'll choose the last element).
    pivot = arr[-1]

    # Partition the array into elements less than and greater than the pivot.
    less_than_pivot = []
    greater_than_pivot = []

    for element in arr[:-1]:
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)

    # Recursively sort the subarrays and combine them with the pivot.
    sorted_less = quicksort(less_than_pivot)
    sorted_greater = quicksort(greater_than_pivot)

    # Combine the sorted subarrays and the pivot to get the final sorted array.
    return sorted_less + [pivot] + sorted_greater
# Example usage:
arr = [7, 5, -8, 0, 10, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)

"""Explanation:

The quicksort function takes an array arr as input.
In the base case, if the array has one element or is empty, 
it's considered sorted, and we return the array.
We choose a pivot element, which in this example, is the last element of the array (pivot = arr[-1]).
We partition the array into two subarrays: 
less_than_pivot for elements less than or equal to the pivot and greater_than_pivot 
for elements greater than the pivot.
We recursively apply the quicksort function to both subarrays and
 combine them with the pivot to obtain the final sorted array.
Finally, we demonstrate the usage of the quicksort function 
by sorting an example array [7, 5, -8, 0, 10, 1].
"""

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less_than_pivot, greater_than_pivot = [], []
    for element in arr[:-1]:
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)
    sorted_less, sorted_greater = quicksort(less_than_pivot), quicksort(greater_than_pivot)
    return sorted_less + [pivot] + sorted_greater
arr = [7, 5, -8, 0, 10, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)









































































































print(sorted_arr)













print(sorted_arr)






























