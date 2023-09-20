from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    output = []
    for num in nums1:
        for j in range(len(nums2)):
            if num == nums2[j]:
                break
        greater_found = False
        for k in range(j + 1, len(nums2)):
            if nums2[k] > num:
                greater_found = True
                output.append(nums2[k])
                break
        if not greater_found:
            output.append(-1)
    return output
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))




def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    for num in nums1:
        for i in range(len(nums2)):
            if nums2[i] == num:
                find_num = -1
                for k in range(i + 1, len(nums2)):
                    if nums2[k] > nums2[i]:
                        find_num = nums2[k]
                        break
                stack.append(find_num)
                break
    return stack