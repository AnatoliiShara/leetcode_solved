from typing import List

def countPrefixes(words: List[str], s: str) -> int:
    c = 0
    for w in words:
        if s.startswith(w):
            c += 1
    return c
print(countPrefixes(["a","b","c","ab","bc","abc"],"abc"))

