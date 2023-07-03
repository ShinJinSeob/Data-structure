class Heap:   # 조건1. 완전 이진 트리,  조건2. 모든 노드는 자식 노드보다 크거나 같음
	def __init__(self, *args):
		if len(args) != 0:
			self.__A = args[0] # 파라미터로 온 리스트
		else:
			self.__A = []
 
	def insert(self, x):   # 삽입
		self.__A.append(x)
		self.__percolateUp(len(self.__A)-1)

	def __percolateUp(self, i:int):   # 스며오르기
		parent = (i - 1) // 2
		if i > 0 and self.__A[i] > self.__A[parent]:
			self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
			self.__percolateUp(parent)

	def deleteMax(self):   # 리프 노드 삭제
		if (not self.isEmpty()):
			max = self.__A[0]
			self.__A[0] = self.__A.pop()   # 힙의 끝 원소 삭제 후 리프 노드로 리턴
			self.__percolateDown(0)
			return max
		else:
			return None

	def __percolateDown(self, i:int):   # 스며내리기
		child = 2 * i + 1    # 왼자식
		right = 2 * i + 2    # 오른자식
		if (child <= len(self.__A)-1):
			if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
				child = right   # 오른자식을 자식 노드로 변경 (if절 거짓일 시 왼자식 자식 노드로 유지)
			if self.__A[i] < self.__A[child]:
				self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
				self.__percolateDown(child)

	def max(self):
		return self.__A[0]

	def buildHeap(self):   # 리스트를 힙으로
		for i in range((len(self.__A) - 2) // 2, -1, -1):
			self.__percolateDown(i)

	def isEmpty(self) -> bool:
		return len(self.__A) == 0

	def clear(self):
		self.__A = []

	def size(self) -> int:
		return len(self.__A)
