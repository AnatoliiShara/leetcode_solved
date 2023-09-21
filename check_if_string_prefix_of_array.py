from typing import List

def isPrefixString(s: str, words: List[str]) -> bool:
    prefix = ""
    for word in words:
        prefix += word
        if prefix == s:
            return True
        if len(prefix) >= len(s):
            break
    return False

s = "iloveleetcode" 
words = ["i","love","leetcode","apples"]
print(isPrefixString(s, words))

def isPrefixString2(s: str, words: List[str]) -> bool:
    prefix = ""
    for word in words:
        prefix += word
        if prefix == s:
            return True
        if not s.startswith(prefix):
            break
    return False

s2 = "iloveleetcode" 
words2 = ["i","love","leetcode","apples"]
print(isPrefixString(s2, words2))