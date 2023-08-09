from typing import List

def calPoints(operations: List[str]) -> int:
	stack = []
	for operation in operations:
		if operation == "D":
			stack.append(int(stack[-1]) * 2)
		elif operation == "C":
			stack.pop()
		elif operation == "+":
			stack.append(int(stack[-1] + stack[-2]))
		else:
			stack.append(int(operation))
	return sum(stack)
print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))














