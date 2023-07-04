def shellSort(A):
	H = gapSequence(len(A))
	for h in H:
		for k in range(h):   # 간격이 h 인 부분리스트 각각에 대해 삽입정렬
			stepInsertionSort(A, k, h)

def stepInsertionSort(A, k:int, h:int):   # A[k, k+h, k+2h, ...] 삽입정렬
	for i in range(k + h, len(A), h):
		j = i - h
		newItem = A[i]
		while 0 <= j and newItem < A[j]:
			A[j + h] = A[j]
			j -= h
		A[j + h] = newItem

def gapSequence(n:int) -> list:   # 갭 수열 생성
	H = [1]; gap = 1
	while gap < n/5:
		gap = 3 * gap + 1
		H.append(gap)
	H.reverse()
	return H

# O(n^(1+(1/v)))의 점근적 수행 시간을 가짐 (고급 정렬)
# 리스트의 크기가 작을 경우 퀵, 셸, 병합, 힙 순, 클 경우 퀵, 병합, 셸, 힙 순으로 빠름
# 삽입정렬의 획기적인 개선
