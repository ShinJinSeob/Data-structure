def selectionSort(A):
	for last in range(len(A)-1, 0, -1):   # 끝 인덱스부터 역순으로 정렬
		k = theLargest(A, last)	
		A[k], A[last] =  A[last], A[k]

def theLargest(A, last:int) -> int:   # 가장 큰 수의 인덱스 리턴
	largest = 0
	for i in range(last+1):
		if A[i] > A[largest]:
			largest = i
	return largest

# n^2의 점근적 수행 시간을 가짐 (기본 정렬)
# 기본 정렬은 삽입, 선택, 버블 순으로 빠름
