def insertionSort(A):
	for i in range(1, len(A)):   # 첫 원소부터 역순으로 정렬
		loc = i-1   # 정렬된 부분의 끝 인덱스
		newItem = A[i]   # 정렬 할 원소
		while loc >= 0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			loc -= 1
		A[loc+1] = newItem

# n^2의 점근적 수행 시간을 가짐 (기본 정렬)
# 기본 정렬은 삽입, 선택, 버블 순으로 빠름
