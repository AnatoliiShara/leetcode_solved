"""
This function iterates through each word in the words array. 
For each word, it checks if every character in the word is present in the allowed string. 
If all characters are in allowed, the word is considered consistent, and the count is incremented.

Let's break down how the function works for the provided examples:

Example 1:

For the word "ad", both characters 'a' and 'b' are in the allowed string "ab," so it's consistent.
For the word "bd," both characters 'b' and 'a' are in "ab," so it's consistent.
For the word "aaab," all characters 'a' and 'b' are in "ab," so it's consistent.
For the word "baa," all characters 'a' and 'b' are in "ab," so it's consistent.
For the word "badab," characters 'b,' 'a,' and 'd' are in "ab," but 'd' is not in "ab," 
so it's not consistent.
The final count is 2, indicating that there are two consistent strings.

Example 2:

All words contain only characters 'a,' 'b,' and 'c,' which are present in the allowed string "abc." 
Therefore, all strings are consistent.
The final count is 7, indicating that all strings are consistent.

Example 3:

For the word "cc," both characters 'c' and 'a' are in the allowed string "cad," so it's consistent.
For the word "acd," all characters 'a,' 'c,' and 'd' are in "cad," so it's consistent.
For the word "ac," both characters 'a' and 'c' are in "cad," so it's consistent.
For the word "d," character 'd' is in "cad," so it's consistent.
For the other words, at least one character is not in "cad," so they are not consistent.
The final count is 4, indicating that there are four consistent strings.

The function correctly counts the consistent strings for the provided examples.
"""

from typing import List

def countConsistentStrings(allowed, words):
    count = 0  # Initialize a count variable to keep track of consistent strings
    
    for word in words:
        consistent = True  # Assume the word is consistent initially
        for char in word:
            if char not in allowed:
                consistent = False  # If a character is not in 'allowed', mark the word as inconsistent
                break
        if consistent:
            count += 1  # If the word is consistent, increment the count
    
    return count  # Return the count of consistent strings

# Test cases
allowed1 = "ab"
words1 = ["ad", "bd", "aaab", "baa", "badab"]
print(countConsistentStrings(allowed1, words1))  # Output: 2

allowed2 = "abc"
words2 = ["a", "b", "c", "ab", "ac", "bc", "abc"]
print(countConsistentStrings(allowed2, words2))  # Output: 7

allowed3 = "cad"
words3 = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
print(countConsistentStrings(allowed3, words3))  # Output: 4
