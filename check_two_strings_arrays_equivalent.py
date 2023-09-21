from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
	str1 = ""
	str2 = ""
	for i in word1:
		str1 += i 
	for j in word2:
		str2 += j 
	return bool(str1 == str2)
print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))

def arrayStringsAreEqual2(word1: List[str], word2: List[str]) -> bool:
    return "".join(word1) == "".join(word2)
print(arrayStringsAreEqual2(["ab", "c"], ["a", "bc"]))