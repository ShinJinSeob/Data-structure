class TreeNode:
	def __init__(self, newItem, left, right):
		self.item = newItem
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.__root = None   # 루트 레퍼런스

	def search(self, x) -> TreeNode:   # 검색
		return self.__searchItem(self.__root, x)

	def __searchItem(self, tNode:TreeNode, x) -> TreeNode:   # 루트가 tnode인 트리에서 x가 원소인 노드 리턴
		if (tNode == None):
			return None
		elif (x == tNode.item):
			return tNode
		elif (x < tNode.item):
			return self.__searchItem(tNode.left, x)
		else:
			return self.__searchItem(tNode.right, x)

	def insert(self, newItem):   # 삽입
		self.__root = self.__insertItem(self.__root, newItem)   # 레퍼런스 재지정 (삽입 노드와 부모 노드 연결하기 위함)

	def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
		if (tNode == None):   # 검색 실패
			tNode = TreeNode(newItem, None, None)
		elif (newItem < tNode.item):
			tNode.left = self.__insertItem(tNode.left, newItem)   # 레퍼런스 재지정 (삽입 노드와 부모 노드 연결하기 위함)
		else:
			tNode.right = self.__insertItem(tNode.right, newItem)   # 레퍼런스 재지정 (삽입 노드와 부모 노드 연결하기 위함)
		return tNode

	def delete(self, x):   # 삭제
		self.__root = self.__deleteItem(self.__root, x)   # 레퍼런스 재지정 (삭제 노드의 자식 노드와 부모 노드 연결하기 위함)
	
	def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
		if (tNode == None):   # 검색 실패
			return None
		elif (x == tNode.item):   # 검색 성공
				tNode = self.__deleteNode(tNode)
		elif (x < tNode.item):
				tNode.left = self.__deleteItem(tNode.left, x)   # 레퍼런스 재지정 (삭제 노드의 자식 노드와 부모 노드 연결하기 위함)
		else:
				tNode.right = self.__deleteItem(tNode.right, x)   # 레퍼런스 재지정 (삭제 노드의 자식 노드와 부모 노드 연결하기 위함)
		return tNode   # tNode: 부모 노드에 매달리는 노드

	def __deleteNode(self, tNode:TreeNode) -> TreeNode:   # 삭제 후처리
		# 3가지 case
		#  1. tNode가 리프 노드
		#  2. tNode가 자식이 하나
		#  3. tNode가 자식이 둘 
		if tNode.left == None and tNode.right == None:   # case 1
			return None
		elif tNode.left == None:   # case 2 (오른자식뿐)
			return tNode.right
		elif tNode.right == None:   # case 2 (왼자식뿐)
			return tNode.left
		else:   # case 3
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)   # (오른쪽 서브트리의 최솟값, tnode의 오른자식)
			tNode.item = rtnItem
			tNode.right = rtnNode    # 레퍼런스 재지정 (삭제 노드의 자식 노드와 부모 노드 연결하기 위함)
			return tNode

	def __deleteMinItem(self, tNode:TreeNode) -> tuple:
		if tNode.left == None:   # 최소 노드 검색
			return (tNode.item, tNode.right)
		else:
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
			tNode.left = rtnNode   # 레퍼런스 재지정 (rttNode와 부모 노드 연결하기 위함)
			return (rtnItem, tNode)

	def isEmpty(self) -> bool:
		return self.__root == self.NIL

	def clear(self):
		self.__root = self.NIL
