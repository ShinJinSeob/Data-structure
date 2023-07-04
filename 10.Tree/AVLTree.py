class AVLNode:
	def __init__(self, newItem, left, right, h):
		self.item = newItem
		self.left = left
		self.right = right
		self.height = h   # 트리 높이
 
class AVLTree:
	def __init__(self):
		self.NIL = AVLNode(None, None, None, 0)
		self.__root = self.NIL   # 루트 레퍼런스
		self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4
		# LL유형: t.left.left가 가장 깊음
		# LR유형: t.left.right가 가장 깊음
		# RR유형: t.right.right가 가장 깊음
		# RL유형: t.right.left가 가장 깊음
		self.NO_NEED = 0;   # 균형 잡기 필요 없음
		self.ILLEGAL = -1   # 유형 파악 안 됨

	def search(x):   # 검색
		return self.__SearchItem(self.root,x)

	def __searchItem(self, tNode:AVLNode, x) -> AVLNode:
		if tNode == self.NIL: 
			return self.NIL
		elif x == tNode.item:
			return tNode
		elif x < tNode.item:
			return self.__searchItem(tNode.left, x)
		else:
			return self.__searchItem(tNode.right, x)

	def insert(self, x):   # 삽입
		self.__root = self.__insertItem(self.__root, x)

	def __insertItem(self, tNode:AVLNode, x) -> AVLNode:
		if tNode == self.NIL:   # 검색 실패
			tNode = AVLNode(x, self.NIL, self.NIL, 1)
		elif x < tNode.item:
			tNode.left = self.__insertItem(tNode.left, x)
			# 후처리
			tNode.height = 1 + max(tNode.right.height, tNode.left.height)
			type = self.__needBalance(tNode)
			if (type != self.NO_NEED):
				tNode = self.__balanceAVL(tNode, type)
		else: 
			tNode.right = self.__insertItem(tNode.right, x)
			# 후처리
			tNode.height = 1 + max(tNode.right.height, tNode.left.height)
			type = self.__needBalance(tNode)
			if type != self.NO_NEED:
				tNode = self.__balanceAVL(tNode, type)
		return tNode

	def delete(self, x):   # 삭제
		self.__root = self.__deleteItem(self.__root, x)

	def __deleteItem(self, tNode:AVLNode, x) -> AVLNode:
		if tNode == self.NIL:   # 검색 실패
			return self.NIL
		else:
			if x == tNode.item:   # 검색 성공
				tNode = self.__deleteNode(tNode)
			elif x < tNode.item:
				tNode.left = self.__deleteItem(tNode.left, x)
				# 후처리
				tNode.height = 1 + max(tNode.right.height, tNode.left.height)
				type = self.__needBalance(tNode)
				if type != self.NO_NEED:
					tNode = self.__balanceAVL(tNode, type)
			else:
				tNode.right = self.__deleteItem(tNode.right, x)
				# 후처리
				tNode.height = 1 + max(tNode.right.height, tNode.left.height)
				type = self.__needBalance(tNode)
				if type != self.NO_NEED:
					tNode = self.__balanceAVL(tNode, type)
			return tNode

	def __deleteNode(self, tNode:AVLNode) -> AVLNode:
		# 3가지 case
		#     1. tNode가 리프 노드
		#     2. tNode가 자식이 하나
		#     3. tNode가 자식이 둘
		if tNode.left == self.NIL and tNode.right == self.NIL:   # case 1
			return self.NIL
		elif tNode.left == self.NIL:   # case 2 (오른자식뿐)
			return tNode.right
		elif tNode.right == self.NIL:   # case 2 (왼자식뿐)
			return tNode.left
		else:   # case 3
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)   # (오른쪽 서브트리의 최솟값, tnode의 오른자식)
			tNode.item = rtnItem
			tNode.right = rtnNode
			# 후처리
			tNode.height = 1 + max(tNode.right.height, tNode.left.height)
			type = self.__needBalance(tNode)
			if type != self.NO_NEED:
				tNode = self.__balanceAVL(tNode, type)
			return tNode

	def __deleteMinItem(self, tNode:AVLNode) -> tuple:
		if tNode.left == self.NIL:   # 최소 노드 검색 성공
			return (tNode.item, tNode.right)
		else: # keep branching left, then backtrack
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)   # (오른쪽 서브트리의 최솟값, tnode의 왼자식)
			tNode.left = rtnNode
			# 후처리
			tNode.height = 1 + max(tNode.right.height, tNode.left.height)
			type = self.__needBalance(tNode)
			if type != self.NO_NEED:
				tNode = self.__balanceAVL(tNode, type)
			return (tNode, rtnItem)

	# 균형 잡기
	def __balanceAVL(self, tNode:AVLNode, type:int) -> AVLNode:
		returnNode = self.NIL
		if type == self.LL:
			returnNode = self.__rightRotate(tNode)
		elif type == self.LR:
			tNode.left = self.__leftRotate(tNode.left)
			returnNode = self.__rightRotate(tNode)
		elif type == self.RR:
			returnNode = self.__leftRotate(tNode)
		elif type == self.RL:
			tNode.right = self.__rightRotate(tNode.right)
			returnNode = self.__leftRotate(tNode)
		else:
			print("Impossible type! Should be one of LL, LR, RR, RL")
		return returnNode

	# 좌회전
	def __leftRotate(self, t:AVLNode) -> AVLNode:
		RChild = t.right
		if RChild == self.NIL:
			print(t.item, "'s RChild shouldn't be NIL!")
		RLChild = RChild.left
		RChild.left = t   # RChild가 루트 노드
		t.right = RLChild   # t의 새로운 오른자식 RLChild
		t.height = 1 + max(t.left.height, t.right.height)
		RChild.height = 1 + max(RChild.left.height, RChild.right.height)
		return RChild

	# 우회전
	def __rightRotate(self, t:AVLNode) -> AVLNode:
		LChild = t.left
		if LChild == self.NIL:
			print(t.item, "'s LChild shouldn't be NIL!")
		LRChild = LChild.right
		LChild.right = t   # LChild가 루트 노드
		t.left = LRChild   # t의 새로운 왼자식 LRChild
		t.height = 1 + max(t.left.height, t.right.height)
		LChild.height = 1 + max(LChild.left.height, LChild.right.height)
		return LChild

	# 유형 파악
	def __needBalance(self, t:AVLNode) -> int:
		type = self.ILLEGAL
		if (t.left.height + 2 <= t.right.height):   # R 유형
			if (t.right.left.height) <= t.right.right.height:
				type = self.RR
			else:
				type = self.RL
		elif t.left.height >= t.right.height + 2:   # L 유형
			if (t.left.left.height) >= t.left.right.height:
				type = self.LL
			else:
				type = self.LR
		else:   # 균형 잡기 필요 없음
			type = self.NO_NEED
		return type

	def isEmpty(self) -> bool:
		return self.__root == self.NIL

	def clear(self):
		self.__root = self.NIL
