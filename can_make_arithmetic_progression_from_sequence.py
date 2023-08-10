from typing import List

def canFormArithmeticProgression(arr: List[int]):
    arr.sort()  # Sort the array in ascending order
    diff = arr[1] - arr[0]  # Calculate the common difference between elements
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False  # If the difference is not constant, return False
    return True  # If all differences are the same, return True
print(canFormArithmeticProgression([3, 5, 1]))  # Output: True

















