from typing import List

def countWords(words1: List[str], words2: List[str]) -> int:
    c = 0
    for i in words1:
        if words1.count(i) == words2.count(i) == 1:
            c += 1
    return c

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

print(countWords(words1, words2))

def countWords100(words1: List[str], words2: List[str]) -> int:
    def countOccurrences(words):
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count
    word_count1 = countOccurrences(words1)
    word_count2 = countOccurrences(words2)
    count = 0
    for word, count1 in word_count1.items():
        if count1 == 1 and word_count2.get(word, 0) == 1:
            count += 1
    return count
print(countWords100(words1, words2))