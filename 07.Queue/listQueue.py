class ListQueue:
	def __init__(self):
		self.__queue = []   # 리스트 활용

	def enqueue(self, x):
		self.__queue.append(x)

	def dequeue(self):
		return self.__queue.pop(0) 

	def front(self):   # 프론트 원소 리턴
		if self.isEmpty():
			return None
		else:
			return self.__queue[0]

	def isEmpty(self) -> bool:
		return (len(self.__queue) == 0);
 
	def dequeueAll(self):
		self.__queue.clear()

	def printQueue(self):
		print("Queue from front:", end = ' ')
		for i in range(len(self.__queue)):
			print(self.__queue[i], end = ' ')
		print()
