class ListStack:
	def __init__(self):
		self.__stack = []   # 리시트 활용

	def push(self, x):
		self.__stack.append(x)

	def pop(self):
		return self.__stack.pop()

	def top(self):   # 탑 원소 리턴
		if self.isEmpty():
			return None
		else:
			return self.__stack[-1]

	def isEmpty(self) -> bool:
		return not bool(self.__stack)

	def popAll(self):
		self.__stack.clear() 

	def printStack(self):
		print("Stack from top:", end = ' ')
		for i in range(len(self.__stack)-1, -1, -1):
			print(self.__stack[i], end = ' ')
		print()
