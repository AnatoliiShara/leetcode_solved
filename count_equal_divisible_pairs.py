from typing import List

def countPairs(nums, k):
    count = 0   # Initialize a count variable to keep track of pairs that meet the conditions
    n = len(nums)   # Get the length of the nums array, which is 7 in this case
    
    for i in range(n):   # Outer loop iterates from i = 0 to i = 6
        for j in range(i + 1, n):   # Inner loop iterates from j = i + 1 to n - 1
            # Check if nums[i] is equal to nums[j] and if (i * j) % k is equal to 0
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1   # If both conditions are met, increment the count

    return count   # Return the final count

# Test case
nums1 = [3, 1, 2, 2, 2, 1, 3]
k1 = 2
print(countPairs(nums1, k1))  