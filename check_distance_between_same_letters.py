from typing import List

def check_distance(s: str, distance: List[int]) -> bool:
    char_indices = {}
    for i, char in enumerate(s):
        char_idx = ord(char) - ord("a")
        if char_idx in char_indices:
            if i - char_indices[char_idx] - 1 != distance[char_idx]:
                return False
        char_indices[char_idx] = i
    return False