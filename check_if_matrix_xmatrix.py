"""
Now, let's break down the input data grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]] 
to see how the function processes it:

The outer loop (for i in range(4)) and the inner loop (for j in range(4)) traverse through each element of the 4x4 matrix.

The first iteration (i = 0, j = 0) checks the element at the top-left corner. 
Since this is a diagonal element (i == j), the function checks if it is non-zero. 
In this case, grid[0][0] is 2, which is non-zero, so the condition is satisfied.

The second iteration (i = 0, j = 1) checks the element in the top row, second column. 
Since this is not a diagonal element (i != j), the function checks if it is zero. 
In this case, grid[0][1] is 0, which is zero, so the condition is satisfied.

The function continues to iterate through all other elements in a similar manner, 
checking diagonal and non-diagonal elements against their respective conditions.

Throughout this process, the function encounters elements on both the main diagonal 
and the secondary diagonal and 
correctly verifies that diagonal elements are non-zero (2, 3, 2, 2) 
and that non-diagonal elements are zero (0, 0, 0, 0).

Since the function successfully checks all elements in the matrix 
and finds that they meet the criteria for an X-Matrix, it returns True, 
indicating that the input matrix grid is indeed an X-Matrix.

Main Diagonal (i == j):
    When i (the row index) is equal to j (the column index), 
    it indicates that the current element is on the main diagonal of the matrix.
    The main diagonal runs from the top-left corner to the bottom-right corner.
    For example, in a 4x4 matrix, 
    elements at positions (0, 0), (1, 1), (2, 2), and (3, 3) are on the main diagonal.

Secondary Diagonal (j == n - i - 1):
When j (the column index) is equal to n - i - 1 
(where n is the size of the matrix and i is the row index), 
it indicates that the current element is on the secondary diagonal of the matrix.
The secondary diagonal runs from the top-right corner to the bottom-left corner.
For example, in a 4x4 matrix, elements at positions (0, 3), (1, 2), (2, 1), and (3, 0) 
are on the secondary diagonal.
"""

from typing import List

def checkXMatrix(grid: List[List[int]]) -> bool:
    n = len(grid)
    # The outer loop (i) iterates through rows of the matrix.
    for i in range(n):
        # The inner loop (j) iterates through columns of the matrix.
        for j in range(n):
            # Check if this is a diagonal element because X-Matrix has two diagonals:
            # - The main diagonal (top-left to bottom-right) where i == j.
            # - The secondary diagonal (top-right to bottom-left) where j == n - i - 1.
            if j == i or j == n - i - 1:
                # Make sure that diagonal elements are non-zero.
                if grid[i][j] == 0:
                    # If a diagonal element is zero, return False, indicating that the matrix is not an X-Matrix.
                    return False
            else:
                # For elements outside both diagonals:
                # Make sure that these elements are zero because X-Matrix should have all other elements as zeros.
                if grid[i][j] != 0:
                    # If a non-diagonal element is non-zero, return False, indicating that the matrix is not an X-Matrix.
                    return False
    # If no problems were found after checking all elements in the matrix, return True,
    # indicating that the input matrix is indeed an X-Matrix.
    return True
print(checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
