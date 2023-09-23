
"""
Initialize variables:
        n is 7.
        right starts at 0.
        pairs is initially 0.
        count is initialized to 0.
        counter is a Counter object with the initial counts of elements in the subarray [3].

Start iterating through the array with the left pointer at index 0.

    Enter a while loop:
        right advances to index 1.
        pairs remains 0.
        counter is updated to {3: 1} since it counts the number of occurrences of elements 
        within the current subarray.

    Check if pairs is greater than or equal to k:
        Not satisfied (0 is not greater than or equal to 2).

    Increment count:
        count remains 0.

    Move the left pointer to index 1:
        left is now at index 1.

    Repeat steps 3-6 in the while loop:
        right advances to index 3.
        pairs becomes 1 (since there is one pair of 3's).
        counter is updated to {3: 2, 1: 1} as it counts elements within the current subarray.

    Check if pairs is greater than or equal to k:
        Not satisfied (1 is not greater than or equal to 2).

    Increment count:
        count remains 0.

    Move the left pointer to index 2:
        left is now at index 2.

    Repeat steps 3-6 in the while loop:
        right advances to index 4.
        pairs becomes 2 (since there are two pairs of 2's).
        counter is updated to {3: 2, 1: 1, 4: 1, 2: 1} as it counts elements within the current subarray.

    Check if pairs is greater than or equal to k:
        Satisfied (2 is greater than or equal to 2).

    Increment count:
        count becomes 1 (initial value + 1).

    Move the left pointer to index 3:
        left is now at index 3.

    Repeat steps 3-6 in the while loop:
        right advances to index 5.
        pairs becomes 3 (since there are three pairs of 2's).
        counter is updated to {3: 2, 1: 1, 4: 1, 2: 2} as it counts elements 
        within the current subarray.

    Check if pairs is greater than or equal to k:
        Satisfied (3 is greater than or equal to 2).

    Increment count:
        count becomes 2 (previous value + 1).

    Move the left pointer to index 4:
        left is now at index 4.

    Repeat steps 3-6 in the while loop:
        right advances to index 6.
        pairs becomes 4 (since there are four pairs of 2's).
        counter is updated to {3: 2, 1: 1, 4: 2, 2: 2} as it counts elements 
        within the current subarray.

    Check if pairs is greater than or equal to k:
        Satisfied (4 is greater than or equal to 2).

    Increment count:
        count becomes 3 (previous value + 1).

    Move the left pointer to index 5:
        left is now at index 5.

    The process continues until the left pointer reaches the end of the array.

    Finally, return count, which is 3.

In summary, pairs represents the count of pairs of equal elements 
within the current subarray defined by the left and right pointers. 
It is initially 0 and increases as equal elements are encountered 
and decreases when elements are removed from the subarray by moving the left pointer.
"""


from typing import List
from collections import Counter

def countGood(nums: List[int], k: int) -> int:
    n = len(nums)
    right = 0
    pairs = 0
    count = 0
    counter = Counter()
    for left in range(n):
        while right < n and pairs < k:
            pairs += counter[nums[right]]
            counter[nums[right]] += 1
            right += 1
        if pairs >= k:
            count += n - right + 1
        counter[nums[left]] -= 1
        pairs -= counter[nums[left]]
    return count

print(countGood([3,1,4,3,2,2,4],2))
# Test cases
nums1 = [1, 1, 1, 1, 1]
k1 = 10
print(countGood(nums1, k1))  # Output: 1

nums2 = [3, 1, 4, 3, 2, 2, 4]
k2 = 2
print(countGood(nums2, k2))  # Output: 4

