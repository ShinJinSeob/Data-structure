def heapSort(A):
	buildHeap(A)
	for last in range(len(A)-1, 0, -1):
		A[last], A[0] = A[0], A[last]   # 역순으로 정렬
		percolateDown(A, 0, last-1)   # 정렬된 부분 제외하고 힙으로 만들기

def buildHeap(A):   # 리스트 힙으로 만들기
	for i in range((len(A)-2) // 2, -1, -1):
		percolateDown(A, i, len(A)-1)

# A[k]를 루트로 하는 서브 트리가 A[k...end] 범위 내에서 힙 특성을 만족하도록 수선
def percolateDown(A, k:int, end:int):
	child = 2*k+1
	right = 2*k+2
	if child <= end:
		if right <= end and A[child] < A[right]:
			child = right
		if A[k] < A[child]:
			A[k], A[child] = A[child], A[k]
			percolateDown(A, child, end)

# θ(nlogn)의 점근적 수행 시간을 가짐 (고급 정렬)
# 고급 정렬은 퀵, 병합, 힙 순으로 빠름
# 최악의 경우에도 θ(nlogn) 의 수행 시간을 가지고 추가적인 공간도 요구하지 않는 이론적으로는 완벽한 알고리즘
