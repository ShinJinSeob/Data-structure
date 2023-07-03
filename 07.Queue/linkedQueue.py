from DS.list.circularLinkedList import CircularLinkedList

class LinkedQueue:
	def __init__(self):
		self.__queue = CircularLinkedList()   # 연결리스트 활용

	def enqueue(self, x):
		self.__queue.append(x)   # 끝 노드 삽입

	def dequeue(self):
		return self.__queue.pop(0)   # 0번 노드 삭제

	def front(self):   # 프론트 원소 리턴
		return self.__queue.get(0) 

	def isEmpty(self) -> bool:
		return self.__queue.isEmpty()
 
	def dequeueAll(self):
		self.__queue.clear()
	def printQueue(self):
		print("Queue from front:", end = ' ')
		for i in range(self.__queue.size()):
			print(self.__queue.get(i), end = ' ')
		print()
