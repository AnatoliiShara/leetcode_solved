from typing import List

"""
Now, let's explain how the code works with the given input:

seen is initialized as an empty set.

The for loop iterates through the elements of the input array arr, 
starting with the first element, which is 10.

For num = 10:
The code checks if num * 2, which is 20, is in the seen set. 
Since it's not in the set (it's the first element encountered), 
the first part of the condition is not met.
The code also checks if num is even (num % 2 == 0) and if num // 2, which is 5, is in the seen set. 
Again, this condition is not met.
Therefore, the code adds 10 to the seen set and continues to the next element.

For num = 2:
The code checks if num * 2, which is 4, is in the seen set. 
Since it's not in the set, the first part of the condition is not met.
The code also checks if num is even (num % 2 == 0) and if num // 2, which is 1, is in the seen set. This condition is not met either.
2 is added to the seen set, and the loop continues.

For num = 5:
The code checks if num * 2, which is 10, is in the seen set.
This condition is met because 10 was added to the seen set earlier when num was 10.
Since the condition is met, 
the function returns True because we've found two indices i and j such that i != j and arr[i] == 2 * arr[j].

The result True is printed to the console 
because the code successfully found a pair of indices that 
meet the specified conditions in the input array [10, 2, 5, 3].
"""

def checkIfDoubleExists(arr):
    seen = set()  # Create an empty set called 'seen' to store encountered elements.

    for num in arr:  # Iterate through the elements in the input array 'arr'.
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            # Check if either of the following conditions is met:
            # 1. 'num * 2' is already in the 'seen' set, meaning we found 'i' and 'j' where 'arr[i] == 2 * arr[j]'.
            # 2. 'num' is even ('num % 2 == 0') and 'num // 2' is in the 'seen' set, meaning we found 'i' and 'j' where 'arr[i] == 2 * arr[j]'.
            return True  # Return True if either condition is met.
        seen.add(num)  # If the conditions are not met, add the current element 'num' to the 'seen' set.

    return False  # If we finish iterating through the array without finding a pair of indices that meet the conditions, return False.

# Using the input array 'arr' to check for the specified conditions.
arr = [10, 2, 5, 3]
result = checkIfDoubleExists(arr)
print(result)  # Output: True (Explanation below)








