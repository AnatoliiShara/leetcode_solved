# bubble sort
from typing import List
def bubble_sort(arr: List[int]):
    # O(n**2)
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def choice_sort(arr: List[int]):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i - 1
        cur_el = arr[i]
        while j >= 0 and cur_el < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur_el


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    less = [el for el in arr[:-1] if el < pivot]
    greater = [el for el in arr[:-1] if el >= pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quicksort_in(arr, start, end):
    if start < end:
        pivot_ind = partition(arr, start, end)
        quicksort_in(arr, start, pivot_ind - 1)
        quicksort_in(arr, pivot_ind + 1, end)

def merge_sorted_array(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    return merge_sort(arr[:middle]), merge_sort(arr[middle:])



if __name__ == '__main__':
    #nums  = [4, 8, 3, 1, 2]
    #bubble_sort(nums)
    #choice_sort(nums)
    #insertion_sort(nums)
    #print(quicksort(nums))
    #partition(nums, 0, len(nums) -1)
    #print(nums)
    #arr1 = [3, 4, 90]
    #arr2 = [1, 2, 3, 100]
    #print(merge_sorted_array(arr1, arr2))
    arr = [4, 1, 9, 3, 5, 0]
    print(merge_sort(arr))