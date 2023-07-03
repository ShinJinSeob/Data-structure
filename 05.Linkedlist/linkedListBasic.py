from DS.list.listNode import ListNode

class LinkedListBasic:
	def __init__(self):
		self.__head = ListNode('dummy', None)   # 헤드 레퍼런스
		self.__numItems = 0   # 더미 노드 제외 노드 수

	def __getNode(self, i:int) -> ListNode:   # i번 노드 리턴
		curr = self.__head 
		for index in range(i+1):
			curr = curr.next
		return curr   

	def get(self, i:int):   # i번 노드 원소 리턴
		if self.isEmpty():
			return None
		if (i >= 0 and i <= self.__numItems - 1):
			return self.__getNode(i).item
		else:
			return None
	
	def __findNode(self, x) -> (ListNode, ListNode):   # (원소가 x인 노드의 직전 노드, 원소가 x인 노드) 리턴
		prev = self.__head 
		curr = prev.next
		while curr != None:
			if curr.item == x:
				return (prev, curr)
			else:
				prev = curr; curr = curr.next
		return (None, None)
		
	def insert(self, i:int, newItem):   # 노드 삽입 (인덱스, 원소)
		if i >= 0 and i <= self.__numItems:
			prev = self.__getNode(i - 1)
			newNode = ListNode(newItem, prev.next)
			prev.next = newNode
			self.__numItems += 1   
		else:
			print("index", i, ": out of bound in insert()")
 
	def append(self, newItem):   # 끝에 노드 삽입
		prev = self.__getNode(self.__numItems - 1)
		newNode = ListNode(newItem, prev.next)
		prev.next = newNode
		self.__numItems += 1 

	def pop(self, i:int):   # i번 노드 삭제, 리턴
		if (i >= 0 and i <= self.__numItems-1):
			prev = self.__getNode(i - 1)
			curr = prev.next
			prev.next = curr.next
			retItem = curr.item
			self.__numItems -= 1 
			return retItem 
		else:
			return None
	
	def remove(self, x):   # 원소가 x인 노드 삭제
		(prev, curr) = self.__findNode(x)
		if curr != None:
			prev.next = curr.next
			self.__numItems -= 1
			return x   
		else:
			return None
 
	def index(self, x) -> int:   # 원소가 x인 노드의 인덱스 리턴
		curr = self.__head.next	 
		for index in range(self.__numItems):
			if curr.item == x:
				return index
			else:
				curr = curr.next
		return -2 

	def isEmpty(self) -> bool:   # 리스트 비어있는지 확인 (비어있으면 1 리턴)
		return self.__numItems == 0

	def size(self) -> int:   # 총 노드 수
		return self.__numItems

	def clear(self):    # 리스트 비우기
		self.__head = ListNode("dummy", None)
		self.__numItems = 0

	def count(self, x) -> int:   # 원소가 x인 노드 수
		cnt = 0
		curr = self.__head.next
		while curr != None:
			if curr.item == x:
					cnt += 1
			curr = curr.next
		return cnt

	def extend(self, a):   # 연결리스트 a를 연장
		for index in range(a.size()):
			self.append(a.get(index))
 
	def copy(self):   #연결리스트 복사
		a = LinkedListBasic()
		for index in range(self.__numItems):
			a.append(self.get(index))
		return a

	def reverse(self):   #연결리스트 거꾸로
		a = LinkedListBasic()
		for index in range(self.__numItems):
			a.insert(0, self.get(index))
		self.clear()
		for index in range(a.size()):
			self.append(a.get(index))

	def sort(self) -> None:   #연결리스트 정렬
		a = []
		for index in range(self.__numItems):
			a.append(self.get(index))
		a.sort()
		self.clear()
		for index in range(len(a)):
			self.append(a[index])

	def printList(self):   #연결리스트 출력
		curr = self.__head.next
		while curr != None:
			print(curr.item, end = ' ')
			curr = curr.next
		print()
