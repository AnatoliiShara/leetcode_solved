"""
An n x n matrix is valid if every row and every column contains 
all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
"""

"""

"""



def is_valid_matrix(matrix):
    n = len(matrix)
    # Check rows
    for row in matrix:
        if len(set(row)) != n or any(x not in row for x in range(1, n+1)):
            return False
    # Check columns
    for j in range(n):
        column = [matrix[i][j] for i in range(n)]
        if len(set(column)) != n or any(x not in column for x in range(1, n+1)):
            return False
    
    return True

# Test cases
matrix1 = [[1,2,3],[3,1,2],[2,3,1]]
matrix2 = [[1,1,1],[1,2,3],[1,2,3]]

print(is_valid_matrix(matrix1))  # Output: True
print(is_valid_matrix(matrix2))  # Output: False
