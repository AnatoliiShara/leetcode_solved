from typing import List
from collections import Counter

def findLHS(nums: List[int]) -> int:
	counter = Counter(nums)
	max_summa = 0
	for key, value in counter.items():
		summa = value 
		if (key + 1) in counter:
			summa += counter[key + 1]
			if summa > max_summa:
				max_summa = summa
	return max_summa
print(findLHS([1,3,2,2,5,2,3,7]))