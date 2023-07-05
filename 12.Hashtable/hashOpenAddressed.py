class HashOpenAddressed:
	def __init__(self, n:int):
		self.__table = [None for i in range(n)]
		self.__numItems = 0   # 총 노드 수
		self.__DELETED = -54321   # 채워져있다가 삭제된 경우 저장

	def __hash(self, i:int, x):   # i번째 해시 함수
		return (x + i) % len(self.__table)   # 선형 탐색
 
	def insert(self, x):
		if self.__numItems == len(self.__table):
		else:
			for i in range(len(self.__table)):
				slot = self.__hash(i, x)
				if self.__table[slot] == None or self.__table[slot] == self.__DELETED:   # 비어있음
					self.__table[slot] = x
					self.__numItems += 1
					break

	NOT_FOUND = -12345   # 검색 실패 상수
	def search(self, x) -> int:
		for i in range(len(self.__table)):
			slot = self.__hash(i, x)
			if self.__table[slot] == None:   # 검색 실패
				return HashOpenAddressed.NOT_FOUND
			if self.__table[slot] == x:   # 검색 성공
				return slot   # 인덱스 리턴
		return self.__NOT_FOUND   # 검색 실패

	def delete(self, x):
		for i in range(len(self.__table)):
			slot = self.__hash(i, x)
			if self.__table[slot] == None:   # 검색 실패
				break
			if self.__table[slot] == x:   # 검색 성공
				self.__table[slot] = self.__DELETED;   # 키 대신하여 저장 (다른 키의 검색을 위해 비우지 않고 상수값 저장)
				self.__numItems -= 1
				break

# 체이닝방법에서는 적재율 a가 1을 넘을 수 없음
# 탐색 횟수의 기대치는 검색 실패 시 1/(1-a) 이하, 성공 시 (1/a)log1/(1-a) 이하
# a 값이 1에 가까워질수록 기대치는 급격히 탐색 횟수 기대치 급격히 커짐 (a > 1/2 로 커지면 해시 테이블 크기를 2배로 조정) 
# 이론적으로는 체이닝방법이 개방주소방법보다 좋음
# 적재율이 그리 높지 않은 경우 추가 공간이 필요하지 않는 개방주소방법 선호
