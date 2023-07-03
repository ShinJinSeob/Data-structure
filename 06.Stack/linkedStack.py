from DS.list.linkedListBasic import LinkedListBasic

class LinkedStack:
	def __init__(self):
		self.__list = LinkedListBasic()   # 연결리스트 활용

	def push(self, newItem):
		self.__list.insert(0, newItem)   # 0번 노드로 삽입

	def pop(self):
		return self.__list.pop(0)   # 0번 노드 삭제

	def top(self):   # 탑 원소 리턴
		if self.isEmpty():
			return None
		else:
			return self.__list.get(0)

	def isEmpty(self) -> bool:
		return self.__list.isEmpty()

	def popAll(self):
		self.__list.clear()

	def printStack(self):
		print("Stack from top:", end = '')
		for i in range(self.__list.size()):
			print(self.__list.get(i), end = '')
		print()
