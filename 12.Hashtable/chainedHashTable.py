from DS.list.circularLinkedList import *
from DS.list.listNode import *

class ChainedHashTable:
	def __init__(self, n):
		self.__table = [CircularLinkedList() for i in range(n)]   # 더미노드 n개 생성
		self.__numItems = 0;   # 총 노드 수

	def __hash(self, x:int):   # 편의상 int 타입으로 제한
		return x % len(self.__table)   # 나누기 방법 (테이블 크기를 2의 멱수에 가깝지 않은 소수로 택하는 것이 좋음)

	def insert(self, x:int):
		slot = self.__hash(x)
		self.__table[slot].insert(0, x)   # 0번 노드로 삽입
		self.__numItems += 1

	def search(self, x:int) -> ListNode:
		slot = self.__hash(x)
		if self.__table[slot].isEmpty():
			return None 
		else:
			head = prev = self.__table[slot].getNode(-1)   # 더미 헤드
			curr = prev.next    # 0번 노드
			while curr != head:
				if curr.item == x:
					return slot   # 인덱스 리턴
				else:
					prev = curr; curr = curr.next
			return None
	def delete(self, x:int):
		slot = self.__hash(x)
		success = self.__table[slot].remove(x)   # 원소가 x인 노드 삭제
		if success != None:
			self.__numItems -= 1
	def isEmpty(self):
		return self.__numItems == 0

	def clear(self):
		for i in range(len(self.__table)):
			self.__table[i] = CircularLinkedList()
		self.__numItems = 0

# 체이닝방법에서는 적재율 a가 1을 넘을 수 있음
# 탐색 횟수의 기대치는 a
# 이론적으로는 체이닝방법이 개방주소방법보다 좋음
# 적재율이 그리 높지 않은 경우 추가 공간이 필요하지 않는 개방주소방법 선호
