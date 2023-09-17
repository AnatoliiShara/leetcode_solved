
"""
- first pair of indices [rowi, coli] [0,1] - 
it means that we have to increment by 1 the first row as "0" here means "first row", 
so matrix will look like this [[1, 1, 1], [0, 0, 0]] 

after that as we have "1" as coli we have to increment by 1 the second column as "1' 
here means the second column, 
so matrix will be look like this [ [1,2,1], [0, 1, 0]], 

- the second pair of  [rowi, coli] [1,1] - 
it means that we have to increment by the second row as "1" here means "second row", 
so matrix will look like [ [1,2,1], [1, 2, 1]], 
after that we have to increment the 2 column as "1" here means "second column", 
so matrix will look like [[1,3,1], [1, 3, 1]]


[[1, 3, 1],
 [1, 3, 1]]

Here's how you can identify the odd-valued cells:

    The cell at position [0, 0] is 1, which is odd.
    The cell at position [0, 1] is 3, which is odd.
    The cell at position [0, 2] is 1, which is odd.
    The cell at position [1, 0] is 1, which is odd.
    The cell at position [1, 1] is 3, which is odd.
    The cell at position [1, 2] is 1, which is odd.

There are six cells in the matrix that have odd values. 
Each of these cells corresponds to a location in the matrix 
where an increment operation has been performed an odd number of times. 
Hence, the result of 6 is obtained by counting the total number of odd-valued cells in the matrix.
"""

from typing import List

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	row = [0 for _ in range(n)]
	col = [0 for _ in range(m)]
	# inc. corresponding row and col 
	for rowi, coli in indices:
		row[rowi] += 1 
		col[coli] += 1
	res = 0 
	for i in range(n):
		for j in range(m):
			if (row[i] + col[j]) % 2 == 1:
				res += 1
	return res
print(oddCells(2,3, [[0,1], [1,1]]))

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	row = [0 for _ in range(n)]
	col = [0 for _ in range(m)]
	for rowi, coli in indices:
		row[rowi] += 1
		col[coli] += 1
	res = 0 
	for i in range(n):
		for j in range(m):
			if (row[i] + col[j]) % 2 == 1:
				res += 1
	return res 

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	row = [0 for _ in range(n)]
	col = [0 for _ in range(m)]
	for rowi, coli in indices:
		row[rowi] += 1
		col[coli] += 1
	res = 0
	for i in range(n):
		for j in range(m):
			if (row[i] + col[j]) % 2 == 1:
				res += 1
	return res

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	row, col = [0] * n, [0] * m 
	for rowi, coli in indices:
		row[rowi] += 1
		col[coli] += 1
	res = 0
	for i in range(n):
		for j in range(m):
			if (row[i] + col[j]) % 2 == 1:
				res += 1
	return res 

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	matrix = [[0] * m for _ in range(n)]
	for r, c in indices:
		for i in range(m):
			matrix[r][i] += 1
		for j in range(n):
			matrix[c][j] += 1
	odd_count = 0
	for row in matrix:
		for cell in row:
			if cell % 2 == 1:
				odd_count += 1
	return odd_count
print(oddCells(2,3, [[0,1], [1,1]]))

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
	matrix = [[0] * m for _ in range(n)]
	for row, col in indices:
		for i in range(m):
			matrix[row][i] += 1
		for j in range(n):
			matrix[col][j] += 1
	odd_count = 0 
	for row in matrix:
		for cell in row:
			if cell % 2 == 1:
				odd_count += 1
	return odd_count




















































































